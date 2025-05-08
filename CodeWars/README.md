# CodeWars Challenges

[XCOM-409](#xcom-409)\
[FlickSwitch](#flick-switch)\
[Vanaishing Values](#vanishing-values)

## [XCOM-409](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0049-XCOM-409.py)

You are an intern working in the software development department of the X-COM agency, responsible for fighting off a large-scale invasion of extraterrestrials. Your task for today is described with the bug report below:

### [BUG] XCOM-409: Flight distance of Interceptor planes is miscalculated

**Type**: Bug\
**Priority**: Major\
**Component**: Operational Logistics Software\
**Reporter**: maverick\
**Assignee**: Assigned to you

### Bug Description

Pilots have reported discrepancies in their flight logs after returning from interception missions. The travel distance logged in the logistics software does not match actual flight paths, potentially leading to incorrect fuel calculations and errors in planning of future missions.

### Steps to Reproduce
1. Deploy an interceptor to engage a UFO.

2. Upon its return, note the average speed (given in knots) and travel time (in minutes) reported by onboard instruments.

3. Enter the values into the Logistics and Planning System.

4. Expected result: The system should correctly compute the distance in kilometers.

5. Actual result: The logged distance appears inaccurate.

### Impact

If not fixed, this could cause interceptors to run out of fuel mid-mission, leaving Earth vulnerable to alien attacks. On the other hand, if the system overestimates travel distance, interceptors may be overfueled, making them heavier than necessary. This reduces maneuverability, increases takeoff time, and could put pilots at a disadvantage during high-speed engagements with alien craft.

The Flight Operations team has requested an immediate fix.

### Task
Investigate and fix the bug in the travel distance calculation function

<!-- ------------------------------------------------------------ -->

## [Flick Switch](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0050-FlickSwitch.py)

### Task

Create a function that always returns True/true for every item in a given list.
However, if an element is the word **'flick'**, switch to always returning the opposite boolean value.

### Examples

    ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

    ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

    ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]

### Notes

- "flick" will always be given in lowercase.
- A list may contain multiple flicks.
- Switch the boolean value on the same element as the flick itself.

<!-- ------------------------------------------------------------ -->

## [Vanishing Values](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0051-VanashingValues.py)

### Description

Confusion, perplexity, a mild headache. These are just a sample of the things you have experienced in the last few minutes while trying to figure out what is going on in your code.

The task is very simple: accept a list of values, and another value n, then return a new list with every value multiplied by n. For example, [1, 2, 3] and 4 should result in [4, 8, 12].

While writing the function, you even added some debugging lines to make sure that you didn't mess anything up, and everything looked good! But for some reason when you run the function it always seems to return an empty list, even though you can clearly see, that the list ***should*** have the right values in it! Somehow, the values are simply disappearing! Is this a bug in the programming language itself...?

<!-- ------------------------------------------------------------ -->