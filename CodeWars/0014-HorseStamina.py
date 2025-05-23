import timeit
import unittest
from itertools import groupby

# ---------- Initial Solution ----------
def estimator(obstacles, stamina):
    # Can use Two pointers: When encountering a 1, move second pointer forward until it reaches 0
    # move second pointer forward counting continuious occurances of 1, adjust by subtracing from
    # stamina (occurances squared plus 1)

    lp = 0
    rp = 0
    while lp < len(obstacles):
        if obstacles[lp] == 1:
            rp = lp
            while rp <= len(obstacles)-1 and obstacles[rp] == 1:
                rp += 1
            stamina -= (lp-rp) * (lp-rp) + 1
            lp = rp
        lp += 1
    return stamina >= 0

# ---------- Additional Solution ----------
def estimatorTwo(obstacles, stamina):
    return stamina >= sum(len(list(g)) ** 2 + 1 for k, g in groupby(obstacles) if k == 1)

# ---------- Additional Solution ----------
# The mimimum value to subtract will always be two. set cost = 2.
# As we iterate through each number in the list, when we encounter the first
# occurance of 1, we subtract cost from stamina and calculate how much we 
# should add to to cost, so if another 1 appears next in the sequence, the
# correct amount can be subtracted from stamina: E.g. we need to add 3 to cost
# so if two 1's are encountered in a sequence, we are subtracting 5 from the
# stamina. Reset cost to 2 when encountering a 0.
def estimatorThree(obstacles, stamina):
    cost = 2
    for i in obstacles:
        if i:
            stamina -= cost
            cost += (cost // 2 + cost % 2)
        else:
            cost = 2
    return stamina >= 0

# ---------- Tests ----------
class Test(unittest.TestCase):
    def testestimator(self):
        for data in testData:
            self.assertEqual(estimator(data[0], data[1]), data[2])
    
    def testestimatorTwo(self):
        for data in testData:
            self.assertEqual(estimatorTwo(data[0], data[1]), data[2])
    
    def testestimatorThree(self):
        for data in testData:
            self.assertEqual(estimatorThree(data[0], data[1]), data[2])

#  ---------- Testing Data ----------
testData = [
    [[0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0], 18, False],
    [[0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0], 20, True],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1, True],
    [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 15, False],
    [[1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], 60, True],
    [[1, 1, 1], 5, False],
    [[1, 1], 5, True],
    [[1], 4, True],
    [[1], 0, False],
    [[0, 1, 0, 0, 0, 0, 1], 3, False],
    [[1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1], 40, True]
]

# ---------- Main Program ----------
if __name__ == '__main__':
  # print(f'Reverse Letter Function: {timeit.timeit(lambda: estimator(testData[3][0], testData[3][1]), number=1000000)}')
  # print(
  # f'Reverse Letter Two Function: {timeit.timeit(lambda: estimatorTwo(testData[3][0], testData[3][1]), number=1000000)}')
  # print(
  # f'Reverse Letter Three Function: {timeit.timeit(lambda: estimatorThree(testData[3][0], testData[3][1]), number=1000000)}')

  # Reverse Letter Function: 1.7880034999980126
  # Reverse Letter Two Function: 3.189092599997821
  # Reverse Letter Three Function: 0.7948039000002609

  # ---------- Results ----------
  for data in testData:
      result = estimatorThree(data[0], data[1])
      print(result)

  # ---------- Run Tests ----------
  unittest.main()