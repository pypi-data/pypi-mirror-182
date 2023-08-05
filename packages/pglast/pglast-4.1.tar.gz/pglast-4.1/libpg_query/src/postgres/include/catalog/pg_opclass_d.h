/*-------------------------------------------------------------------------
 *
 * pg_opclass_d.h
 *    Macro definitions for pg_opclass
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
#ifndef PG_OPCLASS_D_H
#define PG_OPCLASS_D_H

#define OperatorClassRelationId 2616

#define Anum_pg_opclass_oid 1
#define Anum_pg_opclass_opcmethod 2
#define Anum_pg_opclass_opcname 3
#define Anum_pg_opclass_opcnamespace 4
#define Anum_pg_opclass_opcowner 5
#define Anum_pg_opclass_opcfamily 6
#define Anum_pg_opclass_opcintype 7
#define Anum_pg_opclass_opcdefault 8
#define Anum_pg_opclass_opckeytype 9

#define Natts_pg_opclass 9

#define DATE_BTREE_OPS_OID 3122
#define FLOAT8_BTREE_OPS_OID 3123
#define INT2_BTREE_OPS_OID 1979
#define INT4_BTREE_OPS_OID 1978
#define INT8_BTREE_OPS_OID 3124
#define NUMERIC_BTREE_OPS_OID 3125
#define OID_BTREE_OPS_OID 1981
#define TEXT_BTREE_OPS_OID 3126
#define TIMESTAMPTZ_BTREE_OPS_OID 3127
#define TIMESTAMP_BTREE_OPS_OID 3128
#define TEXT_BTREE_PATTERN_OPS_OID 4217
#define VARCHAR_BTREE_PATTERN_OPS_OID 4218
#define BPCHAR_BTREE_PATTERN_OPS_OID 4219

#endif							/* PG_OPCLASS_D_H */
