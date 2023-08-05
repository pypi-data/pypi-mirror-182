/*-------------------------------------------------------------------------
 *
 * pg_operator_d.h
 *    Macro definitions for pg_operator
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
#ifndef PG_OPERATOR_D_H
#define PG_OPERATOR_D_H

#define OperatorRelationId 2617

#define Anum_pg_operator_oid 1
#define Anum_pg_operator_oprname 2
#define Anum_pg_operator_oprnamespace 3
#define Anum_pg_operator_oprowner 4
#define Anum_pg_operator_oprkind 5
#define Anum_pg_operator_oprcanmerge 6
#define Anum_pg_operator_oprcanhash 7
#define Anum_pg_operator_oprleft 8
#define Anum_pg_operator_oprright 9
#define Anum_pg_operator_oprresult 10
#define Anum_pg_operator_oprcom 11
#define Anum_pg_operator_oprnegate 12
#define Anum_pg_operator_oprcode 13
#define Anum_pg_operator_oprrest 14
#define Anum_pg_operator_oprjoin 15

#define Natts_pg_operator 15

#define BooleanNotEqualOperator 85
#define BooleanEqualOperator 91
#define Int4EqualOperator 96
#define Int4LessOperator 97
#define TextEqualOperator 98
#define NameEqualTextOperator 254
#define NameLessTextOperator 255
#define NameGreaterEqualTextOperator 257
#define TIDEqualOperator 387
#define TIDLessOperator 2799
#define TIDGreaterOperator 2800
#define TIDLessEqOperator 2801
#define TIDGreaterEqOperator 2802
#define Int8LessOperator 412
#define OID_NAME_REGEXEQ_OP 639
#define OID_TEXT_REGEXEQ_OP 641
#define TextLessOperator 664
#define TextGreaterEqualOperator 667
#define Float8LessOperator 672
#define BpcharEqualOperator 1054
#define OID_BPCHAR_REGEXEQ_OP 1055
#define BpcharLessOperator 1058
#define BpcharGreaterEqualOperator 1061
#define ARRAY_EQ_OP 1070
#define ARRAY_LT_OP 1072
#define ARRAY_GT_OP 1073
#define OID_NAME_LIKE_OP 1207
#define OID_TEXT_LIKE_OP 1209
#define OID_BPCHAR_LIKE_OP 1211
#define OID_NAME_ICREGEXEQ_OP 1226
#define OID_TEXT_ICREGEXEQ_OP 1228
#define OID_BPCHAR_ICREGEXEQ_OP 1234
#define OID_INET_SUB_OP 931
#define OID_INET_SUBEQ_OP 932
#define OID_INET_SUP_OP 933
#define OID_INET_SUPEQ_OP 934
#define OID_INET_OVERLAP_OP 3552
#define OID_NAME_ICLIKE_OP 1625
#define OID_TEXT_ICLIKE_OP 1627
#define OID_BPCHAR_ICLIKE_OP 1629
#define ByteaEqualOperator 1955
#define ByteaLessOperator 1957
#define ByteaGreaterEqualOperator 1960
#define OID_BYTEA_LIKE_OP 2016
#define TextPatternLessOperator 2314
#define TextPatternGreaterEqualOperator 2317
#define BpcharPatternLessOperator 2326
#define BpcharPatternGreaterEqualOperator 2329
#define OID_ARRAY_OVERLAP_OP 2750
#define OID_ARRAY_CONTAINS_OP 2751
#define OID_ARRAY_CONTAINED_OP 2752
#define RECORD_EQ_OP 2988
#define RECORD_LT_OP 2990
#define RECORD_GT_OP 2991
#define OID_RANGE_LESS_OP 3884
#define OID_RANGE_LESS_EQUAL_OP 3885
#define OID_RANGE_GREATER_EQUAL_OP 3886
#define OID_RANGE_GREATER_OP 3887
#define OID_RANGE_OVERLAP_OP 3888
#define OID_RANGE_CONTAINS_ELEM_OP 3889
#define OID_RANGE_CONTAINS_OP 3890
#define OID_RANGE_ELEM_CONTAINED_OP 3891
#define OID_RANGE_CONTAINED_OP 3892
#define OID_RANGE_LEFT_OP 3893
#define OID_RANGE_RIGHT_OP 3894
#define OID_RANGE_OVERLAPS_LEFT_OP 3895
#define OID_RANGE_OVERLAPS_RIGHT_OP 3896
#define OID_MULTIRANGE_LESS_OP 2862
#define OID_MULTIRANGE_LESS_EQUAL_OP 2863
#define OID_MULTIRANGE_GREATER_EQUAL_OP 2864
#define OID_MULTIRANGE_GREATER_OP 2865
#define OID_RANGE_OVERLAPS_MULTIRANGE_OP 2866
#define OID_MULTIRANGE_OVERLAPS_RANGE_OP 2867
#define OID_MULTIRANGE_OVERLAPS_MULTIRANGE_OP 2868
#define OID_MULTIRANGE_CONTAINS_ELEM_OP 2869
#define OID_MULTIRANGE_CONTAINS_RANGE_OP 2870
#define OID_MULTIRANGE_CONTAINS_MULTIRANGE_OP 2871
#define OID_MULTIRANGE_ELEM_CONTAINED_OP 2872
#define OID_MULTIRANGE_RANGE_CONTAINED_OP 2873
#define OID_MULTIRANGE_MULTIRANGE_CONTAINED_OP 2874
#define OID_RANGE_CONTAINS_MULTIRANGE_OP 4539
#define OID_RANGE_MULTIRANGE_CONTAINED_OP 4540
#define OID_RANGE_OVERLAPS_LEFT_MULTIRANGE_OP 2875
#define OID_MULTIRANGE_OVERLAPS_LEFT_RANGE_OP 2876
#define OID_MULTIRANGE_OVERLAPS_LEFT_MULTIRANGE_OP 2877
#define OID_RANGE_OVERLAPS_RIGHT_MULTIRANGE_OP 3585
#define OID_MULTIRANGE_OVERLAPS_RIGHT_RANGE_OP 4035
#define OID_MULTIRANGE_OVERLAPS_RIGHT_MULTIRANGE_OP 4142
#define OID_RANGE_ADJACENT_MULTIRANGE_OP 4179
#define OID_MULTIRANGE_ADJACENT_RANGE_OP 4180
#define OID_MULTIRANGE_ADJACENT_MULTIRANGE_OP 4198
#define OID_RANGE_LEFT_MULTIRANGE_OP 4395
#define OID_MULTIRANGE_LEFT_RANGE_OP 4396
#define OID_MULTIRANGE_LEFT_MULTIRANGE_OP 4397
#define OID_RANGE_RIGHT_MULTIRANGE_OP 4398
#define OID_MULTIRANGE_RIGHT_RANGE_OP 4399
#define OID_MULTIRANGE_RIGHT_MULTIRANGE_OP 4400

#endif							/* PG_OPERATOR_D_H */
