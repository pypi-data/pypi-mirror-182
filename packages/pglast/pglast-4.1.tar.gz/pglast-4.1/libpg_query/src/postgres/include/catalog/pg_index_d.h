/*-------------------------------------------------------------------------
 *
 * pg_index_d.h
 *    Macro definitions for pg_index
 *
 * Portions Copyright (c) 1996-2021, PostgreSQL Global Development Group
 * Portions Copyright (c) 1994, Regents of the University of California
 *
 * NOTES
 *  ******************************
 *  *** DO NOT EDIT THIS FILE! ***
 *  ******************************
 *
 *  It has been GENERATED by src/backend/catalog/genbki.pl
 *
 *-------------------------------------------------------------------------
 */
#ifndef PG_INDEX_D_H
#define PG_INDEX_D_H

#define IndexRelationId 2610

#define Anum_pg_index_indexrelid 1
#define Anum_pg_index_indrelid 2
#define Anum_pg_index_indnatts 3
#define Anum_pg_index_indnkeyatts 4
#define Anum_pg_index_indisunique 5
#define Anum_pg_index_indisprimary 6
#define Anum_pg_index_indisexclusion 7
#define Anum_pg_index_indimmediate 8
#define Anum_pg_index_indisclustered 9
#define Anum_pg_index_indisvalid 10
#define Anum_pg_index_indcheckxmin 11
#define Anum_pg_index_indisready 12
#define Anum_pg_index_indislive 13
#define Anum_pg_index_indisreplident 14
#define Anum_pg_index_indkey 15
#define Anum_pg_index_indcollation 16
#define Anum_pg_index_indclass 17
#define Anum_pg_index_indoption 18
#define Anum_pg_index_indexprs 19
#define Anum_pg_index_indpred 20

#define Natts_pg_index 20


/*
 * Index AMs that support ordered scans must support these two indoption
 * bits.  Otherwise, the content of the per-column indoption fields is
 * open for future definition.
 */
#define INDOPTION_DESC			0x0001	/* values are in reverse order */
#define INDOPTION_NULLS_FIRST	0x0002	/* NULLs are first instead of last */


#endif							/* PG_INDEX_D_H */
