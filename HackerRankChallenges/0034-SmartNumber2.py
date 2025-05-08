import math

test = [1, 2, 7, 169]

def is_smart_number(num):
    val = int(math.sqrt(num))
    if val * val == num:
        return True
    return False


for x in range(len(test)):
    ans = is_smart_number(test[x])
    if ans:
        print("YES")
    else:
        print("NO")
