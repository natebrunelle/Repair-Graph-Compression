import csv

#
# normal_algorithm_row_1 = 0
# row_3 = 0
# normal_using_compression_aware_row_5 = 0
# row_7 = 0
# bipartite_compression_time_row_9 = 0 #time for the compression of complete bipartite graph
# compressed_time_row_11 = 0 #time for compression aware algorithm on compressed graph
# row_13 = 0
# decompression_of_complete_bipartite1_row_15 = 0  #Time for actual decompression of complete bipartite graph

Size_of_generated_compressed_graph_row_1 = 0
Time_for_Compression_Aware_Bipartite_row_3 = 0
Time_for_Compression_Aware_Topological_Sort_row_5 = 0
Size_of_decompressed_graph_row_7 = 0
Time_for_Decompression_row_9 = 0
Time_for_Normal_Bipartite_row_11 = 0
Time_for_Normal_Topological_Sort_row_13 = 0


# for number in range(1,11):


filename = "algorithms/generated_compressed_final_tests/All_compression_ratios.csv"


# final_file = filename + "nodes" + str(number) + ".csv"
# final_file = filename+".csv"
f = open(filename)
csv_f = csv.reader(f)

# print(final_file)
rows = [r for r in csv_f]

i = 0
count = 0
ratios = [0.819, 0.82, 0.821, 0.822, 0.823, 0.824, 0.827, 0.828, 0.832, 0.833, 0.833, 0.835,0.84, 0.85]
for ratio in ratios:
    Size_of_generated_compressed_graph_row_1 = 0
    Time_for_Compression_Aware_Bipartite_row_3 = 0
    Time_for_Compression_Aware_Topological_Sort_row_5 = 0
    Size_of_decompressed_graph_row_7 = 0
    Time_for_Decompression_row_9 = 0
    Time_for_Normal_Bipartite_row_11 = 0
    Time_for_Normal_Topological_Sort_row_13 = 0

    count = 0
    i = 0
    print("")
    for r in rows:
        # print(i, r)
        i+=1
        if( str(ratio) == r[0]):
            count += 1
            file_to_grab = r[1]

            file_to_average = filename = "algorithms/generated_compressed_final_tests/" + file_to_grab
            f_temp = open(filename)
            reading_data = csv.reader(f_temp)
            read_data = [r for r in reading_data]

            Size_of_generated_compressed_graph_row_1 += (float(read_data[1][0]))
            Time_for_Compression_Aware_Bipartite_row_3 += (float(read_data[3][0]))
            Time_for_Compression_Aware_Topological_Sort_row_5 += (float(read_data[5][0]))
            Size_of_decompressed_graph_row_7 += (float(read_data[7][0]))
            Time_for_Decompression_row_9 += (float(read_data[9][0]))
            Time_for_Normal_Bipartite_row_11 += (float(read_data[11][0]))
            Time_for_Normal_Topological_Sort_row_13 += (float(read_data[13][0]))

            # speedup = (1-float(Time_for_Compression_Aware_Bipartite_row_3))/float(Time_for_Normal_Bipartite_row_11)
            # print("speedup", count, speedup)
            f_temp.close()

    # print(Size_of_decompressed_graph_row_7 / Size_of_generated_compressed_graph_row_1, "nodes" + str(number) + ".csv")

    f.close()

# print(Size_of_generated_compressed_graph_row_1)
    print(ratio)
    print("Size of generated compressed graph,", Size_of_generated_compressed_graph_row_1)
    print("Time for Compression Aware Bipartite,", Time_for_Compression_Aware_Bipartite_row_3)
    print("Time for Compression Aware Topological Sort,", Time_for_Compression_Aware_Topological_Sort_row_5)
    print("Size of decompressed graph,", Size_of_decompressed_graph_row_7)
    print("Time for Decompression, ", Time_for_Decompression_row_9)
    print("Time for Normal Bipartite,", Time_for_Normal_Bipartite_row_11)
    print("Time for Normal Topological Sort,", Time_for_Normal_Topological_Sort_row_13)

    print("COUNT,", count)