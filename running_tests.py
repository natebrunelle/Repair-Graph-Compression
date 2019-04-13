'''
purpose of this file is to run multiple instances of tests and log them automatically...
with a setup like this and a correct test file/function, this function and run overnight, running tests and logging results
'''

import tests.test_algorithms as testclass
import datetime

for number in range(1, 1):
    filename = "algorithms/generating_random_compressed_results/10nodes_weighted_quarter"
    # filename = "test"
    final_file = filename + str(number) + ".csv"
    # final_file = filename+".csv"
    print(final_file)
    f = open(final_file, 'w', newline='')

    print("started: ", number)
    datetime.datetime.now().time()
    datetime.time(15, 8, 24, 78915)
    print(datetime.datetime.now().time())

    c = (testclass.TestTopologicalSort().setUpRandomCompression(10))

    f.write(c)
    f.close()
    print("finished: ", number)
    datetime.datetime.now().time()
    datetime.time(15, 8, 24, 78915)
    print(datetime.datetime.now().time())
    print("")



