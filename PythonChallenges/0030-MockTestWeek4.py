from collections import Counter

def anagram(s):
  if len(s) % 2 != 0:
    return -1
  
  s = Counter(s[:len(s)//2]) - Counter(s[len(s)//2:])

  return sum(s.values())




if __name__ == '__main__':
  s = list(map(str, "aaabbb ab abx mnop xyyx xaxbbbxx".rstrip().split()))
  for i in s:
    result = anagram(i)
    print(result)
