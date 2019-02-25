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

perfect_normal_row_1 = 0
perfect_compressed_row_4 = 0
perfect_decompressed_row_7 = 0

for number in range(1,6):

    filename = "Repair-Graph-Compression/algorithms/perfect_bipartite_300nodetest_"

    final_file = filename+str(number)+".csv"
    f = open(final_file)
    csv_f = csv.reader(f)

    print(final_file)
    rows = [r for r in csv_f]


    perfect_normal_row_1 += float(rows[1][0])
    perfect_compressed_row_4 += float(rows[4][0])
    perfect_decompressed_row_7 += float(rows[7][0])

    # dense_normal_bipartite_time_row_1 += float(rows[1][0])
    # dense_compression_aware_bipartite_time_row_4 += float(rows[4][0])
    # sparse_normal_bipartite_row_8 += float(rows[8][0])
    # sparse_compression_aware_bipartite_row_11 += float(rows[11][0])
    # decompressed_normal_bipartite_row_14 += float(rows[14][0])
    # dense_normal_topsort_row_18 += float(rows[18][0])
    # dense_compression_aware_topsort_row_20 += float(rows[20][0])
    # sparse_normal_topsort_row_22 += float(rows[22][0])
    # sparse_compression_aware_topsort_row_24 += float(rows[24][0])
    # decompressed_sparse_normal_topsort_row_26 += float(rows[26][0])


    f.close()

# print(dense_normal_bipartite_time_row_1)
# print(dense_compression_aware_bipartite_time_row_4)
# print(sparse_normal_bipartite_row_8)
# print(sparse_compression_aware_bipartite_row_11)
# print(decompressed_normal_bipartite_row_14)
# print(dense_normal_topsort_row_18)
# print(dense_compression_aware_topsort_row_20)
# print(sparse_normal_topsort_row_22)
# print(sparse_compression_aware_topsort_row_24)
# print(decompressed_sparse_normal_topsort_row_26)
print(perfect_normal_row_1)
print(perfect_compressed_row_4)
print(perfect_decompressed_row_7)
