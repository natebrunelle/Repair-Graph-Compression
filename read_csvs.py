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
row_3 = 0
normal_using_compression_aware_row_5 = 0
row_7 = 0
bipartite_compression_time_row_9 = 0 #time for the compression of complete bipartite graph
compressed_time_row_11 = 0 #time for compression aware algorithm on compressed graph
row_13 = 0
decompression_of_complete_bipartite1_row_15 = 0  #Time for actual decompression of complete bipartite graph

# decompressed_normal_row_17 = 0 #Time for DECOMPRESSED graph ran in normal algorithm:
# decompression_of_complete_bipartite2_row_21 = 0 #Time for actual decompression of complete bipartite graph:
# decompressed_using_compression_aware_row_23 = 0 #Time for DECOMPRESSED graph ran using compression aware algorithm:
#
# dense_normal_time_row_26 = 0 #Time for Dense Normal topsort
# dense_compression_aware_row_29 = 0 #Time for normal graph using compression aware topsort
# compression_of_dense_graph_row_32 = 0 #Time for compression of dense graph
# compressed_graph_row_34 = 0 # time for compressed graph ran in compression aware topsort
# decompression_of_dense_graph1_row_37 = 0 #Time for actual decompression of dense graph
# decompressed_dense_using_normal_row_39 = 0 #Time for Decompressed dense graph ran in normal topsort
# decompression_of_dense_graph2_row_42 = 0 #Time for actual decompression of dense graph:
# decompressd_dense_using_compression_aware_row_44 = 0 #Time for Decompressed dense graph ran in compression aware topsort:
# #---------------------------
# sparse_normal_topsort_row_48 = 0 #Time for Sparse Normal topsort:
# sparse_compression_topsort_row_51 = 0 #Time for Sparse compression aware topsort
# compression_of_sparse_graph_row_54 = 0 #Time for compression of sparse graph:
# sparse_compressed_row_56 = 0 #Time for Sparse Compression aware topsort:
# decompression_of_sparse_graph1_row_59 = 0 #Time for actual decompression of sparse graph:
# sparse_decompressed_normal_row_61 = 0 #Time for DECOMPRESSED Sparse 'normal' topsort:
# decompression_of_sparse_graph2_row_64 = 0 #Time for actual decompression of sparse graph:
# sparse_decompressed_compressionaware_row_66 = 0 #Time for DECOMPRESSED Sparse compression aware topsort

for number in range(1,51):

    filename = "algorithms/bipartite_and_topsort_tests/fixed_bipartite/sparse_tests/sparse2500nodes"

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

    normal_algorithm_row_1 += float(rows[1][0])
    row_3 += float(rows[3][0])
    normal_using_compression_aware_row_5 += float(rows[5][0])
    row_7 += float(rows[7][0])
    bipartite_compression_time_row_9 += float(rows[9][0])
    compressed_time_row_11 += float(rows[11][0])
    row_13 += float(rows[13][0])
    decompression_of_complete_bipartite1_row_15 += float(rows[15][0])

    # decompressed_normal_row_17 += float(rows[17][0])
    # decompression_of_complete_bipartite2_row_21 += float(rows[21][0])
    # decompressed_using_compression_aware_row_23 += float(rows[23][0])


    #
    # dense_normal_time_row_26 += float(rows[26][0])
    # dense_compression_aware_row_29 += float(rows[29][0])
    # compression_of_dense_graph_row_32 += float(rows[32][0])
    # compressed_graph_row_34 += float(rows[34][0])
    # decompression_of_dense_graph1_row_37 += float(rows[37][0])
    # decompressed_dense_using_normal_row_39 += float(rows[39][0])
    # decompression_of_dense_graph2_row_42 += float(rows[42][0])
    # decompressd_dense_using_compression_aware_row_44 += float(rows[44][0])
    # # ---------------------------
    # sparse_normal_topsort_row_48 += float(rows[48][0])
    # sparse_compression_topsort_row_51 += float(rows[51][0])
    # compression_of_sparse_graph_row_54 += float(rows[54][0])
    # sparse_compressed_row_56 += float(rows[56][0])
    # decompression_of_sparse_graph1_row_59 += float(rows[59][0])
    # sparse_decompressed_normal_row_61 += float(rows[61][0])
    # decompression_of_sparse_graph2_row_64 += float(rows[64][0])
    # sparse_decompressed_compressionaware_row_66 += float(rows[66][0])


    f.close()




print(normal_algorithm_row_1)
print(row_3)
print(normal_using_compression_aware_row_5)
print(row_7)
print(bipartite_compression_time_row_9) #time for the compression of complete bipartite graph
print(compressed_time_row_11) #time for compression aware algorithm on compressed graph
print(row_13)
print(decompression_of_complete_bipartite1_row_15)  #Time for actual decompression of complete bipartite graph
# print(decompressed_normal_row_17) #Time for DECOMPRESSED graph ran in normal algorithm:
# print(decompression_of_complete_bipartite2_row_21) #Time for actual decompression of complete bipartite graph:
# print(decompressed_using_compression_aware_row_23) #Time for DECOMPRESSED graph ran using compression aware algorithm:

# print(dense_normal_time_row_26) #Time for Dense Normal topsort
# print(dense_compression_aware_row_29) #Time for normal graph using compression aware topsort
# print(compression_of_dense_graph_row_32) #Time for compression of dense graph
# print(compressed_graph_row_34) # time for compressed graph ran in compression aware topsort
# print(decompression_of_dense_graph1_row_37) #Time for actual decompression of dense graph
# print(decompressed_dense_using_normal_row_39) #Time for Decompressed dense graph ran in normal topsort
# print(decompression_of_dense_graph2_row_42) #Time for actual decompression of dense graph:
# print(decompressd_dense_using_compression_aware_row_44) #Time for Decompressed dense graph ran in compression aware topsort:
# #---------------------------
# print(sparse_normal_topsort_row_48) #Time for Sparse Normal topsort:
# print(sparse_compression_topsort_row_51) #Time for Sparse compression aware topsort
# print(compression_of_sparse_graph_row_54) #Time for compression of sparse graph:
# print(sparse_compressed_row_56) #Time for Sparse Compression aware topsort:
# print(decompression_of_sparse_graph1_row_59) #Time for actual decompression of sparse graph:
# print(sparse_decompressed_normal_row_61) #Time for DECOMPRESSED Sparse 'normal' topsort:
# print(decompression_of_sparse_graph2_row_64) #Time for actual decompression of sparse graph:
# print(sparse_decompressed_compressionaware_row_66) #Time for DECOMPRESSED Sparse compression aware topsort
