import timeit
import unittest

# The range of Unicode for Cyrillic letters begins at 1024 and ends at 1279
# Simply compare the unicode of the letter and make sure it falls within the
# specific range.

# ---------- Initial Solution ----------
def is_cyrillic(letter):
    return True if 1024 <= ord(letter) <= 1279 else False

# ---------- Tests ----------
class Test(unittest.TestCase):
    def testEqualsCyrillicLetter(self):
        for data in testData:
            self.assertEqual(is_cyrillic(data[0]), data[1])

#  ---------- Testing Data ----------
testData = [
    ["Д", True],
    ["D", False],
    ["а", True],
    ["a", False]
]

# ---------- Main Program ----------
if __name__ == '__main__':
    # ---------- Timing Tests ----------
    # a = [chr(x) for x in range(1024, 1280)]

    # def is_cyrillic_test(letters):
    #     for letter in letters:
    #         True if 1024 <= ord(letter) <= 1279 else False
    #     return "Test Finished"
        
    # print(f'Is_Cyrillic Function: {timeit.timeit(lambda: is_cyrillic_test(a), number=1000000)}')

    # Is_Cyrillic: 17.910790899999938

    # ---------- Results ----------
    for data in testData:
        result = is_cyrillic(data[0])
        print(result)
    
    # ---------- Run Tests ----------
    unittest.main()
