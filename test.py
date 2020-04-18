from timeit import default_timer as timer
import pytest

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

    assert one_results == full_results, "Test succeed. The costs from two algorithms are the same"

