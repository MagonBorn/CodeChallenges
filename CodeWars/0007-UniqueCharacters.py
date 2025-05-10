import timeit
import unittest
import random
import string

# Loop through each character of the first array
# compare with each letter of the second array
# If the letter is not present, add it to a results array
# Join the letter in the results array and return

# ---------- Initial Solution ----------
def solve(a, b):
    temp = []

    for i in a:
        if i not in b:
            temp.append(i)
    for i in b:
        if i not in a:
            temp.append(i)
    return "".join(temp)

# ---------- Additional Solution ----------
def solveTwo(a, b):
    return "".join([x for x in a if x not in b] + [x for x in b if x not in a])

# ---------- Final Solution ----------
def solveThree(a, b):
    s = set(a) & set(b)
    return ''.join(c for c in a+b if c not in s)

# ---------- Tests ----------
class Test(unittest.TestCase):
    def testEquals(self):
        for data in testData:
            self.assertEqual(solveTwo(data[0], data[1]), data[2])

#  ---------- Testing Data ----------
testData = [
    ["xyab", "xzca", "ybzc"],
    ["xyabb", "xzca", "ybbzc"],
    ["abcd", "xyz", "abcdxyz"],
    ["xxx", "xzca", "zca"]
]

if __name__ == '__main__':   
    a = "lCYBYSiXzTWoRNXbHJYFfLWfLhuYnbbiwonEziLuBLvILsJHrxEDjZfwlwngPpIRNGkdmrIPfsACDAlnsEBexeSkJuNigsdtMsSgmOYZfDSVttKHaniauNjdRwcmarNNjcUCLgOUbHLVtjPurdyiTWvpoZlVgwDoHKORDtAMjPUyGQZIpPbhhwwOwulVZrhOcpkyjafwEkOTNZIoClaaWSUphhJucQzmEafhoKSbMlZGQcvFWQqpTzxjtWAzlFBymHfPvITTPCXIXJnfFVqgGphffEWYrWRPUkFvDqkGSHhUYDRfxtHDIhpwoyXNaLMblFBvChxLLRQfdshEKSAXFgPadAWQZINfcQWCTYCTTKgDeWiBeUuRjcWXQnaVbGyRwcOcTtimnXfIghuhTMnZOCPpwoFrUDJYcdtQcvOliQyqpJvkFwNLffzxQePzITMPRogOaynudcCkeXsoMLxCYupPPBmHNYyhGKAkUIOwBVegnbPdjlJleZCJQiuwRinodJfFyyqVDttimNmPOElsMPuPBXIkMACTLpUgGHRoPqGPYFgnZXECWlpvawCCjoDKJHHVoqZOXPtf"

    b = "TznfaAMTvmnVjDpdmEHdNbjemIszUhyJLWfsCDAlOPydSGTgdPflYfEPCLYHcRHokAjAydkzFffaWFYZqKHudCRgFskqMnpWOOdoaAXYLlWfzrSmOhpkBVJJtJadudqRFNVdhfiIdhpWcCNkEuDqnQFFlStyvpHVPKpIIqTAfFTrehJUIVoyEzTcCGqNYoDqwsLfEPYpSoIcPtPYfhbwbcgQdOgfLdPCDqYOSlgMHfPjDeAKcMiOXhlosUKTjXYNdVvKVxUbhbcuvCgDfjwxZpMmLtbVIXIMIcrVjmxTFBiJqYoGpGbVxgPTvSIlomHAhwGKvEmMrlwtNcEAimTgrhmoptafxyvVYGMUjmhbajPqByJQkiDJpGBFMFBSEiSVHZNmzitZnmJTBnMBeYAxpZqykpddDhGbcaUoXcPalcYP"
    
    print(
        f'Solve Function: {timeit.timeit(lambda: solve(a, b), number=1000000)}')
    print(
        f'Solve Final Function: {timeit.timeit(lambda: solveTwo(a, b), number=1000000)}')
    print(
        f'Solve Final Function: {timeit.timeit(lambda: solveThree(a, b), number=1000000)}')
    
    # Time Results:
    # solve: 46.26528759999928
    # solveTwo: 38.90934170000037
    # solveThree: 36.971023800000694

    # ---------- Results ----------
    for data in testData:
        result = solveTwo(data[0], data[1])
        print(result)

    # ---------- Run Tests ----------
    unittest.main()