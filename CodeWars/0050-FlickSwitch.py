def flick_switch(lst):
    flick = True
    result = []
    for word in lst:
        if word == "flick":
            flick = not flick
        result.append(flick)
    return result

tests = [['codewars', 'flick', 'code', 'wars'], [
    'flick', 'chocolate', 'adventure', 'sunshine'], ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'], ['john, smith, susan', 'flick'], ['flick', 'flick', 'flick', 'flick', 'flick']]

for test in tests:
    print(flick_switch(test))

# Expected Results
# [True, False, False, False]
# [False, False, False, False]
# [True, True, False, False, True]
# [True, False]
# [False, True, False, True, False]
