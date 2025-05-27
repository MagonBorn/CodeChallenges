# CodeWars Challenges

[XCOM-409](#xcom-409)\
[FlickSwitch](#flick-switch)\
[Vanaishing Values](#vanishing-values)\
[Planet Mnemonics](#planet-mnemonics)\
[What Comes After](#what-comes-after)\
[Mary's Puzzle Book](#marys-puzzle-book)\
[Unique String Characters](#unique-string-characters)\
[Search For Letters](#search-for-letters)\
[Reverse String](#reverse-string)\
[Cyrillic Letters](#cyrillic-letters)\
[Shift Left](#shift-left)\
[Chemical Elements Regex](#chemical-elements-regex)\
[Arrays of the Right Depth](#arrays-of-the-right-depth)\
[Horse Stamina](#horse-stamina)\
[Chess 960 Positions](#chess-960-positions)\
[Michael Roads](#michael-roads)\
[Unicode Steganography](#unicode-steganography)

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

## [Planet Mnemonics](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0004-PlanetMnemonics.py)

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

## [What Comes After?](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0005-WhatComesAfter.py)

You will be given two inputs: a string of words and a letter. For each string, return the alphabetic character after every instance of letter(case insensitive).

If there is a number, punctuation or underscore following the letter, it should not be returned.

    If letter = 'r':
    "are you really learning Ruby?" # => "eenu"
    "Katy Perry is on the radio!"   # => "rya"
    "Pirates say arrrrrrrrr."       # => "arrrrrrrr"
    "r8 your friend"                # => "i"

Return an empty string if there are no instances of letter in the given string.

<!-- ------------------------------------------------------------ -->

## [Mary's Puzzle Book](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0006-MarysPuzzleBook.py)

### Zero Terminated Sum

Mary has another puzzle book, and it's up to you to help her out! This book is filled with zero-terminated substrings, and you have to find the substring with the largest sum of its digits. For example, one puzzle looks like this:

    "72102450111111090"

Here, there are 4 different substrings: 721, 245, 111111, and 9. The sums of their digits are 10, 11, 6, and 9 respectively. Therefore, the substring with the largest sum of its digits is 245, and its sum is 11.

Write a function largest_sum which takes a string and returns the maximum of the sums of the substrings. In the example above, your function should return 11.

**Notes:**
- A substring can have length 0. For example, 123004560 has three substrings, and the middle one has length 0.
- All inputs will be valid strings of digits, and the last digit will always be 0.

<!-- ------------------------------------------------------------ -->

## [Unique String Characters](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0007-UniqueCharacters.py)

In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.

For example:

    solve("xyab","xzca") = "ybzc" 
    --The first string has 'yb' which is not in the second string. 
    --The second string has 'zc' which is not in the first string.

Notice also that you return the characters from the first string concatenated with those from the second string.

More examples in the tests cases.

Good luck!

<!-- ------------------------------------------------------------ -->

## [Search For Letters](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0008-SearchForLetters.py)

Create a function which accepts one arbitrary string as an argument, and return a string of length 26.

The objective is to set each of the 26 characters of the output string to either '1' or '0' based on the fact whether the Nth letter of the alphabet is present in the input (independent of its case).

So if an 'a' or an 'A' appears anywhere in the input string (any number of times), set the first character of the output string to '1', otherwise to '0'. if 'b' or 'B' appears in the string, set the second character to '1', and so on for the rest of the alphabet.

### For instance:

### Sample Output 1
    "a   **&  cZ"  =>  "10100000000000000000000001"

### Sample Output 2
    "aaaaaaa79345675"  =>  "10000000000000000000000000"

### Sample Output 3
    "&%#*"  =>  "00000000000000000000000000"

<!-- ------------------------------------------------------------ -->

## [Reverse String](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0009-ReverseString.py)

### Task

Given a string str, reverse it and omit all non-alphabetic characters.

### Example

For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

### Input/Output

- [input] string str

A string consists of lowercase latin letters, digits and symbols.

- [output] a string

<!-- ------------------------------------------------------------ -->

## [Cyrillic Letters](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0010-CyrillicLetters.py)

Cyrillic letters, used in languages like Russian and Ukrainian, have different unicode values than Latin letters. 2 of those cyrillic letters include а and у which, if you copy these 2, are not the same as the latin a and y

### Task

Your task is to write a function that returns whether a given string (or char) is a Cyrillic letter in the Cyrillic Unicode Block.

The string (or char) will always be a single letter.

### Hint

Here is a link to [Wikipidia's list of the Cyrillic Unicode block](https://en.wikipedia.org/wiki/Cyrillic_(Unicode_block)) for reference

### Examples

### Example 1

    Input: "D"
    Output: false (or False in Python or your language's equivalent)

### Example 2

    Input: "Я"
    Output: true (or True in Python or your language's equivalent)

<!-- ------------------------------------------------------------ -->

## [Shift Left](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0011-ShiftLeft.py)

You are given two strings. In a single move, you can choose any of them, and delete the first (i.e. leftmost) character.

### For Example:

- By applying a move to the string "where", the result is the string "here".
- By applying a move to the string "a", the result is an empty string "".

Implement a function that calculates the minimum number of moves that should be performed to make the given strings equal.

### Notes

- Both strings consist of lowercase latin letters.
- If the string is already empty, you cannot perform any more delete operations.

<!-- ------------------------------------------------------------ -->

## [Chemical Elements Regex](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0012-ChemicalElementsRegEx.py)

Create a regex to match the symbols of all 118 chemical elements.

Your regex pattern can be maximum 210 characters long.

<!-- ------------------------------------------------------------ -->

## [Arrays of the Right Depth](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0013-ArrayDepths.py)

### Arrays of the Right Depth

You are given a main array (a list of lists) and a dictionary of depth constraints. Each subarray in the main array can either be empty ([]) or contain only one nested array—nothing else.

### Task:

Your goal is to verify whether all arrays inside the main array adhere to the given depth constraints.

### Understanding Depth

The depth is zero-based:

- The elements in the main array have depth 1.
- A single nested empty array ([[]]) has depth 2.
- A double-nested empty array ([[[]]]) has depth 3, and so on.
- The depth constraints do not apply to the main array itself, only to the subarrays inside it.

### Constraints Dictionary

- The dictionary keys represent valid depths.
- The corresponding values indicate the maximum number of arrays at that depth that can appear in the main array.
- If the dictionary is empty, then there are no valid depths (meaning the result should be False).
- If an array has a depth not listed in the dictionary, return False.
- If there are more arrays of a certain depth than allowed, return False.
- If all constraints are met, return True.

### Examples:

[[[]]], {2:1} -> True

#### Explanation:

The only element in the main array ([ [[]] ]) is an array with a single empty array inside it. This means it has depth 2, which is allowed once ({2:1}).

[[[]], [[]]], {2:1} -> False

#### Explanation: 

There are two arrays with depth 2, but only 1 is allowed.

[ [[]], [], [[[]]], [], [[]] ], {2:6,1:2,3:1} -> True

#### Explanation:

- Depth 1: There are two empty arrays ([]), and {1:2} allows them.
- Depth 2: There are three [[]], and {2:6} allows up to 6.
- Depth 3: There is one [[[]]], and {3:1} allows 1.
- No other depths appear, and all constraints are satisfied.

[ [[]], [], [[[]]], [], [[]] ], {2:1,1:2,3:1}  -> False

[ [[]], [], [[[]]], [], [[]] ], {2:6,1:2} -> False

[ [[]], [], [[[]]], [], [[]] ], {} -> False

[ [[]], [] ], {2:6,1:2,3:1,10:8,5:1,6:4} -> True

[ [] ], {1:1} -> True

[ [] ], {} -> False

<!-- ------------------------------------------------------------ -->

## [Horse Stamina](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0014-HorseStamina.py)

### Will My Horse Make It to the End?

You are a professional horse rider and you are about to have a ride on a horse over the line of obstacles. You have a very experienced eye and you can instantly give a rough estimate of the hourse stamina. Moreover, you learned how much stamina it would take for a hourse to jump over a certain obstacle. The only problem now is to understand immediately if the given horse will actually overcome all of the obstacles before it runs out of energy! Your task is to help the horse rider to find it out.

### Task:

Given the horse’s stamina and a map representing the course, determine if the horse can reach the end without running out of energy.

Return True if the horse completes the course with stamina ≥ 0, otherwise return False.

### Input:

- stamina (integer) – the horse’s starting stamina.

- map (array of 0s and 1s) – represents the track:

- 0 – flat ground (no stamina loss).

- 1 – obstacle (requires stamina to jump).

### Stamina Cost per Obstacle:

- A single 1 (length 1) costs 2 stamina.

- A pair of consecutive 1s (length 2) costs 5 stamina.

- A triplet of consecutive 1s (length 3) costs 10 stamina.

### Examples:

[0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0], 18 -> False

[1, 1], 5 -> True

[0, 1, 0, 0, 0, 0, 1], 3 -> False

<!-- ------------------------------------------------------------ -->

## [NaughtyNumber]()

There is a naughty number hidden somewhere in the list. Find the index of it, if you are strong enough, of course!

### Input:

- You will receive an array of arrays (a list of lists).
- Each sub-array can only contain either another array or a single number.
- There will always be at least one sub-array in the input.
- There will be only one number hidden in the sub-arrays

### Output:

Return the index of the first-level sub-array that contains the hidden number.

### Examples:

[ [[[]]] , [[]], [], [], [[2]] ] -> index is 4

[ [1] ] -> index is 0

[ [], [8], [] , [] ] -> index is 1

<!-- ------------------------------------------------------------ -->

## [Chess 960 Positions](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0016-Chess960.py)

### Background:

Freestyle chess, also known as Chess960, is a variant of chess where the starting positions of the pieces are randomized. Magnus Carlsen recently (April 2025) won €60,000 with a 9/9 performance in a freestyle chess tournament.

As in standard chess, in the starting position the 2nd and 7th rank contain pawns and the remaining white/black pieces are on the 1st/8th rank. What changes is that the pieces on the first rank can be placed anywhere, as long as the two bishops are on different colored squares and the king is placed between the two rooks. The configuration of the 8th rank matches the 1st rank, so that white and black start in the same position.

There are a total of 960 possible starting positions, hence the name. If these positions are sorted lexicographically, we can associate each integer from 1 to 960 with a specific Chess960 starting position.

### Task:

Given a positive integer ibetween 1 and 960, return a string representing the board in the i'thChess960 starting position. The pieces are denoted using queen -> Q, rook -> R, king -> K, knight -> N, bishop -> B and pawn -> P, with lowercase letters representing black and uppercase white. '.' is used for empty squares.

### Examples:

The following examples show how the strings should display when printed.

1 => ## lexicographically first

b b n n q r k r\
p p p p p p p p\
. . . . . . . .\
. . . . . . . .\
. . . . . . . .\
. . . . . . . .\
P P P P P P P P\
B B N N Q R K R\

960 => ## lexicographically last

r q n n k r b b\
p p p p p p p p\
. . . . . . . .\
. . . . . . . .\
. . . . . . . .\
. . . . . . . .\
P P P P P P P P\
R Q N N K R B B

<!-- ------------------------------------------------------------ -->

## [Michael Roads](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0017-MichaelRoads.py)

"I merely walk the humble Michael Street."

### Background

Well, you lost Michael.

You last saw him walking ahead of you on an infinitely forking road. Luckily, you don't need to think very hard about which road to take, for each fork leads only to two new roads, never more, never less. The issue is that it's much too foggy to see, and you can't tell whether a silhouette on the path is Michael or some other such terrible monster. Luckily, Michael lets off a very distinct, ghastly onion smell at all times, allowing you to use only your sense of smell to find him.

### Task

You must traverse the given road to find Michael. Return a String representing the turns you took on the road before finding Michael. Right turns are denoted by the character 'R' and left turns by 'L'.

    -> "RRRRLLLRLRL" // took the right path 4 times, then the left 3 times, then the right, left, right, left
    -> "LLLLLLLLLLL" // just turned left like it's Nascar

### The Road

The only argument passed to your code is a singular object, the Road. You can gather information about either of the next roads by using .sniffLeft() and .sniffRight() to retrieve the smells of the left and right roads respectively. Note that while you are on a road, you cannot access its scent, so you should gather scents before continuing down a path. Also, you can only sniff once per fork. After using a sniffing method, you cannot use another without an OverusedSnifferException being thrown. Of course, you can use your nose again once you move down one of the roads.

To go down a road, you must use its .traverseLeft() or .traverseRight() methods. This will change the road object to either its left or right subroad respectively.

The number of roads between you and Michael is at least 1 road.

Below is all that you need to know about the Road structure.

class Road:
    # L: Road     (private)
    # R: Road     (private)
    # scent: str  (private)

    sniff_left: Callable[[], str]       # returns scent of Road L
    sniff_right: Callable[[], str]      # returns scent of Road R
    
    traverse_left: Callable[[], None]   # changes this Road to Road L
    traverse_right: Callable[[], None]  # changes this Road to Road R

### Hunting for Michael

You can find if a Road leads to Michael by using its scent. Michael is followed by a horrible, noxious odor: if the scent of a road reads "This one reeks." then you know that that is the road that you must go down. "Pleasant air." denotes that Michael is absolutely not down that road. If it reads "Michael!" then it is the road that Michael is currently on, meaning you only need one more turn to reach him. If you check one road while the other road has Michael, that road will read "I smell Michael on the other road!"

### Final Notes

- Road is a very unorthodox structure. You will have to be able to understand a new, usermade construct based off of its description; a useful skill in the programming world.

- On any given road, one of the next roads will always carry Michael or his wretched stench; you don't need to worry about probability or taking chances.

- The road is infinite. A single mistake will lead to you losing Michael forever, likely timing out your code.

- You may create your own Road object, but it is not useful to do so.

- See a detailed example of the problem in the sample test cases.

- Other Michael katas will soon follow this first one, forming a Michael Series.

<!-- ------------------------------------------------------------ -->

## [Unicode Steganography](https://github.com/MagonBorn/CodeChallenges/blob/main/CodeWars/0018-UnicodeSteganography.py)

### Unicode Steganography

Find the secret messages hidden within seemingly normal text, and learn to encode your own.

### Instructions

You need to implement two functions:  

- `decode`: Retrieves the hidden message from the encoded text.

- `encode`: Encodes a secret message *invisibly* into a given text.  


Can you figure out how the encoding works?

<!-- ------------------------------------------------------------ -->

## [Dreidel Dreidel]()

Let's play a fun gambling game. A dreidel has four sides; here are the descriptions for each of them:

- Nun - nothing happens

- Gimel - you take the pot!

- Hei - you take half the pot (rounded down)

- Shin - you put a piece into the pot

So here's how we play. You, being a raging gambling addict, start with all of your hard earned coins - oy vei! The pot will also have some non-negative amount of coins when the game begins.

Complete the function that given an array of dreidel rolls, the number of coins in your account, and the number of coins in the pot, returns the number of coins left in your account after the last roll.

### Notes:

- you can have a negative amount at the end of the game, just like real gambling :)
- my_coins and pot will always be non-negative

<!-- ------------------------------------------------------------ -->