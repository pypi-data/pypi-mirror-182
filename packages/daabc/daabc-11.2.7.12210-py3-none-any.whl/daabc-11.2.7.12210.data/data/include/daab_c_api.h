#ifndef __DAAB__C__API__
#define __DAAB__C__API__

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <math.h>
#include <sys/time.h>
#include <sys/timeb.h>
#include <stdbool.h>

#include <cblas.h>

#define NUM_FACTORS 512
#define MAX_FIELD_QUOTA 10
#define MAX_FIELD_QUOTA_PYBIN 5
#define MAX_FIELD_ALST 8
#define MAX_FIELD_STRUCETED 8
#define MAX_FIELD_UNSTRUCETED 32
#define MAX_THREADS 500
#define MAX_BUFFER_WINDOW 64
#define MAX_BUFFER_WINDOW_UNSTRUCTED 5120
#define MSEC_TICK 3000
#define MSEC_FACTOR 3000
#define MAX_FIELD_TIME_SERIES 4
#define MAX_FIELD_MACDS 5

#define VOLUME_WINDOW_START_RANK_TICK 201
#define VOLUME_WINDOW_STEP_BASIC 0.1
#define VOLUME_WINDOW_FOR_ABNORMAL_P 0.00033

#define SPCSR_ROWS_ORDERBOOK_500 28441
#define SPCSR_MAX_NONZERO MAX_ID

#define SECOND_130000_MINUS_093000 12600000
#define SECOND_130000_MINUS_113000 5400000

#define MAX_ID 1048576
#define MAX_FIELD_HASHMAP 8
#define LENGTH_BLOOMFILTER_0 32768
#define LENGTH_BLOOMFILTER_1 65536
#define LENGTH_BLOOMFILTER_2 131072

#define MULTIPLIER_HASHMAP (MAX_ID * MAX_FIELD_HASHMAP)

#define SIZE_TYPE_DB_FT 1024
#define SIZE_TYPE_DB_MP 32
#define SIZE_TYPE_DB_VS 32
#define SIZE_TYPE_DB_VS_MUL 8
#define SIZE_TYPE_DB_VS_MP 2
#define SIZE_TYPE_DB_GP 5
// #define SIZE_TYPE_DB_RK 2

int write_symbol_list(char *file, int *symbol_list, const int process, int *list_len_ob);

void hashmap_modify(int *hashmap, int *ob, const int _id, const int _dir, const int _price, const int _volume, const int _lp, const int _lob);

void preprocess_transaction(const int rank_tick, int *_time_trflow_latest, const int LOB, int *_buf_ORDERFLOW_BID, int *_buf_ORDERFLOW_ASK, int *_buf_ORDERFLOW_VOL);

void process_transaction(const int rank_tick, int *_time_trflow_latest, const int _id0, const int _id1, const int PRICE, const int VOLUME, const int LOB, const int _idx_lob, int *_buf_ORDERFLOW_BID, int *_buf_ORDERFLOW_ASK, int *_buf_ORDERFLOW_VOL, int *_price_trade_latest, int *_delta_acc, bool _if_modify_acc);

double refresh_volume_window(const int LOB, const int _idx_mid, const int _price_window, int *_buf_ORDERBOOK, int *_buf_ORDERFLOW_BID, int *_buf_ORDERFLOW_ASK);
double refresh_volume_window_atomic(const int LOB, const int _price_window, const bool _if_bid, const int _idx_p1, int *_buf_ORDERBOOK, int volume, double *_tmp);
void add_vw(int _id0, int _id1, int rank_thread, int LOB, double *_buf_vw_atomic, int *_buf_price_window, double *_buf_unstructed, int _offset_unstructed_IDXASK1, int _offset_unstructed_IDXBID1, int *_time_market_latest, int *_buf_latest_orderbook, int *_list_len_ob, int sum_len_ob, int VOLUME, double *_tmptmpd);

typedef struct
{
    double *d_feature;
    double *d_mid_price;
    double *d_volumes;
    double *d_gaps;
    int rank;
    int p_mp;
    int p_vs;
} DASHBOARD;

void dashboard_malloc(DASHBOARD *x, int n);
void dashboard_free(DASHBOARD *x, int n);

void dashboard_write_rk(DASHBOARD *x, int t);
void dashboard_write_mp(DASHBOARD *x, double t);
void dashboard_write_vs(DASHBOARD *x, double t, int pe);
void dashboard_write_gp(DASHBOARD *x, double *t);
void dashboard_refresh_vs(DASHBOARD *x);
void dashboard_calc_ft(DASHBOARD *x);    

int factor_toolbox(double *_x, int _time, int LOB, int *_buf_structed, double *_buf_unstructed, double *_buf_macds);

typedef struct
{
    int *_row_offsets;
    int *_col_indices;
    int *_values;
} spcsr_z;

typedef struct
{
    spcsr_z lob;
    spcsr_z ofl;
} L2DATA_G;

void SPCSR_Z_malloc(spcsr_z *d, int n);
void SPCSR_Z_free(spcsr_z *d, int n);

void L2DATA_G_malloc(L2DATA_G *d, int n);
void L2DATA_G_free(L2DATA_G *d, int n);

void MultiProcessAlloc_XTECHZMQ(char *symbol, char symbol_list[][7], int num_symbol, int num_process, int *alloc);
void RealtimeDataProcess_XTECHZMQ_V1(char *line, int *data);
void RealtimeDataProcess_XTECHZMQ_V2(char *line, int *data);
void RealtimeDataProcess_XTECHZMQ_V3(char *line, int *data, int date);
void RealtimeDataProcess_XTECHZMQ_V4(char *line, int *data, int date);

long long GetUnixTime();

int str2time(char *date_time);
int str2time4format(char *date_time, char *format);
int str2time4nodate(char *only_time);

int min(int a, int b);
int max(int a, int b);

int PRICE100X(char *p);
int PRICE1000X(char *p);

int symbol_id(char *symbol, char symbol_list[][7], int pa, int pb);

void itoa_symbol(int symbol_int, char *symbol);

unsigned hash_loc(unsigned key);
int hash_put(int key, int *KeyID);
int hash_find(int key, int *KeyID);

unsigned bloom_filter_hash_func_0(unsigned key, uint32_t *bf);
unsigned bloom_filter_hash_func_1(unsigned key, uint32_t *bf);
unsigned bloom_filter_hash_func_2(unsigned key, uint32_t *bf);

void get_fname_cfg(char *ds, char *feature, char *lob, char *_file_date_symbol);

#endif
