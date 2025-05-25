import timeit
import unittest
from AdditionalResources import MichaelRoadsPreloaded

# ---------- Initial Solution ----------
def solve_roads(road):
    path = []
    found = False
    
    while not found:
        scent = road.sniff_left()
        if scent == "Michael!":
            path.append("L")
            found = True
        elif scent == "I smell Michael on the other road!":
            path.append("R")
            found = True
        elif scent == "This one reeks.":
            path.append("L")
            road.traverse_left()
        elif scent == "Pleasant air.":
            path.append("R")
            road.traverse_right()

    return "".join(path)

# ---------- Additional Solution ----------
def solve_roads_two(road):
    match road.sniff_left():
        case "Michael!":
            return "L"
        case "I smell Michael on the other road!":
            return "R"
        case "This one reeks.":
            road.traverse_left()
            return "L" + solve_roads(road)
        case _:
            road.traverse_right()
            return "R" + solve_roads(road)

#  ---------- Testing Data ----------
testData = [
    ["LRRL"],
    ["RRRRRRR"],
    ["R"],
    ["LLLRRR"],
    ["RLLRLRRL"],
    ["LLLLLLL"],
    ["L"],
    ["RLRLRLRLRLRLRLRL"]
]

# ---------- Tests ----------
class Test(unittest.TestCase):
    def test_solve_roads(self):
        for data in testData:
            road = MichaelRoadsPreloaded.Road(data[0])
            self.assertEqual(solve_roads(road), data[0])
    
    def test_solve_roads_two(self):
        for data in testData:
            road = MichaelRoadsPreloaded.Road(data[0])
            self.assertEqual(solve_roads_two(road), data[0])

if __name__ == '__main__':
  # def genRoad():
  #     return MichaelRoadsPreloaded.Road(testData[7][0])

  # print(
  #     f'Solve Roads Function: {timeit.timeit(lambda: solve_roads(genRoad()), number=1000000)}')
  
  # print(
  #     f'Solve Roads Function: {timeit.timeit(lambda: solve_roads_two(genRoad()), number=1000000)}')
  
  # Solve Roads Function: 1215.543834600001
  # Solve Roads Function Two: 1192.7895749999989

   # ---------- Results ----------
  for data in testData:
      road = MichaelRoadsPreloaded.Road(data[0])
      result = solve_roads(road)
      print(f'Found Michael via path {result}')

  # ---------- Run Tests ----------
  unittest.main()