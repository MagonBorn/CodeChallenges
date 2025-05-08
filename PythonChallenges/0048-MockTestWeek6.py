# Figure out the character to be removed that makes the string a pallindrome
# Return the index of the character to remove or -1 if there is no solution

def pallindrome(s):

  n = len(s)
  for i in range(n // 2 + 1):
      if s[i] != s[n-1-i]:
          if s[i] == s[n-2-i] and s[i+1] == s[n-3-i]:
              return n-1-i
          else:
              return i

  return -1

data = ["aaab", "baa", "aaa", "quyjjdcgsvvsgcdjjyq", 
"hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh",
"fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf",
"bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb",
"fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf",
"mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm",
"tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt",
"lhrxvssvxrhl",
"prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp",
"kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk"]

for i in data:
  result = pallindrome(i)
  print(result)