/*--------------------------------------------------------------------
 * Symbols referenced in this file:
 * - datumCopy
 * - datumGetSize
 * - datumIsEqual
 *--------------------------------------------------------------------
 */

/*-------------------------------------------------------------------------
 *
 * datum.c
 *	  POSTGRES Datum (abstract data type) manipulation routines.
 *
 * Portions Copyright (c) 1996-2021, PostgreSQL Global Development Group
 * Portions Copyright (c) 1994, Regents of the University of California
 *
 *
 * IDENTIFICATION
 *	  src/backend/utils/adt/datum.c
 *
 *-------------------------------------------------------------------------
 */

/*
 * In the implementation of these routines we assume the following:
 *
 * A) if a type is "byVal" then all the information is stored in the
 * Datum itself (i.e. no pointers involved!). In this case the
 * length of the type is always greater than zero and not more than
 * "sizeof(Datum)"
 *
 * B) if a type is not "byVal" and it has a fixed length (typlen > 0),
 * then the "Datum" always contains a pointer to a stream of bytes.
 * The number of significant bytes are always equal to the typlen.
 *
 * C) if a type is not "byVal" and has typlen == -1,
 * then the "Datum" always points to a "struct varlena".
 * This varlena structure has information about the actual length of this
 * particular instance of the type and about its value.
 *
 * D) if a type is not "byVal" and has typlen == -2,
 * then the "Datum" always points to a null-terminated C string.
 *
 * Note that we do not treat "toasted" datums specially; therefore what
 * will be copied or compared is the compressed data or toast reference.
 * An exception is made for datumCopy() of an expanded object, however,
 * because most callers expect to get a simple contiguous (and pfree'able)
 * result from datumCopy().  See also datumTransfer().
 */

#include "postgres.h"

#include "access/detoast.h"
#include "common/hashfn.h"
#include "fmgr.h"
#include "utils/builtins.h"
#include "utils/datum.h"
#include "utils/expandeddatum.h"


/*-------------------------------------------------------------------------
 * datumGetSize
 *
 * Find the "real" size of a datum, given the datum value,
 * whether it is a "by value", and the declared type length.
 * (For TOAST pointer datums, this is the size of the pointer datum.)
 *
 * This is essentially an out-of-line version of the att_addlength_datum()
 * macro in access/tupmacs.h.  We do a tad more error checking though.
 *-------------------------------------------------------------------------
 */
Size
datumGetSize(Datum value, bool typByVal, int typLen)
{
	Size		size;

	if (typByVal)
	{
		/* Pass-by-value types are always fixed-length */
		Assert(typLen > 0 && typLen <= sizeof(Datum));
		size = (Size) typLen;
	}
	else
	{
		if (typLen > 0)
		{
			/* Fixed-length pass-by-ref type */
			size = (Size) typLen;
		}
		else if (typLen == -1)
		{
			/* It is a varlena datatype */
			struct varlena *s = (struct varlena *) DatumGetPointer(value);

			if (!PointerIsValid(s))
				ereport(ERROR,
						(errcode(ERRCODE_DATA_EXCEPTION),
						 errmsg("invalid Datum pointer")));

			size = (Size) VARSIZE_ANY(s);
		}
		else if (typLen == -2)
		{
			/* It is a cstring datatype */
			char	   *s = (char *) DatumGetPointer(value);

			if (!PointerIsValid(s))
				ereport(ERROR,
						(errcode(ERRCODE_DATA_EXCEPTION),
						 errmsg("invalid Datum pointer")));

			size = (Size) (strlen(s) + 1);
		}
		else
		{
			elog(ERROR, "invalid typLen: %d", typLen);
			size = 0;			/* keep compiler quiet */
		}
	}

	return size;
}

/*-------------------------------------------------------------------------
 * datumCopy
 *
 * Make a copy of a non-NULL datum.
 *
 * If the datatype is pass-by-reference, memory is obtained with palloc().
 *
 * If the value is a reference to an expanded object, we flatten into memory
 * obtained with palloc().  We need to copy because one of the main uses of
 * this function is to copy a datum out of a transient memory context that's
 * about to be destroyed, and the expanded object is probably in a child
 * context that will also go away.  Moreover, many callers assume that the
 * result is a single pfree-able chunk.
 *-------------------------------------------------------------------------
 */
Datum
datumCopy(Datum value, bool typByVal, int typLen)
{
	Datum		res;

	if (typByVal)
		res = value;
	else if (typLen == -1)
	{
		/* It is a varlena datatype */
		struct varlena *vl = (struct varlena *) DatumGetPointer(value);

		if (VARATT_IS_EXTERNAL_EXPANDED(vl))
		{
			/* Flatten into the caller's memory context */
			ExpandedObjectHeader *eoh = DatumGetEOHP(value);
			Size		resultsize;
			char	   *resultptr;

			resultsize = EOH_get_flat_size(eoh);
			resultptr = (char *) palloc(resultsize);
			EOH_flatten_into(eoh, (void *) resultptr, resultsize);
			res = PointerGetDatum(resultptr);
		}
		else
		{
			/* Otherwise, just copy the varlena datum verbatim */
			Size		realSize;
			char	   *resultptr;

			realSize = (Size) VARSIZE_ANY(vl);
			resultptr = (char *) palloc(realSize);
			memcpy(resultptr, vl, realSize);
			res = PointerGetDatum(resultptr);
		}
	}
	else
	{
		/* Pass by reference, but not varlena, so not toasted */
		Size		realSize;
		char	   *resultptr;

		realSize = datumGetSize(value, typByVal, typLen);

		resultptr = (char *) palloc(realSize);
		memcpy(resultptr, DatumGetPointer(value), realSize);
		res = PointerGetDatum(resultptr);
	}
	return res;
}

/*-------------------------------------------------------------------------
 * datumTransfer
 *
 * Transfer a non-NULL datum into the current memory context.
 *
 * This is equivalent to datumCopy() except when the datum is a read-write
 * pointer to an expanded object.  In that case we merely reparent the object
 * into the current context, and return its standard R/W pointer (in case the
 * given one is a transient pointer of shorter lifespan).
 *-------------------------------------------------------------------------
 */


/*-------------------------------------------------------------------------
 * datumIsEqual
 *
 * Return true if two datums are equal, false otherwise
 *
 * NOTE: XXX!
 * We just compare the bytes of the two values, one by one.
 * This routine will return false if there are 2 different
 * representations of the same value (something along the lines
 * of say the representation of zero in one's complement arithmetic).
 * Also, it will probably not give the answer you want if either
 * datum has been "toasted".
 *
 * Do not try to make this any smarter than it currently is with respect
 * to "toasted" datums, because some of the callers could be working in the
 * context of an aborted transaction.
 *-------------------------------------------------------------------------
 */
bool
datumIsEqual(Datum value1, Datum value2, bool typByVal, int typLen)
{
	bool		res;

	if (typByVal)
	{
		/*
		 * just compare the two datums. NOTE: just comparing "len" bytes will
		 * not do the work, because we do not know how these bytes are aligned
		 * inside the "Datum".  We assume instead that any given datatype is
		 * consistent about how it fills extraneous bits in the Datum.
		 */
		res = (value1 == value2);
	}
	else
	{
		Size		size1,
					size2;
		char	   *s1,
				   *s2;

		/*
		 * Compare the bytes pointed by the pointers stored in the datums.
		 */
		size1 = datumGetSize(value1, typByVal, typLen);
		size2 = datumGetSize(value2, typByVal, typLen);
		if (size1 != size2)
			return false;
		s1 = (char *) DatumGetPointer(value1);
		s2 = (char *) DatumGetPointer(value2);
		res = (memcmp(s1, s2, size1) == 0);
	}
	return res;
}

/*-------------------------------------------------------------------------
 * datum_image_eq
 *
 * Compares two datums for identical contents, based on byte images.  Return
 * true if the two datums are equal, false otherwise.
 *-------------------------------------------------------------------------
 */


/*-------------------------------------------------------------------------
 * datum_image_hash
 *
 * Generate a hash value based on the binary representation of 'value'.  Most
 * use cases will want to use the hash function specific to the Datum's type,
 * however, some corner cases require generating a hash value based on the
 * actual bits rather than the logical value.
 *-------------------------------------------------------------------------
 */


/*-------------------------------------------------------------------------
 * btequalimage
 *
 * Generic "equalimage" support function.
 *
 * B-Tree operator classes whose equality function could safely be replaced by
 * datum_image_eq() in all cases can use this as their "equalimage" support
 * function.
 *
 * Currently, we unconditionally assume that any B-Tree operator class that
 * registers btequalimage as its support function 4 must be able to safely use
 * optimizations like deduplication (i.e. we return true unconditionally).  If
 * it ever proved necessary to rescind support for an operator class, we could
 * do that in a targeted fashion by doing something with the opcintype
 * argument.
 *-------------------------------------------------------------------------
 */


/*-------------------------------------------------------------------------
 * datumEstimateSpace
 *
 * Compute the amount of space that datumSerialize will require for a
 * particular Datum.
 *-------------------------------------------------------------------------
 */


/*-------------------------------------------------------------------------
 * datumSerialize
 *
 * Serialize a possibly-NULL datum into caller-provided storage.
 *
 * Note: "expanded" objects are flattened so as to produce a self-contained
 * representation, but other sorts of toast pointers are transferred as-is.
 * This is because the intended use of this function is to pass the value
 * to another process within the same database server.  The other process
 * could not access an "expanded" object within this process's memory, but
 * we assume it can dereference the same TOAST pointers this one can.
 *
 * The format is as follows: first, we write a 4-byte header word, which
 * is either the length of a pass-by-reference datum, -1 for a
 * pass-by-value datum, or -2 for a NULL.  If the value is NULL, nothing
 * further is written.  If it is pass-by-value, sizeof(Datum) bytes
 * follow.  Otherwise, the number of bytes indicated by the header word
 * follow.  The caller is responsible for ensuring that there is enough
 * storage to store the number of bytes that will be written; use
 * datumEstimateSpace() to find out how many will be needed.
 * *start_address is updated to point to the byte immediately following
 * those written.
 *-------------------------------------------------------------------------
 */


/*-------------------------------------------------------------------------
 * datumRestore
 *
 * Restore a possibly-NULL datum previously serialized by datumSerialize.
 * *start_address is updated according to the number of bytes consumed.
 *-------------------------------------------------------------------------
 */

