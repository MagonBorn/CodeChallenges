import timeit
from collections import Counter

# ---------- Initial Solution ----------
def right_depth(arr, constraints):
    counts = []
    for i in arr:
        count = 0
        while i:
            item = i.pop()
            if isinstance(item, list):
                count += 1
                i.extend(item)
        counts.append(count+1)
    return Counter(counts) <= Counter(constraints)

# ---------- Additional Solution ----------
def right_depth_two(arr, constraints):
    def depth(xs): return 1+depth(xs[0]) if xs else 1
    return Counter(map(depth, arr)) <= Counter(constraints)

# ---------- Additional Solution ----------
def right_depth_three(arr, constraints):
    return Counter(constraints) >= Counter(str(a).count("[") for a in arr)

# ---------- Additional Solution ----------
def right_depth_four(arr, constraints):
    def get_depth(xs):
        cur, depth = xs, 1
        while cur:
            depth += 1
            cur = cur[0]
        return depth
    return Counter(map(get_depth, arr)) <= Counter(constraints)   

#  ---------- Testing Data ----------
testData = [
    [[[[]], [], [[[]]], [], [[]]], {2: 1, 1: 2, 3: 1}, False],
    [[[[]], [], [[[]]], [], [[]]], {2: 6, 1: 2, 3: 1}, True],
    [[[[]], [], [[[]]], [], [[]]], {2: 6, 1: 2}, False],
    [[[[]], [], [[[]]], [], [[]]], {}, False],
    [[[[]], []], {2: 6, 1: 2, 3: 1, 10: 8, 5: 1, 6: 4}, True],
    [[[]], {1: 1}, True],
    [[[]], {}, False],
    [[[[]], [], [[[]]], [], [[]], [[[]]], [[[]]], [], [], [], [], [], [], [[]], [[[[[[[]]]]]]]], {2: 6, 1: 8, 3: 3, 7: 1}, True]
]

# ---------- Main Program ----------
if __name__ == '__main__':
    # a = [[[[]], [], [[[]]], [], [[]], [[[]]], [[[]]], [], [], [], [], [], [], [[]], [[[[[[[]]]]]]]],
    #      {2: 6, 1: 8, 3: 3, 7: 1}, True]
    
    # print(
    #     f'Right Depth Function: {timeit.timeit(lambda: right_depth(a[0], a[1]), number=10000000)}')
    # print(
    #     f'Right Depth Two Function: {timeit.timeit(lambda: right_depth_two(a[0], a[1]), number=10000000)}')
    # print(
    #     f'Right Depth Three Function: {timeit.timeit(lambda: right_depth_three(a[0], a[1]), number=10000000)}')
    # print(
    #     f'Right Depth Four Function: {timeit.timeit(lambda: right_depth_four(a[0], a[1]), number=10000000)}')

    # Right Depth Function: 35.352185399999144
    # Right Depth Two Function: 38.61897229999886
    # Right Depth Three Function: 57.89749809999921
    # Right Depth Four Function: 41.93897039999865

    for data in testData:
        result = right_depth(data[0], data[1])
        print(result)