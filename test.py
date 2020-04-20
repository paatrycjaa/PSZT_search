from timeit import default_timer as timer
import numpy as np
#import pytest

def sum_to_n(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail

def get_random_AB(n, min, max):
    for x in range(n) :
        yield np.random.randint(min, max, size=2)


def test_1 (one_to_one, full_search):
    one_results = []
    full_results = []
    start_one = timer()
    for x in sum_to_n(55, 2):
        one_to_one.setAB(x[0], x[1])
        one_results.append(one_to_one.simulation())
    t_one = timer() - start_one

    start_full = timer()
    for x in sum_to_n(55, 2):
        full_search.setAB(x[0], x[1])
        full_results.append(full_search.simulation())
    t_full = timer() - start_full

    print("Test 1")
    print(("%s : " + "%0.3g" + " seconds") % ("One_to_one", t_one))
    print(("%s : " + "%0.3g" + " seconds") % ("FullSearch", t_full))

    try:
        assert one_results == full_results

    except AssertionError:
        print("Test 1 failed. The costs from two algorithms are not the same")
    else:
        print("Test passed all costs are the same")

def test_2(one_to_one, full_search):
    one_results = []
    full_results = []
    t_one = 0
    t_full = 0
    for x in get_random_AB(20, 1, 55):
        start_one = timer()
        one_to_one.setAB(x[0], x[1])
        one_results.append(one_to_one.simulation())
        end_one = timer() - start_one
        t_one = t_one + end_one

        start_one = timer()
        full_search.setAB(x[0], x[1])
        full_results.append(full_search.simulation())
        end_one = timer() - start_one
        t_full = t_full + end_one

    print("Test 2")
    print(("%s : " + "%0.3g" + " seconds") % ("One_to_one", t_one))
    print(("%s : " + "%0.3g" + " seconds") % ("FullSearch", t_full))

    try:
        assert one_results == full_results

    except AssertionError:
        print("Test 2 failed. The costs from two algorithms are not the same")
    else:
        print("Test passed all costs are the same")

    



