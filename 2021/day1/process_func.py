from functools import reduce


def count_inc(accum, depth):
    counter, idx, old_depth = accum
    if idx > 0 and old_depth < depth:
        counter += 1
    return (counter, idx+1, depth)



with open("input.txt", "r") as f:
    counter = 0
    depths = f.readlines()
    
    depths_ints = map(lambda x: int(x.strip()), depths)

    counter, _, _ = reduce(count_inc, depths_ints, (0,0,0))

    print("counter = ", counter)