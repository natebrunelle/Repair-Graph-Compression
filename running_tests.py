'''
purpose of this file is to run multiple instances of tests and log them automatically...
with a setup like this and a correct test file/function, this function and run overnight, running tests and logging results
'''

import tests.test_algorithms as testclass
import datetime


ret_str = ""
for number in range(1, 1000):
    # filename = "algorithms/generated_compressed_final_tests/1200nodes"
    # filename = "test"
    # final_file = filename + str(number) + ".csv"
    # final_file = filename+".csv"
    # print(final_file)
    # f = open(final_file, 'w', newline='')

    # print("started: ", number)
    datetime.datetime.now().time()
    datetime.time(15, 8, 24, 78915)
    # print(datetime.datetime.now().time())

    testclass.TestTopologicalSort().testControllingCompressionRatio(110)

    # f.write(c)
    # f.close()
    # print("finished: ", number)
    datetime.datetime.now().time()
    datetime.time(15, 8, 24, 78915)
    # print(datetime.datetime.now().time())
    print("")

