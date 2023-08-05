/*-------------------------------------------------------------------------
 *
 * pg_collation_d.h
 *    Macro definitions for pg_collation
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
#ifndef PG_COLLATION_D_H
#define PG_COLLATION_D_H

#define CollationRelationId 3456

#define Anum_pg_collation_oid 1
#define Anum_pg_collation_collname 2
#define Anum_pg_collation_collnamespace 3
#define Anum_pg_collation_collowner 4
#define Anum_pg_collation_collprovider 5
#define Anum_pg_collation_collisdeterministic 6
#define Anum_pg_collation_collencoding 7
#define Anum_pg_collation_collcollate 8
#define Anum_pg_collation_collctype 9
#define Anum_pg_collation_collversion 10

#define Natts_pg_collation 10


#define COLLPROVIDER_DEFAULT	'd'
#define COLLPROVIDER_ICU		'i'
#define COLLPROVIDER_LIBC		'c'

#define DEFAULT_COLLATION_OID 100
#define C_COLLATION_OID 950
#define POSIX_COLLATION_OID 951

#endif							/* PG_COLLATION_D_H */
