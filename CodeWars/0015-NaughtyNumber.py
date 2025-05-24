import timeit
import unittest
import copy

# ---------- Initial Solution ----------
def naughty_number(arr):
    for i in range(len(arr)):
        while len(arr[i]) != 0:
            item = arr[i].pop()
            if isinstance(item, int):
                return i
            arr[i].extend(item)

# ---------- Additional Solution ----------
def naughty_number_two(arr):
    return next(i for i, x in enumerate(arr) if any(str.isdigit(c) for c in str(x)))

# ---------- Additional Solution ----------
def naughty_number_three(arr):
    for i in range(len(arr)):
        for a in str(arr[i]):
            if a != '[' and a != ']':
                return i

# ---------- Tests ----------
class Test(unittest.TestCase):
    def testNaughtyNumber(self):
        for data in testDataTwo:
            self.assertEqual(naughty_number(data[0]), data[1])
    
    def testNaughtyNumberTwo(self):
        for data in testDataThree:
            self.assertEqual(naughty_number(data[0]), data[1])
    
    def testNaughtyNumberThree(self):
        for data in testDataFour:
            self.assertEqual(naughty_number(data[0]), data[1])

#  ---------- Testing Data ----------
testData = [
    [[[[[]]], [[]], [], [], [[2]]], 4],
    [[[1]], 0],
    [[[], [8], [], []], 1],
    [[[[[[[[[[42]]]]]]]]], 0],
    [[[], [], [], [], [], [], [], [], [], [], [], [77]], 11],
    [[[[]], [[[[[]]]]], [], [[[[[[[[[]]]]]]]]], [[[]]], [[[[31]]]], [[]], []], 5],
    [[[1], [[[[]]]], [[]], [[[[[[[[[]]]]]]]]], []], 0]
]
testDataTwo = copy.deepcopy(testData)
testDataThree = copy.deepcopy(testData)
testDataFour = copy.deepcopy(testData)

if __name__ == '__main__':
    # a = [[[[]], [[[[[]]]]], [], [[[[[[[[[]]]]]]]]], [[[]]], [[[[31]]]], [[]], []]]
    # b = copy.deepcopy(a)
    # c = copy.deepcopy(b)

    # print(
    #     f'Naught Number Function: {timeit.timeit(lambda: naughty_number(a), number=10000000)}')
    # print(
    #     f'Naughty Number Two Function: {timeit.timeit(lambda: naughty_number_two(b), number=10000000)}')
    # print(
    #     f'Naughty Number Three Function: {timeit.timeit(lambda: naughty_number_three(c), number=10000000)}')
    
    # Naught Number Function: 3.621157800000219
    # Naughty Number Two Function: 77.94348119999995
    # Naughty Number Three Function: 39.78264150000177

    # ---------- Results ----------
    for data in testData:
        result = naughty_number(data[0])
        print(result)
    
    # # ---------- Run Tests ----------
    unittest.main()