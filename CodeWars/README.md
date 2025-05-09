# CodeWars Challenges

[XCOM-409](#xcom-409)\
[FlickSwitch](#flick-switch)\
[Vanaishing Values](#vanishing-values)\
[Planet Mnemonics](#planet-mnemonics)

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

## [Planet Mnemonics]()

Oh no! The planets are jumbled up again!

### ABOUT

Did you know that there is a mnemonic to remember the planets in there order in our Solar System.

The mnemonic is the sentence "My Very Efficient Mother Just Served Us Nuts", where the M of "My" stands for Mercury, V of "Very" for Venus, E of "Efficient" for Earth and so on.

### TASK

Now that the planets are all jumbled up, some people have decided to come up with a new mnemonic, and your task is to confirm whether the mnemonic they have made fits the new Solar System using a program.

So, given the Solar System in the form of a list, you have to return a boolean value that is either True if the mnemonic is correct or False if it is not.

However, an Asteroid has to be ignored as it should not be part of the mnemonic.

Pluto will never be part of the Solar System.

### EXAMPLES

    ["Earth", "Jupiter", "Asteroid", "Asteroid", "Mercury", "Asteroid", "Saturn"], "Even Jaguars Make Spaghetti" -> True

    # E of "Even" stands for Earth
    # J of "Jaguars" stands for Jupiter
    # Asteroid is ignored
    # Another Asteroid is ignored
    # M of "Make" stands for Mercury
    # Asteroid is ignored again
    # Finally, S of "Spaghetti" stands for Saturn
    # As the whole mnemonic fits the given Solar System, you have to just return True

    ["Asteroid", "Mars", "Uranus", "Asteroid"], "Water Melon" -> False

### NOTES

- All the planet names will be Title Case and so will be the mnemonic
- There will never be more than one of anything except Asteroids
- If the Solar System is empty or it contains only Asteroids, then empty string mnemonic, "", is valid. However, "Hello" is not valid.
- The Solar System will never contain anything outside ["Asteroid", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
- Pluto will never be part of the Solar System

<!-- ------------------------------------------------------------ -->

