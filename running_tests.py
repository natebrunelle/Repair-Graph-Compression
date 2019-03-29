'''
purpose of this file is to run multiple instances of tests and log them automatically...
with a setup like this and a correct test file/function, this function and run overnight, running tests and logging results
'''

import tests.test_algorithms as testclass
import datetime

for number in range(1, 51):
    filename = "algorithms/bipartite_and_topsort_tests/fixed_bipartite/sparse_tests/sparse500nodes"
    # filename = "test"
    final_file = filename + str(number) + ".csv"
    # final_file = filename+".csv"
    f = open(final_file, 'w', newline='')

    print("started: ", number)
    datetime.datetime.now().time()
    datetime.time(15, 8, 24, 78915)
    print(datetime.datetime.now().time())

    c = (testclass.TestTopologicalSort().testTopologicalSorts())

    f.write(c)
    f.close()
    print("finished: ", number)
    datetime.datetime.now().time()
    datetime.time(15, 8, 24, 78915)
    print(datetime.datetime.now().time())
    print("")



