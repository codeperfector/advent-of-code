from collections import deque
from functools import reduce
from itertools import islice


def count_inc(accum, depth):
    counter, idx, old_depth = accum
    if idx > 0 and old_depth < depth:
        counter += 1
    return (counter, idx+1, depth)

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield sum(window)
    for x in it:
        window.append(x)
        yield sum(window)

with open("input.txt", "r") as f:
    counter = 0
    depths = f.readlines()
    
    depths_ints_it = map(lambda x: int(x.strip()), depths)

    sums_it = sliding_window(depths_ints_it, 3)

    counter, _, _ = reduce(count_inc, sums_it, (0,0,0))

    print("counter = ", counter)