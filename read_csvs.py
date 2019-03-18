import csv
#
# dense_normal_bipartite_time_row_1 = 0
# dense_compression_aware_bipartite_time_row_4 = 0
# sparse_normal_bipartite_row_8 = 0
# sparse_compression_aware_bipartite_row_11 = 0
# decompressed_normal_bipartite_row_14 = 0
# dense_normal_topsort_row_18 = 0
# dense_compression_aware_topsort_row_20 = 0
# sparse_normal_topsort_row_22 = 0
# sparse_compression_aware_topsort_row_24 = 0
# decompressed_sparse_normal_topsort_row_26 = 0

normal_algorithm_row_1 = 0
normal_using_compression_aware_row_5 = 0
compressed_time_row_9 = 0
decompressed_normal_row_13 = 0
decompressed_using_compression_aware_row_17 = 0

dense_normal_time_row_20 = 0
dense_compression_aware_row_23 = 0
compressed_graph_row_26 = 0
decompressed_dense_using_normal_row_29 = 0
decompressd_dense_using_compression_aware_row_32 = 0

sparse_normal_topsort_row_36 = 0
sparse_compression_topsort_row_39 = 0
sparse_compressed_row_42 = 0
sparse_decompressed_normal_row_45 = 0
sparse_decompressed_compressionaware_row_48 = 0

for number in range(1,6):

    filename = "algorithms/bipartite_and_topsort/b_and_t_100nodes"

    final_file = filename+str(number)+".csv"
    # final_file = filename+".csv"
    f = open(final_file)
    csv_f = csv.reader(f)

    print(final_file)
    rows = [r for r in csv_f]

    # i = 0
    # for r in rows:
    #     print(i, r)
    #     i+=1

    normal_algorithm_row_1  += float(rows[1][0])
    normal_using_compression_aware_row_5 += float(rows[5][0])
    compressed_time_row_9 += float(rows[9][0])
    decompressed_normal_row_13 += float(rows[13][0])
    decompressed_using_compression_aware_row_17 += float(rows[17][0])

    dense_normal_time_row_20 += float(rows[20][0])
    dense_compression_aware_row_23 += float(rows[23][0])
    compressed_graph_row_26 += float(rows[26][0])
    decompressed_dense_using_normal_row_29 += float(rows[29][0])
    decompressd_dense_using_compression_aware_row_32 += float(rows[32][0])

    sparse_normal_topsort_row_36 += float(rows[36][0])
    sparse_compression_topsort_row_39 += float(rows[39][0])
    sparse_compressed_row_42 += float(rows[42][0])
    sparse_decompressed_normal_row_45 += float(rows[45][0])
    sparse_decompressed_compressionaware_row_48 += float(rows[48][0])
    # # dense_normal_bipartite_time_row_1 += float(rows[1][0])
    # # dense_compression_aware_bipartite_time_row_4 += float(rows[4][0])
    # # sparse_normal_bipartite_row_8 += float(rows[8][0])
    # # sparse_compression_aware_bipartite_row_11 += float(rows[11][0])
    # # decompressed_normal_bipartite_row_14 += float(rows[14][0])
    # # dense_normal_topsort_row_18 += float(rows[18][0])
    # # dense_compression_aware_topsort_row_20 += float(rows[20][0])
    # # sparse_normal_topsort_row_22 += float(rows[22][0])
    # # sparse_compression_aware_topsort_row_24 += float(rows[24][0])
    # # decompressed_sparse_normal_topsort_row_26 += float(rows[26][0])


    f.close()



print(normal_algorithm_row_1)
print(normal_using_compression_aware_row_5)
print(compressed_time_row_9)
print(decompressed_normal_row_13)
print(decompressed_using_compression_aware_row_17)

print(dense_normal_time_row_20)
print(dense_compression_aware_row_23)
print(compressed_graph_row_26)
print(decompressed_dense_using_normal_row_29)
print(decompressd_dense_using_compression_aware_row_32)

print(sparse_normal_topsort_row_36)
print(sparse_compression_topsort_row_39)
print(sparse_compressed_row_42)
print(sparse_decompressed_normal_row_45)
print(sparse_decompressed_compressionaware_row_48)
