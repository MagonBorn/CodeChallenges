import timeit
import unittest
import string

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

# ---------- Tests ----------
class Test(unittest.TestCase):
    def testEquals(self):
        for data in testData:
            self.assertEqual(reverse_letter_three(data[0]), data[1])


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
    
    # reverse_letter: 42.668504700000085
    # reverse_letter_two: 23.631478100000095
    # reverse_letter_three: 19.41206710000006
    # reverse_letter_four: 36.83084409999992

    # ---------- Results ----------
    for data in testData:
        result = reverse_letter_three(data[0])
        print(result)

    # ---------- Run Tests ----------
    unittest.main()