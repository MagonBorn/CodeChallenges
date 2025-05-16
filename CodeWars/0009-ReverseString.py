import timeit
import unittest

# Loop through the string from the end using list comprehension
# Check if each letter is alpha
# Add to list and return the joined string

# ---------- Initial Solution ----------
def reverse_letter(st):
    return ''.join([st[i] for i in range(len(st) - 1, -1, -1) if st[i].isalpha()])

# ---------- Additional Solution ----------
def reverse_letter_two(s):
    return ''.join([i for i in s if i.isalpha()])[::-1]

# ---------- Additional Solution ----------
def reverse_letter_three(string):
    return ''.join(filter(str.isalpha, reversed(string)))

# ---------- Additional Solution ----------
def reverse_letter_four(string):
    return ''.join(c for c in string[::-1] if c.isalpha())

# ---------- Final Solution ----------
def reverse_letter_five(s):
    tab = str.maketrans("", "", r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789""")
    return s.translate(tab)[::-1]

# ---------- Tests ----------
class Test(unittest.TestCase):
    def testEqualsReverseLetter(self):
        for data in testData:
            self.assertEqual(reverse_letter(data[0]), data[1])

    def testEqualsReverseLetterTwo(self):
        for data in testData:
            self.assertEqual(reverse_letter_two(data[0]), data[1])

    def testEqualsReverseLetterThree(self):
        for data in testData:
            self.assertEqual(reverse_letter_three(data[0]), data[1])

    def testEqualsReverseLetterFour(self):
        for data in testData:
            self.assertEqual(reverse_letter_four(data[0]), data[1])

    def testEqualsReverseLetterFive(self):
        for data in testData:
            self.assertEqual(reverse_letter_five(data[0]), data[1])


#  ---------- Testing Data ----------
testData = [
    ["krishan", "nahsirk"],
    ["ultr53o?n", "nortlu"],
    ["ab23c", "cba"],
    ["krish21an", "nahsirk"]
]

# ---------- Main Program ----------
if __name__ == '__main__':
    
    # ---------- Timing Tests ----------
    # a = "lCYBYSiXzTWoRNXbHJYFfLWfLhuYnbbiwonEziLuBLvILsJHrxEDjZfwlwngPpIRNGkdmrIPfsACDAlnsEBexeSkJuNigsdtMsSgmOYZfDSVttKHaniauNjdRwcmarNNjcUCLgOUbHLVtjPurdyiTWvpoZlVgwDoHKORDtAMjPUyGQZIpPbhhwwOwulVZrhOcpkyjafwEkOTNZIoClaaWSUphhJucQzmEafhoKSbMlZGQcvFWQqpTzxjtWAzlFBymHfPvITTPCXIXJnfFVqgGphffEWYrWRPUkFvDqkGSHhUYDRfxtHDIhpwoyXNaLMblFBvChxLLRQfdshEKSAXFgPadAWQZINfcQWCTYCTTKgDeWiBeUuRjcWXQnaVbGyRwcOcTtimnXfIghuhTMnZOCPpwoFrUDJYcdtQcvOliQyqpJvkFwNLffzxQePzITMPRogOaynudcCkeXsoMLxCYupPPBmHNYyhGKAkUIOwBVegnbPdjlJleZCJQiuwRinodJfFyyqVDttimNmPOElsMPuPBXIkMACTLpUgGHRoPqGPYFgnZXECWlpvawCCjoDKJHHVoqZOXPtf"

    # print(
    #     f'Reverse Letter Function: {timeit.timeit(lambda: reverse_letter(a), number=1000000)}')
    # print(
    #     f'Reverse Letter Two Function: {timeit.timeit(lambda: reverse_letter_two(a), number=1000000)}')
    # print(
    #     f'Reverse Letter Three Function: {timeit.timeit(lambda: reverse_letter_three(a), number=1000000)}')
    # print(
    #     f'Reverse Letter Four Function: {timeit.timeit(lambda: reverse_letter_four(a), number=1000000)}')
    # print(
    #     f'Reverse Letter Five Function: {timeit.timeit(lambda: reverse_letter_five(a), number=1000000)}')
    
# Reverse Letter: 50.69786440000007
# Reverse Letter Two: 27.547644799999944
# Reverse Letter Three: 20.118738899999926
# Reverse Letter Four: 42.117678799999794
# Reverse Letter Five: 7.909158699999807

    # ---------- Results ----------
    for data in testData:
        result = reverse_letter_five(data[0])
        print(result)

    # ---------- Run Tests ----------
    unittest.main()