import timeit
import unittest

# ---------- Initial Solution ----------
def shiftLeft(a, b):
    count = 0
    while a != b:
        bigWord = max(a, b, key=len)
        if bigWord == a:
            a = a.replace(a[0], "", 1)
            count += 1
        else:
            b = b.replace(b[0], "", 1)
            count += 1
    return count

# ---------- Additional Solution ----------
# combine the lengths of a and b and subtract any changes between them starting from the end of the smaller of the two.
def shiftLeftTwo(a, b):
    r = len(a) + len(b)
    for i in range(1, len(min(a, b, key=len)) + 1):
        if a[-i] != b[-i]:
            break
        r -= 2
    return r

# ---------- Additional Solution ----------
def shiftLeftThree(a, b):
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 and j >= 0 and a[i] == b[j]:
        i -= 1
        j -= 1

    return (i + 1) + (j + 1)

# ---------- Tests ----------
class Test(unittest.TestCase):
    def testShiftLeft(self):
        for data in testData:
            self.assertEqual(shiftLeft(data[0], data[1]), data[2])

    def testShiftLeftTwo(self):
        for data in testData:
            self.assertEqual(shiftLeftTwo(data[0], data[1]), data[2])
    
    def testShiftLeftThree(self):
        for data in testData:
            self.assertEqual(shiftLeftThree(data[0], data[1]), data[2])

#  ---------- Testing Data ----------
testData = [
    ["test", "west", 2],
    ["test", "yes", 7],
    ["b", "ab", 1],
    ["abacabadabacaba", "abacabadacaba", 18],
    ["aaabc", "bc", 3],
    ["dark", "d", 5],
    ["dadc", "dddc", 4],
    ["nogkvcdldfpvlbkpedsecl", "nogkvcdldfpvlbkpedsecl", 0],
    ["", "a", 1]
]

# ---------- Main Program ----------
if __name__ == '__main__':
    
    # a = "lCYBYSiXzTWoRNXbHJYFfLWfLhuYnbbiwonEziLuBLvILsJHrxEDjZfwlwngPpIRNGkdmrIPfsACDAlnsEBexeSkJuNigsdtMsSgmOYZfDSVttKHaniauNjdRwcmarNNjcUCLgOUbHLVtjPurdyiTWvpoZlVgwDoHKORDtAMjPUyGQZIpPbhhwwOwulVZrhOcpkyjafwEkOTNZIoClaaWSUphhJucQzmEafhoKSbMlZGQcvFWQqpTzxjtWAzlFBymHfPvITTPCXIXJnfFVqgGphffEWYrWRPUkFvDqkGSHhUYDRfxtHDIhpwoyXNaLMblFBvChxLLRQfdshEKSAXFgPadAWQZINfcQWCTYCTTKgDeWiBeUuRjcWXQnaVbGyRwcOcTtimnXfIghuhTMnZOCPpwoFrUDJYcdtQcvOliQyqpJvkFwNLffzxQePzITMPRogOaynudcCkeXsoMLxCYupPPBmHNYyhGKAkUIOwBVegnbPdjlJleZCJQiuwRinodJfFyyqVDttimNmPOElsMPuPBXIkMACTLpUgGHRoPqGPYFgnZXECWlpvawCCjoDKJHHVoqZOXPtf"

    # b = "TznfaAMTvmnVjDpdmEHdNbjemIszUhyJLWfsCDAlOPydSGTgdPflYfEPCLYHcRHokAjAydkzFffaWFYZqKHudCRgFskqMnpWOOdoaAXYLlWfzrSmOhpkBVJJtJadudqRFNVdhfiIdhpWcCNkEuDqnQFFlStyvpHVPKpIIqTAfFTrehJUIVoyEzTcCGqNYoDqwsLfEPYpSoIcPtPYfhbwbcgQdOgfLdPCDqYOSlgMHfPjDeAKcMiOXhlosUKTjXYNdVvKVxUbhbcuvCgDfjwxZpMmLtbVIXIMIcrVjmxTFBiJqYoGpGbVxgPTvSIlomHAhwGKvEmMrlwtNcEAimTgrhmoptafxyvVYGMUjmhbajPqByJQkiDJpGBFMFBSEiSVHZNmzitZnmJTBnMBeYAxpZqykpddDhGbcaUoXcPalcYP"

    # print(
    #     f'Reverse Letter Function: {timeit.timeit(lambda: shiftLeft(a, b), number=1000000)}')
    # print(
    #     f'Reverse Letter Two Function: {timeit.timeit(lambda: shiftLeftTwo(a, b), number=1000000)}')
    # print(
    #     f'Reverse Letter Three Function: {timeit.timeit(lambda: shiftLeftThree(a, b), number=1000000)}')
    
    # Reverse Letter Function: 434.82384980000006
    # Reverse Letter Two Function: 0.5405253999997512
    # Reverse Letter Three Function: 0.31077019999975164
    
    # ---------- Results ----------
    for data in testData:
        result = shiftLeft(data[0], data[1])
        print(result)

    # ---------- Run Tests ----------
    unittest.main()
