with open("input.txt", "r") as f:
    counter = 0
    depths = f.readlines()
    old_depth = 0
    for idx, depth in enumerate(depths):
        d = int(depth.strip())
        if idx > 0 and old_depth < d:
            counter += 1
        old_depth = d
    print("counter = ", counter)