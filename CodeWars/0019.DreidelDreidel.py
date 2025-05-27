import math
import timeit
import unittest

# ---------- Initial Solution ----------
def gamble(rolls, my_coins, pot):
    for roll in rolls:
        match roll:
            case 'Nun':
                continue
            case 'Gimel':
                my_coins += pot
                pot = 0
            case 'Hei':
                my_coins += pot//2
                pot = math.ceil(pot/2)
            case 'Shin':
                my_coins -= 1
                pot += 1
    return my_coins

# ---------- Additional Solution ----------
def gambleAgain(rolls, my_coins, pot):
    actions = {
        "Nun": lambda c, p: (c, p),
   	    "Gimel": lambda c, p: (c + p, 0),
   	    "Hei": lambda c, p: (c + p//2, p - p//2),
   	    "Shin": lambda c, p: (c - 1, p + 1)
    }

    for roll in rolls:
        my_coins, pot = actions[roll](my_coins, pot)
    return my_coins

#  ---------- Testing Data ----------
testData = [
    [['Nun'], 10, 20, 10],
    [['Gimel'], 10, 20, 30],
    [['Hei', 'Shin'], 10, 20, 19],
    [['Hei', 'Hei'], 10, 20, 25],
    [['Hei', 'Hei', 'Hei'], 10, 20, 27],
    [['Nun', 'Nun', 'Shin', 'Gimel'], 10, 20, 30],
    [['Shin', 'Shin', 'Hei'], 10, 20, 19],
    [['Shin', 'Shin'], 1, 20, -1],
    [['Shin', 'Shin', 'Hei'], 1, 20, 10]
]

a = [['Nun', 'Gimel', 'Nun', 'Hei', 'Hei', 'Gimel', 'Hei',
     'Nun', 'Shin', 'Shin', 'Shin', 'Gimel', 'Shin', 'Gimel'], 32, 36, 68]


# ---------- Unit Tests ----------
class Test(unittest.TestCase):
    def testGamble(self):
      for data in testData:
          self.assertEqual(gamble(data[0], data[1], data[2]), data[3])
    
    def testGambleAgain(self):
      for data in testData:
          self.assertEqual(gambleAgain(data[0], data[1], data[2]), data[3])
    

if __name__ == '__main__':
    # ---------- Efficiency Tests ----------
    # print(
    #     f'Gamble Function: {timeit.timeit(lambda: gamble(a[0], a[1], a[2]), number=10000000)}')

    # print(
    #     f'Gamble Again Function: {timeit.timeit(lambda: gambleAgain(a[0], a[1], a[2]), number=10000000)}')
    
    # Gamble Function: 12.16119770000023
    # Gamble Again Function: 23.95148539999991

    # ---------- Function Results ----------
    for data in testData:
      result = gamble(data[0], data[1], data[2])
      print(result)

    # ---------- Run Unit Tests ----------
    unittest.main()
