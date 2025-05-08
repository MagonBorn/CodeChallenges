def mul_by_n(lst, n):
    print("Inputs: ", lst, n)  # Check our inputs
    result = [x * n for x in lst]
    print("Result: ", result)  # Check our result
    return result

# Multiple ways to fix this:
# 1: change "result = (x * n for x in lst)" to result = tuple(x * n for x in lst)
# If the key word "tuple" is not placed before the expression, a generator object is produced.

# 2. Remove line 4: generator objects are consumed upon use meaning the return statement procudes an emply list

# 3. change line 3 to list comprhension, and remove all occurances of casting generator object to list


tests = [([1, 2, 3], 4), ([9, 1], 9), ([5, 5, 5, 5, 5], 1), ([5, 5, 5, 5, 5], 2), ([77, 88], 0)]

for test in tests:
    print(f'Debugged Results: {mul_by_n(test[0], test[1])}')