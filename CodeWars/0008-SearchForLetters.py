import timeit
import unittest
import string

# Initialise an array of length 26
# Loop through each character in the string
# Calculate the index of the character in the alphabet and compare its value to all ascii letters
# append 1 at alphatbet index otherwise 0

# ---------- Initial Solution ----------
def change(st):
    result = ["0"] * 26
    for letter in st:
        idx = ord(letter.lower()) - 97
        char = ord(letter.lower())
        if char > 96 and char < 123:
            result[idx] = "1"
    return "".join(result)

# ---------- Additional Solution ----------
def changeTwo(st):
    result = ["0"] * 26
    for letter in st:
        if letter.lower() in string.ascii_lowercase:
            result[ord(letter.lower()) - 97] = "1"
    return "".join(result)

# ---------- Final Solution ----------
def changeThree(st):
    s = set(st.lower())
    return "".join("1" if x in s else "0" for x in map(chr, range(97, 123)))

# ---------- Tests ----------
class Test(unittest.TestCase):
    def testEquals(self):
        for data in testData:
            self.assertEqual(changeThree(data[0]), data[1])


#  ---------- Testing Data ----------
testData = [
    ["a **&  bZ", "11000000000000000000000001"],
    ['Abc e  $$  z', "11101000000000000000000001"],
    ["!!a$%&RgTT", "10000010000000000101000000"],
    ["", "00000000000000000000000000"],
    ["abcdefghijklmnopqrstuvwxyz", "11111111111111111111111111"],
    ["aaaaaaaaaaa", "10000000000000000000000000"],
    ["&%&%/$%$%$%$%GYtf67fg34678hgfdyd", "00010111000000000001000010"]
]

if __name__ == '__main__':
    # a = "lCYBYSiXzTWoRNXbHJYFfLWfLhuYnbbiwonEziLuBLvILsJHrxEDjZfwlwngPpIRNGkdmrIPfsACDAlnsEBexeSkJuNigsdtMsSgmOYZfDSVttKHaniauNjdRwcmarNNjcUCLgOUbHLVtjPurdyiTWvpoZlVgwDoHKORDtAMjPUyGQZIpPbhhwwOwulVZrhOcpkyjafwEkOTNZIoClaaWSUphhJucQzmEafhoKSbMlZGQcvFWQqpTzxjtWAzlFBymHfPvITTPCXIXJnfFVqgGphffEWYrWRPUkFvDqkGSHhUYDRfxtHDIhpwoyXNaLMblFBvChxLLRQfdshEKSAXFgPadAWQZINfcQWCTYCTTKgDeWiBeUuRjcWXQnaVbGyRwcOcTtimnXfIghuhTMnZOCPpwoFrUDJYcdtQcvOliQyqpJvkFwNLffzxQePzITMPRogOaynudcCkeXsoMLxCYupPPBmHNYyhGKAkUIOwBVegnbPdjlJleZCJQiuwRinodJfFyyqVDttimNmPOElsMPuPBXIkMACTLpUgGHRoPqGPYFgnZXECWlpvawCCjoDKJHHVoqZOXPtf"
    
    # print(
    #     f'Solve Function: {timeit.timeit(lambda: change(a), number=1000000)}')
    # print(
    #     f'Solve Final Function: {timeit.timeit(lambda: changeTwo(a), number=1000000)}')
    # print(
    #     f'Solve Final Function: {timeit.timeit(lambda: changeThree(a), number=1000000)}')

    # change: 116.89458419999937
    # changeTwo: 93.02122270000109
    # changeThree: 7.54257090000101

    # ---------- Results ----------
    for data in testData:
        result = changeThree(data[0])
        print(result)

    # ---------- Run Tests ----------
    unittest.main()