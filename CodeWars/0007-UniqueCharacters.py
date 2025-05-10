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

# ---------- Final Solution ----------
def solveTwo(a, b):
    return "".join([x for x in a if x not in b] + [x for x in b if x not in a])

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
    
    # Time Results:
    # solve: 39.00026419999995
    # solve_final: 37.29786370000147

    # ---------- Results ----------
    for data in testData:
        result = solveTwo(data[0], data[1])
        print(result)

    # ---------- Run Tests ----------
    unittest.main()