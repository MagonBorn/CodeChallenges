import unittest

def comes_after(st, l):
    # Use list comprehension to iterate over each letter in the sentence: range(len(st.strip())-1)
    # compare the current letter of the sentence to the comparision letter
    # If the proceeding letter is within the alphabet, add it to the return string

    return "".join([st[i+1] for i in range(len(st.strip())-1) if st[i].lower() == l.lower() and st[i+1].isalpha()])


testData = [
    ["are you really learning Ruby?", "r", "eenu"], 
    ["Pirates say arrrrrrrrr", 'r', "arrrrrrrr"], 
    ["Free coffee for all office workers!", 'f', "rfeofi"], 
    ["Every Sunday, she reads newspapers.", 's', "uhp"], 
    ["king kUnta is the sickest rap song ever kNown", 'k', "iUeN"], 
    ["p8tice makes pottery p_r p0rfect!", 'p', "o"], 
    ["d8u d._ rly 2d1s", 'D', ""], 
    ["nothing to be found here", 'z', ""], 
    ["CoDeWaRs", "d", "e"]
    ]


class Test(unittest.TestCase):
    def testEquals(self):
        for test in testData:
          self.assertEqual(comes_after(test[0], test[1]), test[2])

unittest.main()