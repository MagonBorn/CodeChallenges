# HackerRank Python Challenges
[PlusMinus](#plusminus) [Mini-Max Sum](#mini-max-sum)\
[Time Conversion](#time-conversion)\
[Breaking The Records](#breaking-the-records)\
[Divisible Sum Pairs](#divisible-sum-pairs)\
[Lonely Integer](#lonely-integer)\
[Grading Students](#grading-students)\
[Flipping Bits](#flipping-bits)\
[Diagonal Difference](#diagonal-difference)\
[Counting Sort 1](#counting-sort-1)\
[Counting Valleys](#counting-valleys)\
[Pangrams](#pangrams)\
[Mars Exploration](#mars-exploration)\
[Permuting Two Arrays](#permuting-two-arrays)\
[Subarray Division 2](#subarray-division)\
[XOR Strings 3](#xor-strings-3)\
[Sales By Match](#sales-by-match)\
[Migratory Birds](#migratory-birds)\
[Maximum Perimeter Triangle](#maximum-perimeter-triangle)\
[Zig Zag Sequence](#zig-zag-sequence)\
[Drawing Book](#drawing-book)\
[Picking Numbers](#picking-numbers)\
[Left Rotation](#left-rotation)\
[Number Line Jumps](#number-line-jumps)\
[Closest Numbers](#closest-numbers)\
[Tower Breakers](#tower-breakers)\
[Minimum Absolute Difference in an Array](#minimum-absolute-difference-in-an-array)\
[Caesar Cipher](#caesar-cipher)\
[Mock Test Week 4](#mock-test-week-4)\
[Max Min](#max-min)\
[Strong Password](#strong-password)\
[Dynamic Array](#dynamic-array)\
[Smart Number 2](#smart-number-2)\
[Missing Numbers](#missing-numbers)\
[The Full Counting Sort](#the-full-counting-sort)\
[Grid Challenge](#grid-challenge)\
[Sansa and XOR](#sansa-and-xor)\
[Prime Dates](#prime-dates)\
[Sherlock and Array](#sherlock-and-array)\
[Misere Nim](#misere-nim)\
[Gaming Array](#gaming-array)\
[Recursive Digit Sum](#recursive-digit-sum)\
[Counter Game](#counter-game)\
[Sum Vs XOR](#sum-vs-xor)\


## [PlusMinus](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0001-PlusMins.py)
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

### Example
arr=[1,1,0,-1,-1]

There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5, 2/5 and 1/5. Results are printed as:

0.400000\
0.400000\
0.200000

### Function Description
Complete the plusMinus function in the editor below.\
plusMinus has the following parameter(s):\
int arr[n]: an array of integers

### Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

### Input Format
The first line contains an integer, , the size of the array.\
The second line contains  space-separated integers that describe .

### Constraints
0 < n <= 100\
-100 <= arr[i] <= 100

### Output Format
Print the following  lines, each to  decimals:

proportion of positive values\
proportion of negative values\
proportion of zeros

### Sample Input
arr[] size n = 6\
arr = [-4, 3, -9, 0, 4, 1]

### Sample Output
0.500000\
0.333333\
0.166667

### Explanation
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.\
The proportions of occurrence are positive: 3/6 , negative: 2/6 and zeros: 1/6.

<!-- ------------------------------------------------------------ -->

## [Mini-Max Sum](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0002-MiniMaxSum.py)

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

### Example
*arr*=[1,3,5,7,9]\
The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. The function prints

16 24

### Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

- arr: an array of 5 integers

### Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

### Input Format

A single line of five space-separated integers.

### Constraints

1 <= *arr*[i] <= 10<sup>9</sup>

### Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

### Sample Input

1 2 3 4 5

### Sample Output

10 14

### Explanation

The numbers are 1, 2, 3, 4, and 5. Calculate the following sums using four of the five integers:

Sum everything except 1, the sum is 2 + 3 + 4 + 5 = 14.\
Sum everything except 2, the sum is 1 + 3 + 4 + 5 = 13.\
Sum everything except 3, the sum is 1 + 2 + 4 + 5 = 12.\
Sum everything except 4, the sum is 1 + 2 + 3 + 5 = 11.\
Sum everything except 5, the sum is 1 + 2 + 3 + 4 = 10.

<!-- ------------------------------------------------------------ -->

## [Time Conversion](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0003-TimeConversion.py)

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

### Example

- s = **"12:01:00PM"**

Return '12:01:00'.

- s = **12:01:00PM"**

Return '00:01:00'.

### Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

- string s: a time in 12 hour format

### Returns

string: the time in 24 hour format

### Input Format

A single string ***s*** that represents a time in **12**-hour clock format (i.e.: **hh:mm:ssAM** or **hh:mm:ssPM**).

### Constraints

All input times are valid

### Sample Input

07:05:45PM

### Sample Output

19:05:45

<!-- ------------------------------------------------------------ -->

## [Breaking The Records](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0004-BreakingTheRecords.py)

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

### Example

Scores are in the same order as the games played. She tabulates her results as follows:

                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1
Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

### Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

- int scores[n]: points scored per game

### Returns

- int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.

### Input Format

The first line contains an integer *n*, the number of games.
The second line contains  space-separated integers describing the respective values of 
*score*<sub>0</sub>, *score*<sub>1</sub>,....*score*<sub>n-1</sub>.

### Constraints

- 1 $\leq$ *n* $\leq$ 1000
- 0 $\leq$ *scores[i]* $\leq$ 10<sup>8</sup>

<!-- ------------------------------------------------------------ -->

## [Divisible Sum Pairs](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0005-DivisibleSumPairs.py)

Given an array of integers and a positive integer *k*, determine the number of *(i,j)* pairs where *i < j* and *ar[i] + ar[j]* +  is divisible by *k*.

### Example

*ar* = [1,2,3,4,5,6]\
*k* = 5

Three pairs meet the criteria:  [1,4], [2,3], and [4,6].

### Function Description

Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):

- int n: the length of array 
- int ar[n]: an array of integers
- int k: the integer divisor

### Returns

- int: the number of pairs

### Input Format

The first line contains **2** space-separated integers, *n* and *k*.\
The second line contains **n** space-separated integers, each a value of *arr[i]*.

### Constraints

- 2 $\leq$ n $\leq$ 100
- 1 $\leq$ k $\leq$ 100
- 1 $\leq$ arr[i] $\leq$ 100

### Sample Input

    STDIN           Function
    -----           --------
    6 3             n = 6, k = 3
    1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

### Sample Output

    5

### Explanation

Here are the 5 valid pairs when *k* = **3**:
- (0,2) -> arr[0] + arr[2] = 1 + 3 = 3
- (0,5) -> arr[0] + arr[5] = 1 + 2 = 3
- (1,3) -> arr[1] + arr[3] = 3 + 6 = 9
- (2,4) -> arr[2] + arr[4] = 2 + 1 = 3
- (4,5) -> arr[4] + arr[5] = 1 + 2 = 3

<!-- ------------------------------------------------------------ -->

## [Sparse Arrays](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0006-SparseArrays.py)

There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

### Example

*strings* = [*'ab', 'ab', 'abc'*]\
*queries* = [*'ab', 'abc', 'bc'*]


There are **2** instances of '**ab**', **1** of '**abc**' and 0 of '**bc**'. For each query, add an element to the return array,

*results* = [2, 1, 0]

### Function Description

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

- string strings[n] - an array of strings to search
- string queries[q] - an array of query strings

### Returns

- int[q]: an array of results for each query
Input Format

The first line contains and integer **n**, the size of ***strings***[].\
Each of the next **n** lines contains a string ***strings***[**i**].\
The next line contains **q**, the size of ***queries***[].\
Each of the next **q** lines contains a string ***queries***[**i**].

### Constraints

**1 $\leq$ n $\leq$ 1000**\
**1 $\leq$ q $\leq$ 1000**\
**1 $\leq$ |strings[i]|, |queries[i]| $\leq$ 20**\

### Sample Input 1

    4
    aba
    baba
    aba
    xzxb
    3
    aba
    xzxb
    ab

### Sample Output 1

    2
    1
    0

### Sample Input 2

    3
    def
    de
    fgh
    3
    de
    lmn
    fgh

### Sample Output 2

    1
    0
    1

### Sample Input 3

    13
    abcde
    sdaklfj
    asdjf
    na
    basdn
    sdaklfj
    asdjf
    na
    asdjf
    na
    basdn
    sdaklfj
    asdjf
    5
    abcde
    sdaklfj
    asdjf
    na
    basdn

### Sample Output 3

    1
    3
    4
    3
    2

<!-- ------------------------------------------------------------ -->

## [Lonely Integer](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0007-LonelyInteger.py)

Given an array of integers, where all elements but one occur twice, find the unique element.

### Example

**a** = [**1, 2, 3, 4, 3, 2, 1**]

The unique element is **4**.

### Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

- int a[n]: an array of integers

### Returns

- int: the element that occurs only once

### Input Format

The first line contains a single integer, **n**, the number of integers in the array.\
The second line contains **n** space-separated integers that describe the values in **a**.

### Constraints

- **1** $\leq$ **n** $\leq$ **100**
- It is guaranteed that **n** is an odd number and that there is one unique element.
- **0** $\leq$ **a[i]** $\leq$ **100**, where **0** $\leq$ **i** $\lt$ **n**.

<!-- ------------------------------------------------------------ -->

## [Grading Students](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0008-GradingStudents.py)

HackerLand University has the following grading policy:

- Every student receives a ***grade*** in the inclusive range from **0** to **100**.
- Any ***grade*** less than **40** is a failing grade.

Sam is a professor at the university and likes to round each student's ***grade*** according to these rules:

- If the difference between the ***grade*** and the next multiple of **5** is less than **3**, round ***grade*** up to the next multiple of **5**.
- If the value of ***grade*** is less than **38**, no rounding occurs as the result will still be a failing grade.

### Examples
- ***grade*** = **84** round to **85** (85 - 84 is less than 3)
- ***grade*** = **29** do not round (result is less than 40)
- ***grade*** = **57** do not round (60 - 57 is 3 or higher)

Given the initial value of ***grade*** for each of Sam's **n** students, write code to automate the rounding process.

### Function Description

Complete the function gradingStudents in the editor below.

gradingStudents has the following parameter(s):

- int grades[n]: the grades before rounding

### Returns

- int[n]: the grades after rounding as appropriate

### Input Format

The first line contains a single integer, **n**, the number of students.\
Each line *i* of the **n** subsequent lines contains a single integer, ***grades***[**i**].

### Constraints

- **1** $\leq$ **n** $\leq$ **60**
- **0** $\leq$ ***grades***[**i**] $\leq$ **100**

<!-- ------------------------------------------------------------ -->

## [Flipping Bits](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0009-FlippingBits.py)

You will be given a list of 32 bit unsigned integers. Flip all the bits ( **1** -> **0** and **0** -> **1**) and return the result as an unsigned integer.

### Example

**n** = **9**<sub>10</sub>

**9<sub>10</sub>** = **1001<sub>2</sub>** We're working with 32 bits, so:

**00000000000000000000000000001001<sub>2</sub>** = **9<sub>10</sub>**

**11111111111111111111111111110110<sub>2</sub>** = **4294967286<sub>10</sub>**

Return **4294967286**

### Function Description

Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):

- int n: an integer

### Returns

- int: the unsigned decimal integer result

### Input Format

The first line of the input contains ***q***, the number of queries.\
Each of the next ***q*** lines contain an integer, ***n***, to process.

### Constraints

**1** $\leq$ ***q*** $\leq$ **100**

**0** $\leq$ ***n*** $\leq$ **2<sup>32</sup>**

### Sample Input

    3 
    2147483647 
    1 
    0

### Sample Output

    2147483648 
    4294967294 
    4294967295

### Explanation

Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the flipping we get 11111111111111111111111111111110 which in turn is 4294967294.

<!-- ------------------------------------------------------------ -->

## [Diagonal Difference](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0010-DiagonalDifference.py)

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix ***arr*** is shown below:

    1 2 3
    4 5 6
    9 8 9  

The left-to-right diagonal **1 + 5 + 9 = 15**. The right to left diagonal **= 3 + 5 + 9 = 17**. Their absolute difference is **|15 - 17| = 2**.

### Function description

Complete the ***diagonalDifference*** function in the editor below.

diagonalDifference takes the following parameter:

- int arr[n][m]: an array of integers

### Return

- int: the absolute diagonal difference

### Input Format

The first line contains a single integer, ***n***, the number of rows and columns in the square matrix ***arr***.
Each of the next ***n*** lines describes a row, ***arr[i]***, and consists of ***n**** space-separated integers ***arr[i][j]***.

### Constraints

- ***-100*** $\leq$ ***arr[i][j]*** $\leq$ ***100***

### Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

### Sample Input

    3
    11 2 4
    4 5 6
    10 8 -12

### Sample Output

    15

### Explanation

The primary diagonal is:

11
   5
     -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x

<!-- ------------------------------------------------------------ -->

## [Counting Sort 1](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0011-CountingSort1.py)

### Comparison Sorting

Quicksort usually has a running time of ***n X log(n)***, but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat ***n X log(n)*** (worst-case) running time, since ***n X log(n)*** represents the minimum number of comparisons needed to know where to place each element. For more details, you can see [these notes](https://www.cs.cmu.edu/~avrim/451f11/lectures/lect0913.pdf) (PDF).

### Alternative Sorting

Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

### Example

***arr = [1, 1, 3, 2, 1]***

All of the values are in the range **[0...3]**, so create an array of zeros, **results[0, 0, 0, 0]**. The results of each iteration follow:

    i	arr[i]	result
    0	1	[0, 1, 0, 0]
    1	1	[0, 2, 0, 0]
    2	3	[0, 2, 0, 1]
    3	2	[0, 2, 1, 1]
    4	1	[0, 3, 1, 1]

The frequency array is **[0, 3, 1 1]**. These values can be used to create the sorted array as well: ***sorted*** **= [1, 1, 1, 2, 3]**.

### Note

For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.

### Challenge

Given a list of integers, count and return the number of times each value appears as an array of integers.

### Function Description

Complete the countingSort function in the editor below.

countingSort has the following parameter(s):

- arr[n]: an array of integers

### Returns

- int[100]: a frequency array

### Input Format

The first line contains an integer ***n***, the number of items in ***arr***.\
Each of the next ***n*** lines contains an integer ***arr[i]*** where **0** $\leq$ ***arr[i]*** $\le$ ***n***.

### Constraints

**100** $\leq$ ***n*** $\leq$ **10<sup>6</sup>**

**0** $\leq$ ***arr[i]*** $\le$ **100**

### Sample Input

    100
    63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33  

### Sample Output

    0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0 1 1 1 0 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2 

### Explanation

Each of the resulting values ***result[i]*** represents the number of times ***i*** appeared in ***arr***.

<!-- ------------------------------------------------------------ -->

## [Counting Valleys](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0012-CountingValleys.py)

An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly ***steps*** steps, for every step it was noted if it was an uphill, ***U***, or a downhill, ***D*** step. Hikes always start and end at sea level, and each step up or down represents a **1** unit change in altitude. We define the following terms:

- A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.

- A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

### Example

 ***steps*** = ***8 path*** = ***[DDUUUUDD]***

The hiker first enters a valley **2** units deep. Then they climb out and up onto a mountain **2** units high. Finally, the hiker returns to sea level and ends the hike.

### Function Description

Complete the countingValleys function in the editor below.

countingValleys has the following parameter(s):

- int steps: the number of steps on the hike

- string path: a string describing the path

### Returns

- int: the number of valleys traversed

### Input Format

The first line contains an integer ***steps***, the number of steps in the hike.

The second line contains a single string ***path***, of ***steps*** characters that describe the path.

### Constraints

- **2** $\leq$ ***Steps*** $\leq$ **<sup>6</sup>**

- ***path[i]*** $\epsilon$ ***{UD}***

### Sample Input

    8
    UDDDUDUU
    
### Sample Output

    1

### Explanation

If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

    _/\      _
      \    /
        \/\/

The hiker enters and leaves one valley.

<!-- ------------------------------------------------------------ -->

## [Pangrams](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0013-Pangrams.py)

A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

### Example

***s*** = **'The quick brown for jumps over the lazy dog'**

The string contains all letters in the English alphabet, so return pangram.

### Function Description

Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

pangrams has the following parameter(s):

- string s: a string to test

### Returns

- string: either pangram or not pangram

### Input Format

A single line with string ***s***.

### Constraints

**0** $\le$ **length of s** $\leq$ **10<sup>3</sup>**

Each character of **s, s[i]**, $\epsilon$ **{a - z, A - Z, spaCE}**, 

### Sample Input

Sample Input 0

    We promptly judged antique ivory buckles for the next prize

Sample Output 0

    pangram

Sample Explanation 0

    All of the letters of the alphabet are present in the string.

Sample Input 1

    We promptly judged antique ivory buckles for the prize

Sample Output 1

    not pangram

Sample Explanation 0

    The string lacks an x.

<!-- ------------------------------------------------------------ -->

## [Mars Exploration](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0014-MarsExploration.py)

A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.

Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, ***s***, determine how many letters of the SOS message have been changed by radiation.

### Example

***s*** = **'SOSTOT'**

The original message was SOSSOS. Two of the message's characters were changed in transit.

### Function Description

Complete the marsExploration function in the editor below.

marsExploration has the following parameter(s):

- string s: the string as received on Earth

### Returns

- int: the number of letters changed during transmission

### Input Format

There is one line of input: a single string, ***s***.

### Constraints

- **1** $\leq$ length of ***s*** $\leq$ **99**

- length of ***s*** modulo **3 = 0**

- ***s*** will contain only uppercase English letters, ascii[A-Z].

### Explanation

**Sample 0**

***S*** = SOSSPSSQSSOR, and signal length **|S|** = **12**. Sami sent **4** SOS messages (i.e.:**12/3** = **4**).

Expected signal: **SOSSOSSOSSOS**\
Recieved signal: **SOSSPSSQSSOR**

We print the number of changed letters, which is **3**.

**Sample 1**

**S*** = **SOSSOT**, and signal length **|S|**. Sami sent **2** SOS messages (i.e.: **6/3 = 2**).

Expected Signal: **SOSSOS**\
Received Signal: **SOSSOT**

We print the number of changed letters, which is **1**.

<!-- ------------------------------------------------------------ -->

## [Permuting Two Arrays](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0015-PermutingTwoArrays.py)

There are two ***n***-element arrays of integers, ***A*** and ***B***. Permute them into some ***A'*** and ***B'*** such that the relation **A'[i] + B'[i] $\geq$ k** holds for all  where **0 $\leq$ i $\leq$ n**.

There will be ***q*** queries consisting of ***A***, ***B***, and ***k***. For each query, return YES if some permutation ***A'***, ***B'*** satisfying the relation exists. Otherwise, return NO.

### Example

**A** = [**0, 1**]\
**B** = [**0, 2**]\
**k** = **1**

A valid ***A', B'*** is ***A'*** = [**1, 0**] and ***B'*** = [**0, 2**]: **1 + 0 $\geq$ 1** and **0 + 2 $\geq$ 1**. Return YES.

### Function Description

Complete the twoArrays function in the editor below. It should return a string, either YES or NO.

twoArrays has the following parameter(s):

- int k: an integer
- int A[n]: an array of integers
- int B[n]: an array of integers

### Returns

- string: either YES or NO

### Input Format

The first line contains an integer ***q***, the number of queries.

The next ***q*** sets of **3** lines are as follows:

- The first line contains two space-separated integers ***n*** and ***k***, the size of both arrays ***A*** and ***B***, and the relation variable.
- The second line contains ***n*** space-separated integers **A**[i].
- The third line contains ***n*** space-separated integers **B**[i].

### Constraints

- **1 $\leq$ q $\leq$ 10**
- **1 $\leq$ n $\leq$ 1000**
- **1 $\leq$ k $\leq$ 10<sup>9</sup>**
- **0 $\leq$ A[i], B[i] $\leq$ 10<sup>9</sup>**

### Sample Input

    STDIN       Function
    -----       --------
    2           q = 2
    3 10        A[] and B[] size n = 3, k = 10
    2 1 3       A = [2, 1, 3]
    7 8 9       B = [7, 8, 9]
    4 5         A[] and B[] size n = 4, k = 5
    1 2 2 1     A = [1, 2, 2, 1]
    3 3 3 4     B = [3, 3, 3, 4]

### Sample Output

    YES
    NO

### Explanation

There are two queries:

1. Permute these into ***A'*** = [**1, 2, 3**] and ***B'*** = [**7, 8, 9]** so that the following statements are true:

- **A[0] + B[1] = 1 + 9 = 10 $\geq$ k**
- **A[1] + B[1] = 2 + 8 = 10 $\geq$ k**
- **A[2] + B[2] = 3 + 7 = 10 $\geq$ k**

2. **A** = [**1, 2, 2, 1**], **B** = [**3, 3, 3, 4**], and ***k*** = **5**. To permute ***A*** and ***B*** into a valid ***A'*** and ***B'***, there must be at least three numbers in **A** that are greater than **1**.

<!-- ------------------------------------------------------------ -->

## [Subarray Division](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0016-SubarrayDivision.py)

Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

- The length of the segment matches Ron's birth month, and,
- The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.

### Example

***s*** = **[2, 2, 1, 3, 2]**

***d*** = **4**

***m*** =**2**

Lily wants to find segments summing to Ron's birth day, ***d*** = **4** with a length equalling his birth month, ***m*** = **2**. In this case, there are two segments meeting her criteria: **[2, 2]** and **[1, 3]**.

### Function Description

Complete the birthday function in the editor below.

birthday has the following parameter(s):

- int s[n]: the numbers on each of the squares of chocolate
- int d: Ron's birth day
- int m: Ron's birth month

### Returns

- int: the number of ways the bar can be divided

### Input Format

The first line contains an integer ***n***, the number of squares in the chocolate bar.

The second line contains  space-separated integers ***s***[i], the numbers on the chocolate squares where **0** $\leq$ ***i*** $\leq$ ***n***.

The third line contains two space-separated integers, ***d*** and ***m***, Ron's birth day and his birth month.

### Constraints

- **1** $\leq$ ***n*** $\leq$ **100**
- **1** $\leq$ ***s***[i] $\leq$ **5**, where (**0** $\leq$ ***i*** $\le$ ***n***)
- **1** $\leq$ ***d*** $\leq$ **31**
- **1** $\leq$ ***m*** $\leq$ **12**

<!-- ------------------------------------------------------------ -->

## [XOR Strings 3](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0017-XORStrings3.py)

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.

To know more about XOR [Click Here](https://en.wikipedia.org/wiki/Exclusive_or)

Debug the given function strings_xor to find the XOR of the two given strings appropriately.

Note: You can modify at most three lines in the given code and you cannot add or remove lines to the code.

To restore the original code, click on the icon to the right of the language selector.

### Input Format

The input consists of two lines. The first line of the input contains the first string, ***s***, and the second line contains the second string, ***t***.

### Constraints

- **1** $\leq$ |**s**| $\leq$ **10<sup>4</sup>**

- |**s**|  = |**t**|

### Output Format

Print the string obtained by the XOR of the two input strings in a single line.

### Sample Input

    10101
    00101

### Sample Output

    10000

### Explanation

The XOR of the two strings **10101** and **00101** is **1 $\theta$ 0, 0 $\theta$ 0, 1 $\theta$ 1, 0 $\theta$ 0, 1 $\theta$ 1 = 10000**

<!-- ------------------------------------------------------------ -->

## [Sales By Match](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0018-SalesByMatch.py)

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

### Example

***N*** = **7**

***ar*** = [**1, 2, 1, 2, 1, 3, 2**]

There is one pair of color **1** and one of color **2**. There are three odd socks left, one of each color. The number of pairs is **2**.

### Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

- int n: the number of socks in the pile
- int ar[n]: the colors of each sock

### Returns

- int: the number of pairs

### Input Format

The first line contains an integer ***n***, the number of socks represented in ***ar***.
The second line contains ***n*** space-separated integers, ***ar[i]***, the colors of the socks in the pile.

### Constraints

- **1** $\leq$ ***n*** $\leq$ **100**

- **1** $\leq$ ***arr[i]*** $\leq$ **100** where **0** $\leq$ ***i*** $\lt$ ***n***

### Sample Input

    STDIN                       Function
    -----                       --------
    9                           n = 9
    10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

### Sample Output

    3

<!-- ------------------------------------------------------------ -->

## [Migratory Birds](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0019-MigratoryBirds.py)

Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

### Example

***arr*** = **[1, 1, 2, 2, 3]**

There are two each of types **1** and **2**, and one sighting of type **3**. Pick the lower of the two types seen twice: type **1**.

### Function Description

Complete the migratoryBirds function in the editor below.

migratoryBirds has the following parameter(s):

- int arr[n]: the types of birds sighted

### Returns

- int: the lowest type id of the most frequently sighted birds

### Input Format

The first line contains an integer, ***n***, the size of ***arr***.
The second line describes ***arr*** as ***n*** space-separated integers, each a type number of the bird sighted.

### Constraints

- **5** $\leq$ ***n*** $\leq$ **2 x 10<sup>5</sup>**

- It is guaranteed that each type is **1, 2, 3, 4 or 5**.


<!-- ------------------------------------------------------------ -->

## [Maximum Perimeter Triangle](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0020-MaximumPerimeterTriangle.py)

Given an array of stick lengths, use **3** of them to construct a non-degenerate triangle with the maximum possible perimeter. Return an array of the lengths of its sides as  integers in non-decreasing order.

If there are several valid triangles having the maximum perimeter:

Choose the one with the longest maximum side.
1. If more than one has that maximum, choose from them the one with the longest minimum side.
2. If more than one has that maximum as well, print any one them.
3. If no non-degenerate triangle exists, return [-1].

### Example

***sticks*** = **[1, 2, 3, 4, 5, 10]**

The triplet **(1, 2, 3)** will not form a triangle. Neither will **(4, 5, 10)** or **(2, 3, 5)**, so the problem is reduced to **(2, 3, 4)** and **(3, 4, 5)**. The longer perimeter is **3 + 4 + 5 = 12**.

### Function Description

Complete the maximumPerimeterTriangle function in the editor below.

maximumPerimeterTriangle has the following parameter(s):

- int sticks[n]: the lengths of sticks available

### Returns

int[3] or int[1]: the side lengths of the chosen triangle in non-decreasing order or -1

### Input Format

The first line contains single integer ***n***, the size of array ***sticks***.\
The second line contains ***n*** space-separated integers ***sticks[i]***, each a stick length.

### Constraints

- **3** $\leq$ ***n*** $\leq$ **50**

- **1** $\leq$ ***sticks[i]*** $\leq$ **10<sup>9</sup>**

### Explanation

Sample Case 0:
There are **2** possible unique triangles:

1. **(1, 1, 1)**

2. **(1, 3, 3)**

The second triangle has the largest perimeter, so we print its side lengths on a new line in non-decreasing order.

Sample Case 1:
The triangle **(1, 2, 3)** is degenerate and thus can't be constructed, so we print -1 on a new line.

<!-- ------------------------------------------------------------ -->

## [Zig Zag Sequence](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0021-ZigZagSequence.py)

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given an array of ***n*** distinct integers, transform the array into a zig zag sequence by permuting the array elements. A sequence will be called a zig zag sequence if the first  elements in the sequence are in increasing order and the last ***k*** elements are in decreasing order, where ***k*** = (***n*** + **1**)/**2**. You need to find the lexicographically smallest zig zag sequence of the given array.

### Example.

***a*** = **[2, 3, 5, 1, 4]**

Now if we permute the array as **[1, 4, 5, 3, 2]**, the result is a zig zag sequence.

Debug the given function findZigZagSequence to return the appropriate zig zag sequence for the given input array.

**Note**: You can modify at most three lines in the given code. You cannot add or remove lines of code.

To restore the original code, click on the icon to the right of the language selector.

### Input Format

The first line contains ***t*** the number of test cases. The first line of each test case contains an integer ***n***, denoting the number of array elements. The next line of the test case contains ***n*** elements of array ***a***.

### Constraints

**1** $\leq$ ***t*** $\leq$ **20**

**1** $\leq$ ***n*** $\leq$ 10000 (***n*** is always odd)

**1** $\leq$ ***a<sub>i</sub>*** $\leq$ **10<sup>9</sup>**

### Output Format

For each test cases, print the elements of the transformed zig zag sequence in a single line.

<!-- ------------------------------------------------------------ -->

## [Drawing Book](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0022-DrawingBook.py)

A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page **1** is always on the right side:

When they flip page **1**, they see pages **2** and **3**. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is ***n*** pages long, and a student wants to turn to page ***p***, what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

Given ***n*** and ***p***, find and print the minimum number of pages that must be turned in order to arrive at page ***p***.

### Example

***n*** = 5

***p*** = 3

If the student wants to get to page **3**, they open the book to page **1**, flip **1** page and they are on the correct page. If they open the book to the last page, page **5**, they turn **1** page and are at the correct page. Return **1**.

### Function Description

Complete the pageCount function in the editor below.

pageCount has the following parameter(s):

- int n: the number of pages in the book
- int p: the page number to turn to

### Returns

- int: the minimum number of pages to turn

### Input Format

The first line contains an integer ***n***, the number of pages in the book.
The second line contains an integer, ***p***, the page to turn to.

### Constraints

- **1** $\leq$ ***n*** $\leq$ **10<sup>5</sup>**

- **1** $\leq$ ***p*** $\leq$ ***n***

<!-- ------------------------------------------------------------ -->

## [Picking Numbers](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0023-PickingNumbers.py)

Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to **1**.

### Example

***a*** = **[1,1, 2, 2, 4, 4, 5, 5, 5]**

There are two subarrays meeting the criterion: **[1, 1, 2, 2]** and **[4, 4, 5, 5, 5]**. The maximum length subarray has **5** elements.

### Function Description

Complete the pickingNumbers function in the editor below.

pickingNumbers has the following parameter(s):

- int a[n]: an array of integers

### Returns

- int: the length of the longest subarray that meets the criterion

### Input Format

The first line contains a single integer ***n***, the size of the array ***a***.

The second line contains ***n*** space-separated integers, each an ***a***[i].

### Constraints

- **2** $\leq$ ***n*** $\leq$ **100**

- **0** $\lt$ ***a***[i] $\lt$ **100**

- The answer will be $\geq$ **2**

<!-- ------------------------------------------------------------ -->

## [Left Rotation](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0024-LeftRotation.py)

A left rotation operation on an array of size ***n*** shifts each of the array's elements **1** unit to the left. Given an integer, **4**, rotate the array that many steps left and return the result.

### Example

***d*** = **2**

***arr*** = **[1, 2, 3, 4, 5]**

After **2** rotations, ***arr*** = **[3, 4, 5, 1, 2]**.

### Function Description

Complete the rotateLeft function in the editor below.

rotateLeft has the following parameters:

- int d: the amount to rotate by

- int arr[n]: the array to rotate

### Returns

- int[n]: the rotated array

### Input Format

The first line contains two space-separated integers that denote ***n*** , the number of integers, and ***d***, the number of left rotations to perform.
The second line contains ***n*** space-separated integers that describe ***arr*[]***.

### Constraints

- **1** $\leq$ ***n*** $\leq$ **10<sup>5</sup>**

- **1** $\leq$ ***d*** $\leq$ ***n***

- **1** $\leq$ ***a[i]*** $\leq$ **10<sup>6</sup>**

### Sample Input

    5 4
    1 2 3 4 5

### Sample Output

    5 1 2 3 4

### Explanation

To perform ***d*** = **4** left rotations, the array undergoes the following sequence of changes:

**[1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1] -> [3, 4, 5, 1, 2] -> [4, 5, 1, 2, 3] -> [5, 1, 2, 3, 4]**

<!-- ------------------------------------------------------------ -->

## [Number Line Jumps](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0025-NumberLineJumps.py)

You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

- The first kangaroo starts at location ***x*****1** and moves at a rate of ***v*****1** meters per jump.

- The second kangaroo starts at location ***x*****2** and moves at a rate of ***v*****2** meters per jump.

You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

### Example

***x*****1** = **2**

***v*****1** = **1**

***x*****2** = **1**

***v*****2** = **2**

After one jump, they are both at ***x*** = **3**, (***x*****1** + ***v*****1** = **2** + **1**, ***x*****2** + ***v*****2** = **1** + **2**), so the answer is YES.

### Function Description

Complete the function kangaroo in the editor below.

kangaroo has the following parameter(s):

- int x1, int v1: starting position and jump distance for kangaroo 1

- int x2, int v2: starting position and jump distance for kangaroo 2

### Returns

- string: either YES or NO

### Input Format

A single line of four space-separated integers denoting the respective values of ***x*****1**, ***v*****1**, ***x*****2**, and ***v*****2**.

### Constraints

- **0** $\leq$ ***x*****1** $\lt$ ***x*****2** $\leq$ **100000**

- **1** $\leq$ ***v*****1** $\leq$ **100000**

- **1** $\leq$ ***v*****2** $\leq$ **100000**

<!-- ------------------------------------------------------------ -->

## [Closest Numbers](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0026-ClosestNumbers.py)

Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

### Example

***arr*** = [**5, 2, 3, 4, 1**]

Sorted, ***arr*** = [**1, 2, 3, 4, 5**]. Several pairs have the minimum difference of **1**: [(**1, 2), (2, 3), (3, 4), (4, 5)**]. Return the array [**1, 2, 2, 3, 3, 4, 4, 5**].

### Note

As shown in the example, pairs may overlap.

Given a list of unsorted integers, ***arr***, find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.

### Function Description

Complete the closestNumbers function in the editor below.

closestNumbers has the following parameter(s):

- int arr[n]: an array of integers

### Returns

- int[]: an array of integers as described

### Input Format

The first line contains a single integer ***n***, the length of ***arr***.\
The second line contains ***n*** space-separated integers, ***arr***[**i**].

### Constraints

- **2** $\leq$ ***n*** $\leq$ **200000**

- **-10<sup>7</sup>** $\leq$ ***arr***[**i**] $\leq$ **10<sup>7</sup>**

- All **a**[**i**] are unique in ***arr***.

### Output Format

### Sample Input 0

    10
    -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854

### Sample Output 0

    -20 30

### Explanation 0

(30) - (-20) = 50, which is the smallest difference.

### Sample Input 1

    12
    -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470

### Sample Output 1

    -520 -470 -20 30

### Explanation 1

(-470) - (-520) = 30 - (-20) = 50, which is the smallest difference.

### Sample Input 2

    4
    5 4 3 2

### Sample Output 2

    2 3 3 4 4 5

### Explanation 2

Here, the minimum difference is 1. Valid pairs are (2, 3), (3, 4), and (4, 5).

<!-- ------------------------------------------------------------ -->

## [Tower Breakers](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0027-TowerBreakers.py)

Two players are playing a game of Tower Breakers! Player **1** always moves first, and both players always play optimally. The rules of the game are as follows:

- Initially there are *n* towers.

- Each tower is of height *m*.

- The players move in alternating turns.

- In each turn, a player can choose a tower of height *x* and reduce its height to *y*, where **1** $\leq$ *y* $\lt$ *x* and *y* evenly divides *x*.

- If the current player is unable to make a move, they lose the game.

Given the values of *n* and *m*, determine which player will win. If the first player wins, return **1**. Otherwise, return **2**.

### Example. 

***n*** = **2**

***m*** = **6**

There are  towers, each **6** units tall. Player **1** has a choice of two moves:

remove **3** pieces from a tower to leave **3** as **6 modulo = 0**\
remove **5** pieces to leave **1**\
Let Player **1** remove **3**. Now the towers are **3** and **6** units tall.\
Player **2** matches the move. Now the towers are both **3** units tall.\
Now Player **1** has only one move.\
Player **1** removes **2** pieces leaving **1**. Towers are **1** and **2** units tall.\
Player **2** matches again. Towers are both **1** unit tall.\
Player **1** has no move and loses. Return **2**.

### Function Description

Complete the towerBreakers function in the editor below.

towerBreakers has the following paramter(s):

- int n: the number of towers
- int m: the height of each tower

### Returns

- int: the winner of the game

### Input Format

The first line contains a single integer **t**, the number of test cases.
Each of the next **t** lines describes a test case in the form of **2** space-separated integers, *n* and *m*.

### Constraints

- **1** $\leq$ *t* $\leq$ **100**

- **1** $\leq$ *n, m* $\leq$ **10<sup>6</sup>**

### Sample Input

    STDIN   Function
    -----   --------
    2       t = 2
    2 2     n = 2, m = 2
    1 4     n = 1, m = 4

### Sample Output

    2
    1

### Explanation

We'll refer to player **1** as ***P*****1** and player **2** as ***P*****2**

In the first test case, ***P*****1** chooses one of the two towers and reduces it to **1**. Then **P*****2** reduces the remaining tower to a height of **1**. As both towers now have height **1**, ***P*****1** cannot make a move so **P*****2** is the winner.

In the second test case, there is only one tower of height **4**. ***P*****2** can reduce it to a height of either **1** or **2**. ***P*****1** chooses **1** as both players always choose optimally. Because **P*****2** has no possible move, ***P*****1** wins.

<!-- ------------------------------------------------------------ -->

## [Minimum Absolute Difference in an Array](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0028-MinAbsArrayDiff.py)

The absolute difference is the positive difference between two values *a* and *b*, is written |*a* - *b*| or |*b* - *a*| and they are equal. If *a* = **3** and *b* = **2**, |**3** - **2**| = |**2** - **3**| = **1**. Given an array of integers, find the minimum absolute difference between any two elements in the array.

### Example. 

There are **3** pairs of numbers: |-**2**, **2**|, |-**2**, **4**| and |**2**, **4**|. The absolute differences for these pairs are |**(-2)** -**2**| = **4**, |**(-2) -4**| = **6** and |**2 - 4**| = **2**. The minimum absolute difference is **2**.

### Function Description

Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

- int arr[n]: an array of integers

### Returns

- int: the minimum absolute difference found

### Input Format

The first line contains a single integer ***n***, the size of ***arr***.

The second line contains ***n*** space-separated integers, ***arr***[**i**].

### Constraints

- **2** $\leq$ ***n*** $\leq$ **10<sup5</sup>**

- **-10<sup>9</sup>** $\leq$ ***arr***[**i**] $\leq$ **10<sup>9</sup>**

<!-- ------------------------------------------------------------ -->

## [Caesar Cipher](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0029-CaesarCipher.py)

Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

    Original alphabet:      abcdefghijklmnopqrstuvwxyz
    Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

### Example

***s*** = **There's-a-starman-waiting-in-the-sky**

***k*** = **3**

The alphabet is rotated by **3**, matching the mapping above. The encrypted string is 

**Wkhuh'v-d-vwdupdq-zdwlqj-lq-qkh-vnb.**

### Note:
The cipher only encrypts letters; symbols, such as -, remain unencrypted.

### Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

- string s: cleartext
- int k: the alphabet rotation factor

### Returns

- string: the encrypted string

### Input Format

The first line contains the integer, ***n***, the length of the unencrypted string.
The second line contains the unencrypted string, ***s***.
The third line contains ***k***, the number of letters to rotate the alphabet by.

### Constraints

- **1** $\leq$ ***n*** $\leq$ **100**

- **0** $\leq$ ***k*** $\leq$ **100**

***s*** is a valid ASCII string without any spaces.

### Sample Input

    11
    middle-Outz
    2

### Sample Output

    okffng-Qwvb

### Explanation

    Original alphabet:      abcdefghijklmnopqrstuvwxyz
    Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

    m -> o
    i -> k
    d -> f
    d -> f
    l -> n
    e -> g
    -    -
    O -> Q
    u -> w
    t -> v
    z -> b

<!-- ------------------------------------------------------------ -->

## [Mock Test Week 4](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0030-MockTestWeek4.py)

Two words are anangrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of each other.

### Example

***s*** = **abccde**
Break ***s*** into two parts 'abc' and 'cde'. Note that all letter have been used, the substrings are contiguous and their lengths are equal. Now you can change the 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' with are anagrams. Two changes were necessary.

### Function Desacription

Complete the anagram function: *anagram* has the following parameter(s):

- *string s*: a string

### Returns

- *int*: the minimum number of changes of characters to change or -1.

### Input format

The first line will contain an integer *q*, the number of test cases.\
Each test case will contain a string *s*.

### Constraints

- **1** $\leq$ *q* $\leq$ **100**

- **1** $\leq$ |*s*| $\leq$ **10<sup4</sup>**

-*s* consists only of characters in the range ascii[a-z].

### Sample Input

    6
    aaabbb
    ab
    abc
    mnop
    xyyx
    xaxbbbxx

### Sample Output

    3
    1
    -1
    2
    0
    1

### Explanation

*Test case #01:* We split *s* into two strings ***S1***='aaa' and ***S2***='bbb'. We have to replace all three characters from the first string with 'b' to make the stings anagrams.

*Test case #02:* You have to replace 'a' with 'b', which will generate 'bb'.

*Test case #3:* It is not possible for two strings of unequal length to be anagrans of one another.

*Test case #4:* We have to replace both the characters of the first string ('mn') to make it an anagram of the other one.

*Test case #5*: ***S1*** and ***S2*** are already anagrams of one another.

*Test case #6:* here S1 = 'xaxb' and S2 = 'bbxx'. You must replace 'a' from S1 with 'b' so that S1 = 'xbxb'.

<!-- ------------------------------------------------------------ -->

## [Max Min](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0031-MaxMin.py)

You will be given a list of integers, ***arr***, and a single integer ***k***. You must create an array of length ***k*** from elements of ***arr*** such that its unfairness is minimized. Call that array ***arr'***. Unfairness of an array is calculated as

- ***max(arr') - min(arr')***

Where:
- max denotes the largest integer in ***arr'***
- min denotes the smallest integer in ***arr'***

### Example

***arr*** = [**1, 4, 7, 2**]

**k** = **2**

Pick any two elements, say ***arr'*** = [**4, 7**].

***unfairness*** = ***max***(**4, 7**) - ***min***(**4, 7**) = **7** - **4** = **3**

Testing for all pairs, the solution [**1, 2**] provides the minimum unfairness.

**Note**: Integers in ***arr*** may not be unique.

### Function Description

Complete the maxMin function in the editor below.

maxMin has the following parameter(s):

- int k: the number of elements to select

- int arr[n]: an array of integers

### Returns

- int: the minimum possible unfairness

### Input Format

The first line contains an integer ***n***, the number of elements in array ***arr***.\
The second line contains an integer ***k***.\
Each of the next ***n*** lines contains an integer ***arr***[**i**] where **0** $\leq$ ***i*** $\lt$ ***n***.

### Constraints

- **2** $\leq$ ***n*** $\leq$ **10<sup>5</sup>**

- **2** $\leq$ ***k*** $\leq$ ***n***

- **0** $\leq$ ***arr***[**i**] $\leq$ **10<sup>9</sup>**

### Sample Input

### Sample Input #01

    10
    4
    1
    2
    3
    4
    10
    20
    30
    40
    100
    200

### Sample Output

### Sample Output #01

    3

### Explanation

### Explanation #01

Here ***K*** = **4**; selecting the **4** integers **1, 2, 3, 4**, unfairness equals

    max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3

<!-- ------------------------------------------------------------ -->

## [Strong Password](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0032-StrongPassword.py)

Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

- Its length is at least **6**.
- It contains at least one digit.
- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
- It contains at least one special character. The special characters are: !@#$%^&*()-+

She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

### Example

**password** = **'2bbbb'**

This password is 5 characters long and is missing an uppercase and a special character. The minimum number of characters to add is **2**.

**password** = **'2bb#A'**

This password is 5 characters long and has at least one of each character type. The minimum number of characters to add is **1**.

### Function Description

Complete the minimumNumber function in the editor below.

minimumNumber has the following parameters:

- int n: the length of the password
- string password: the password to test

### Returns

- int: the minimum number of characters to add

### Input Format

The first line contains an integer ***n***, the length of the password.

The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

### Constraints

- **1** $\leq$ ***n*** $\leq$ **100**

- All characters in ***password*** are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ].

<!-- ------------------------------------------------------------ -->

## [Dynamic Array](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0033-DynamicArray.py)

- Declare a 2-dimensional array, ***arr***, of ***n*** empty arrays. All arrays are zero indexed.

- Declare an integer, ***lastAnswer***, and initialize it to **0**.

- There are **2** types of queries, given as an array of strings for you to parse:

1. Query: 1 x y\
  1 Let ***idx*** = ((x $\oplus$ lastAnswer) % n).\
  2 Append the integer ***y*** to ***arr[idx]***.

2. Query: 2 x y\
  1 Let ***idx*** = ((x $\oplus$ lastAnswer) % n).\
  2 Assign the value arr[idx][y % size(arr[idx])] to ***lastAnswer***\
  3 Store the new value of ***lastAnswer*** to an answers array.

**Note:** $\oplus$ is the bitwise XOR operation, which corresponds to the ^ operator in most languages. % is the modulo operator.

Finally, size(arr[idx]) is the number of elements in arr[idx]

### Function Description

Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty arrays to initialize in ***arr***
- string queries[q]: query strings that contain 3 space-separated integers

### Returns

int[]: the results of each type 2 query in the order they are presented

### Input Format

The first line contains two space-separated integers, ***n***, the size of ***arr*** to create, and ***q***, the number of queries, respectively.

Each of the ***q*** subsequent lines contains a query string, ***queries[i]***.

### Constraints

- **1** $\leq$ ***n,q*** $\leq$ **10<sup>5</sup>**

- **0** $\leq$ ***x,y*** $\leq$ **10<sup>9</sup>**

- It is guaranteed that query type **2** will never query an empty array or index.

### Sample Input

    2 5
    1 0 5
    1 1 7
    1 0 3
    2 1 0
    2 1 1

### Sample Output

    7
    3

### Explanation

- Initial Values:
n = 2\
lastAnswer = 0\
arr[0] = []\
arr[0] = []

- Query 0: Append 5 to arr[((0 $\oplus$ 0) % 2)] = arr[0]
lastAnswer = 0\
arr[0] = [5]\
arr[1] = []

- Query 1: Append 7 to arr[((1 $\oplus$ 0) % 2)] = arr[1]
arr[0] = [5]\
arr[1] = [7]

- Query 2: Append 3 to arr[((0 $\oplus$ 0) % 2)] = arr[0]
arr[0] = [5, 3]\
arr[1] = [7]

- Query 3: Assign the value at index 0 of arr[((1 $\oplus$ 0) % 2)] = arr[1] to lastAnswer. print last answer.\
lastAnswer = 7
arr[0] = [5, 3]\
arr[1] = [7]

- Query 4: Assign the value at index 1 of arr[((1 $\oplus$ 7) % 2)] = arr[0] to lastAnswer. print last answer.\
lastAnswer = 3
arr[0] = [5, 3]\
arr[1] = [7]

<!-- ------------------------------------------------------------ -->

## [Smart Number 2](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0034-SmartNumber2.py)

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

A number is called a smart number if it has an odd number of factors. Given some numbers, find whether they are smart numbers or not.

Debug the given function is_smart_number to correctly check if a given number is a smart number.

**Note:** You can modify only one line in the given code and you cannot add or remove any new lines.

To restore the original code, click on the icon to the right of the language selector.

### Input Format

The first line of the input contains , the number of test cases.
The next  lines contain one integer each.

### Constraints

- **1** $\leq$ ***t*** $\leq$ **10<sup>3</sup>**

- **1** $\leq$ ***n<sub>i</sub>*** $\leq$ **10<sup>4</sup>**, where ***n<sub>i</sub>*** is the ***i<sup>th</sup>*** integer.

### Output Format

The output should consist of ***t*** lines. In the ***i<sup>th</sup>*** line print YES if the  integer has an odd number of factors, else print NO.

### Sample Input

    4
    1
    2
    7
    169

### Sample Output

    YES
    NO
    NO
    YES

### Explanation

The factors of 1 are just 1 itself.So the answer is YES. The factors of 2 are 1 and 2.It has even number of factors.The answer is NO. The factors of 7 are 1 and 7.It has even number of factors.The answer is NO. The factors of 169 are 1,13 and 169.It has odd number of factors.The answer is YES.

<!-- ------------------------------------------------------------ -->

## [Missing Numbers](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0035-MissingNumbers.py)

Given two arrays of integers, find which elements in the second array are missing from the first array.

### Example

***arr*** = [**7, 2, 5, 3, 5, 3**]

***brr*** = [**7, 2, 5, 4, 6, 3, 5, 3**]

The ***brr*** array is the orginal list. The numbers missing are [**4, 6**].

**Notes**

- If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.

- Return the missing numbers sorted ascending.

- Only include a missing number once, even if it is missing multiple times.

- The difference between the maximum and minimum numbers in the original list is less than or equal to **100**.

### Function Description

Complete the missingNumbers function in the editor below. It should return a sorted array of missing numbers.

missingNumbers has the following parameter(s):

- int arr[n]: the array with missing numbers
- int brr[m]: the original array of numbers

### Returns

- int[]: an array of integers

### Input Format

There will be four lines of input:

***n*** - the size of the first list, ***arr***\
The next line contains ***n*** space-separated integers ***arr***[**i**]\
***m*** - the size of the second list, ***brr***\
The next line contains ***m*** space-separated integers 

### Constraints

- **1** $\leq$ ***n, m*** $\leq$ **2 x 10<sup>5</sup>**

- ***n*** $\leq$ ***m***

- **1** $\leq$ ***brr***[**i**] $\leq$ **10<sup>4</sup>**

- ***max(brr)*** - ***min(brr)*** $\leq$ **100**

### Sample Input

    10
    203 204 205 206 207 208 203 204 205 206
    13
    203 204 204 205 206 207 205 208 203 206 205 206 204

### Sample Output

    204 205 206

### Explanation

**204** is present in both arrays. Its frequency in ***arr*** is **2**, while its frequency in ***b*** is **3**. Similarly, **205** and **206** occur twice in ***arr***, but three times in ***brr***. The rest of the numbers have the same frequencies in both lists.

<!-- ------------------------------------------------------------ -->

## [The Full Counting Sort](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0036-TheFullCountingSort.py)

Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).

Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

Design your counting sort to be stable.

### Example

***arr*** = [[**0, 'a'***], [**1, 'b'**], [**0, 'c'**], [**1, 'd'**]]

The first two strings are replaced with '-'. Since the maximum associated integer is **1**, set up a helper array with at least two empty arrays as elements. The following shows the insertions into an array of three empty arrays.

    i	string	converted	list
    0				[[],[],[]]
    1 	a 	-		[[-],[],[]]
    2	b	-		[[-],[-],[]]
    3	c			[[-,c],[-],[]]
    4	d			[[-,c],[-,d],[]]

The result is then printed: -c -d.

### Function Description

Complete the countSort function in the editor below. It should construct and print the sorted strings.

countSort has the following parameter(s):

- string arr[n][2]: each arr[i] is comprised of two strings, x and s

### Returns

- Print the finished array with each element separated by a single space.

**Note:** The first element of each ***arr***[**i**], ***x***, must be cast as an integer to perform the sort.

### Input Format

The first line contains ***n***, the number of integer/string pairs in the array ***arr***.

Each of the next ***n*** contains  ***x***[**i**] and ***s***[**i**], the integers (as strings) with their associated strings.

### Constraints

- **1** $\leq$ ***n*** $\leq$ **1000000**

- ***n*** is even

- **1** $\leq$ | **s** | $\leq$ **10**

- **0** $\leq$ ***x*** $\lt$ **100**, **$x \in ar$**

- ***s***[**i**] consists of characters in the rangfe **ascii[a-z]**

### Output Format

Print the strings in their correct order, space-separated on one line.

### Sample Input

    20
    0 ab
    6 cd
    0 ef
    6 gh
    4 ij
    0 ab
    6 cd
    0 ef
    6 gh
    0 ij
    4 that
    3 be
    0 to
    1 be
    5 question
    1 or
    2 not
    4 is
    2 to
    4 the

### Sample Output

    - - - - - to be or not to be - that is the question - - - -

### Explanation

The correct order is shown below. In the array at the bottom, strings from the first half of the original array were replaced with dashes.

    0 ab
    0 ef
    0 ab
    0 ef
    0 ij
    0 to
    1 be
    1 or
    2 not
    2 to
    3 be
    4 ij
    4 that
    4 is
    4 the
    5 question
    6 cd
    6 gh
    6 cd
    6 gh

    sorted = [['-', '-', '-', '-', '-', 'to'], ['be', 'or'], ['not', 'to'], ['be'], ['-', 'that', 'is', 'the'], ['question'], ['-', '-', '-', '-'], [], [], [], []]

<!-- ------------------------------------------------------------ -->

## [Grid Challenge](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0037-GridChallenge.py)

Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

### Example

***grid*** = [**'abc', 'ade', 'efg'**]

The grid is illustrated below.

    a b c
    a d e
    e f g

The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

### Function Description

Complete the gridChallenge function in the editor below.

gridChallenge has the following parameter(s):

- string grid[n]: an array of strings

### Returns

- string: either YES or NO

### Input Format

The first line contains ***t***, the number of testcases.

Each of the next  sets of lines are described as follows:
- The first line contains ***n***, the number of rows and columns in the grid.
- The next ***n*** lines contains a string of length 

### Constraints

- **1** $\leq$ ***t*** $\leq$ **100**

- **1** $\leq$ ***n*** $\leq$ **100**

Each string consists of lowercase letters in the range ascii[a-z]

### Output Format

For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or NO otherwise.

### Sample Input

    STDIN   Function
    -----   --------
    1       t = 1
    5       n = 5
    ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    fghij
    olmkn
    trpqs
    xywuv

### Sample Output

    YES

### Explanation

The **5**x**5** grid in the **1** test case can be reordered to

    abcde
    fghij
    klmno
    pqrst
    uvwxy

This fulfills the condition since the rows 1, 2, ..., 5 and the columns 1, 2, ..., 5 are all alphabetically sorted.

<!-- ------------------------------------------------------------ -->

## [Sansa and XOR](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0038-SansaAndXOR.py)

Sansa has an array. She wants to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the values thus obtained. Determine this value.

Example

***arr*** = [**3, 4, 5**]

    Subarray	Operation	Result
    3		None		3
    4		None		4
    5		None		5
    3,4		3 XOR 4		7
    4,5		4 XOR 5		1
    3,4,5		3 XOR 4 XOR 5	2

Now we take the resultant values and XOR them together:

**3** $\theta$ **4** $\theta$ **5** $\theta$ **7** $\theta$ **1** $\theta$ **2** = **6**. Return **6**.

### Function Description

Complete the sansaXor function in the editor below.

sansaXor has the following parameter(s):

- int arr[n]: an array of integers

### Returns

- int: the result of calculations

### Input Format

The first line contains an integer ***t***, the number of the test cases.

Each of the next ***t*** pairs of lines is as follows:

- The first line of each test case contains an integer ***n***, the number of elements in ***arr***.

- The second line of each test case contains ***n*** space-separated integers ***arr***[**i**].

### Constraints

- **1** $\leq$ ***t*** $\leq$ **5**

- **2** $\leq$ ***n*** $\leq$ **10<sup>5</sup>**

- **1** $\leq$$ ***arr***[**i**] $\leq$ **10<sup>8</sup>**

### Sample Input

    2
    3
    1 2 3
    4
    4 5 7 5

### Sample Output

    2
    0

### Explanation

#### Test case #00:
**1** $\theta$ **2** $\theta$ **3** $\theta$ (**1** $\theta$ **2**) $\theta$ (**2** $\theta$ **3**) $\theta$ (**1** $\theta$ **2** $\theta$ **3**) = **2**

#### Test case #01:
**4** $\theta$ **5** $\theta$ **7** $\theta$ **5** $\theta$ (**4** $\theta$ **5**) $\theta$ (**5** $\theta$ **7**) $\theta$ (**7** $\theta$ **5**) $\theta$ (**4** $\theta$ **5** $\theta$ **7**) $\theta$ (**5** $\theta$ **7** $\theta$ **5**) $\theta$ (**4** $\theta$ **5** $\theta$ **7** $\theta$ **5**) = **0**

<!-- ------------------------------------------------------------ -->

## [Prime Dates](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0040-PrimeDates.py)

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given two dates each in the format dd-mm-yyyy, you have to find the number of lucky dates between them (inclusive). To see if a date is lucky,

- Firstly, sequentially concatinate the date, month and year, into a new integer ***x*** erasing the leading zeroes.

- Now if ***x*** is divisible by either **4** or **7**, then we call the date a lucky date.

For example, let's take the date "02-08-2024". After concatinating the day, month and year, we get ***x***  = 2082024. As ***x*** is divisible by **4** so the date "02-08-2024" is called a lucky date.

Debug the given function findPrimeDates and/or other lines of code, to find the correct lucky dates from the given input.

**Note:** You can modify at most five lines in the given code and you cannot add or remove lines to the code.

To restore the original code, click on the icon to the right of the language selector.

### Input Format

The only line of the input contains two strings ***u*** and ***v*** denoting the two dates following the format dd-mm-yyyy. Consider, ***d*** is the day number, ***m*** is the month number and ***y*** is the year number.

Note: Here ***m*** = **1** means January, ***m*** = **2** means February, ***m*** = **3** means March and so on and all the dates follow the standard structure of English calender including the leap year.

### Constraints

- **1** $\leq$ ***d2, d2*** $\leq$ **31**

- **1** $\leq$ ***m1, m2*** $\leq$ **12**

- **1000** $\leq$ ***y1*** $\leq$ ***y2*** $\leq$ **9999**

### Output Format

For each test cases, print a single integer the number of lucky dates between ***u*** and ***v*** in a single line.

<!-- ------------------------------------------------------------ -->

## [Sherlock And Array](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0041-SherlockAndArray.py)

Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.

### Example

***arr*** = [**5, 6, 8, 11**]

**8** is between two subarrays that sum to **11**.

***arr*** = [**1**]

The answer is [**1**] since left and right sum to **0**.

You will be given arrays of integers and must determine whether there is an element that meets the criterion. If there is, return YES. Otherwise, return NO.

### Function Description

Complete the balancedSums function in the editor below.

balancedSums has the following parameter(s):

- int arr[n]: an array of integers

### Returns

- string: either YES or NO

### Input Format

The first line contains **T**, the number of test cases.

The next **T** pairs of lines each represent a test case.

- The first line contains ***n***, the number of elements in the array ***arr***.
- The second line contains ***n*** space-separated integers ***arr***[**i**] where **0** $\leq$ ***i*** $\lt$ ***n***.

### Constraints

- **1** $\leq$ **T** $\leq$ **10**

- **1** $\leq$ ***n*** $\leq$ **10<sup>5</sup>**

- **1** $\leq$ ***arr***[**i**] $\leq$ **2 x 10</sup>4</sup>**

- **0** $\leq$ ***i*** $\lt$ ***n***

### Sample Input

    2
    3
    1 2 3
    4
    1 2 3 3

### Sample Output

    NO
    YES

### Explanation

For the first test case, no such index exists.
For the second test case, **A[0] + A[1] = A[3]**, therefore index **2** satisfies the given conditions

<!-- ------------------------------------------------------------ -->

## [Misere Nim](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0042-MisereNim.py)

Two people are playing game of Misère Nim. The basic rules for this game are as follows:

- The game starts with  piles of stones indexed from **0** to ***n*** - **1**. Each pile ***i*** (where **0** $\leq$ ***i*** $\lt$ ***n***) has ***s<sub>i</sub>*** stones.

- The players move in alternating turns. During each move, the current player must remove one or more stones from a single pile.

- The player who removes the last stone loses the game.

Given the value of ***n*** and the number of stones in each pile, determine whether the person who wins the game is the first or second person to move. If the first player to move wins, print First on a new line; otherwise, print Second. Assume both players move optimally.

### Example

***s*** = [**1, 1, 1**]

In this case, player 1 picks a pile, player 2 picks a pile and player 1 has to choose the last pile. Player 2 wins so return Second.

***s*** = [**1, 2, 2**]

There is no permutation of optimal moves where player 2 wins. For example, player 1 chooses the first pile. If player 2 chooses 1 from another pile, player 1 will choose the pile with 2 left. If player 2 chooses a pile of 2, player 1 chooses 1 from the remaining pile leaving the last stone for player 2. Return First.

### Function Description

Complete the misereNim function in the editor below.

misereNim has the following parameters:

- int s[n]: the number of stones in each pile

### Returns

- string: either First or Second

### Input Format

The first line contains an integer, **T**, the number of test cases.
Each test case is described over two lines:

- An integer, ***n***, the number of piles.

**n** space-separated integers, ***s***[**i**], that describe the number of stones at pile ***i***.

### Constraints

- **1** $\leq$ **T** $\leq$ **100**

- **1** $\leq$ ***n*** $\leq$ **100**

- **1** $\leq$ ***s***[**i**] $\leq$ **10<sup>9</sup>**

### Sample Input

    STDIN   Function
    -----   --------
    2       T = 2
    2       s[] size n = 2
    1 1     s = [1, 1]
    3       s[] size n = 3
    2 1 3   s = [2, 1, 3]

### Sample Output

    First
    Second

### Explanation

In the first testcase, the first player removes 1 stone from the first pile and then the second player has no moves other than removing the only stone in the second pile. So first wins.

<!-- ------------------------------------------------------------ -->

## [Gaming Array](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0043-GamingArray1.py)

Andy wants to play a game with his little brother, Bob. The game starts with an array of distinct integers and the rules are as follows:

- Bob always plays first.

- In a single move, a player chooses the maximum element in the array. He removes it and all elements to its right. For example, if the starting array ***arr*** = [**2, 3, 5, 4, 1**], then it becomes ***arr'*** = [**2, 3**] after removing [**5, 4, 1**].

- The two players alternate turns.

- The last player who can make a move wins.

Andy and Bob play ***g*** games. Given the initial array for each game, find and print the name of the winner on a new line. If Andy wins, print ANDY; if Bob wins, print BOB.

To continue the example above, in the next move Andy will remove **3**. Bob will then remove **2** and win because there are no more integers to remove.

### Function Description

Complete the gamingArray function in the editor below.

gamingArray has the following parameter(s):

- int arr[n]: an array of integers

### Returns

- string: either ANDY or BOB

### Input Format

The first line contains a single integer , the number of games.

Each of the next ***g*** pairs of lines is as follows:

- The first line contains a single integer, ***n***, the number of elements in ***arr***.

- The second line contains ***n*** distinct space-separated integers ***arr***[**i**] where **0** $\leq$ **i** $\lt$ ***n***.

### Constraints

- Array ***arr*** contains ***n*** distinct integers.

For **35%** of the maximum score:

- **1** $\leq$ ***g*** $\leq$ **10**

- **1** $\leq$ ***n*** $\leq$ **1000**

- **1** $\leq$ ***arr***[**i**] $\leq$ **10<sup>5</sup>**

- The sum of ***n*** over all games does not exceed **1000**.

For **100%** of the maximum score:

- **1** $\leq$ ***g*** $\leq$ **10**

- **1** $\leq$ ***n*** $\leq$ **10<sup>5</sup>**

- **1** $\leq$ ***a<sub>i</sub>*** $\leq$ **10<sup>9</sup>**

- The sum of ***n*** over all games does not exceed **10<sup>5</sup>**.

<!-- ------------------------------------------------------------ -->

## [Forming A Magic Square]()

We define a magic square to be an $n \times n$ matrix of distinct positive integers from **1** to ***n<sup>2</sup>*** where the sum of any row, column, or diagonal of length ***n*** is always equal to the same number: the magic constant.

You will be given a $3 \times 3$ matrix ***s*** of integers in the inclusive range [**1, 9**]. We can convert any digit $a$ to any other digit $b$ in the range $[1, 9]$ at cost of $|a - b|$. Given $s$, convert it into a magic square at minimal cost. Print this cost on a new line.

**Note:** The resulting magic square must contain distinct integers in the inclusive range $[1, 9]$.

### Example

$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

The matrix looks like this:

    5 3 4
    1 5 8
    6 4 2

We can convert it to the following magic square:

    8 3 4
    1 5 9
    6 7 2

This took three replacements at a cost of $|5 - 8| + |8 - 9| + |4 - 7| = 7$.

### Function Description

Complete the formingMagicSquare function in the editor below.

formingMagicSquare has the following parameter(s):

- int s[3][3]: a $3 \times 3$ array of integers

### Returns

- int: the minimal total cost of converting the input square to a magic square

### Input Format

Each of the $3$ lines contains three space-separated integers of row $s[i]$.

### Constraints

- $s[i][j] \epsilon [1, 9]$

### Sample Input

    4 9 2
    3 5 7
    8 1 5

### Sample Output

    1

### Explanation

Matrix $s$ initially looks like this:

    4 9 2
    3 5 7
    8 1 5

Observe that it's not yet magic, because not all rows, columns, and center diagonals sum to the same number.

If we change the bottom right value, $s[2][2]$, from $5$ to $6$ at a cost of $\|6 - 5| = 1$, $s$ becomes a magic square at the minimum possible cost. Thus, we print the cost, $1$, on a new line.

<!-- ------------------------------------------------------------ -->

## [Recursive Digit Sum](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0045-RecursiveDigitSum.py)

We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

- If $x$ has only $1$ digit, then its super digit is $x$.

- Otherwise, the super digit of $x$ is equal to the super digit of the sum of the digits of $x$.

For example, the super digit of  will be calculated as:

      super_digit(9875)   9+8+7+5 = 29 
      super_digit(29)     2 + 9 = 11
      super_digit(11)     1 + 1 = 2
      super_digit(2)      = 2  

### Example

$n = '9875'$\
$k = 4$

The number $p$ is created by concatenating the string $n k$ times so the initial $p = 9875987598759875$.

    superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)

All of the digits of $p$ sum to $116$. The digits of $116$ sum to $8$. $8$ is only one digit, so it is the super digit.

### Function Description

Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

- string n: a string representation of an integer
- int k: the times to concatenate $n$ to make $p$

### Returns

- int: the super digit of $n$ repeated $k$ times

### Input Format

The first line contains two space separated integers, $n$ and $k$.

### Constraints

- $1$ $\leq$ $n$ $\lt$ $10$<sup>100000</sup>

- $1$ $\leq$ $k$ $\leq$ $10$<sup>5</sup>

<!-- ------------------------------------------------------------ -->

## [Counter Game](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0046-CounterGame.pyt)

Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of $2$. If it is, they divide it by $2$. If not, they reduce it by the next lower number which is a power of $2$. Whoever reduces the number to  wins the game. Louise always starts.

Given an initial value, determine who wins the game.

### Example

It's Louise's turn first. She determines that $132$ is not a power of $2$. The next lower power of $2$ is $127$, so she subtracts that from $132$ and passes $4$ to Richard. $4$ is a power of $2$, so Richard divides it by $2$ and passes $2$ to Louise. Likewise, $2$ is a power so she divides it by $2$ and reaches $1$. She wins the game.

**Update** If they initially set counter to $1$, Richard wins. Louise cannot make a move so she loses.

### Function Description

Complete the counterGame function in the editor below.

counterGame has the following parameter(s):

- int n: the initial game counter value

### Returns

- string: either Richard or Louise

### Input Format

The first line contains an integer $t$, the number of testcases.
Each of the next $t$ lines contains an integer $n$, the initial value for each game.

### Constraints

- $1$ $\leq$ $t$ $\leq$ $10$

- $1$ $\leq$ $n$ $\leq$ $24$<sup>64</sup> $-1$

### Sample Input

    1
    6

### Sample Output

    Richard

### Explanation

- As $6$ is not a power of $2$, Louise reduces the largest power of $2$ less than $6$ i.e., $4$, and hence the counter reduces to $2$.

- As $2$ is a power of $2$, Richard reduces the counter by half of $2$ i.e., $1$. Hence the counter reduces to $1$.

As we reach the terminating condition with $N == 1$, Richard wins the game.

<!-- ------------------------------------------------------------ -->

## [Sum Vs XOR](https://github.com/MagonBorn/CodeChallenges/blob/main/PythonChallenges/0047-SumVsXOR.py)

Given an integer $n$, find each $x$ such that:

- $0\leq x\leq n$

- $n+x=n\oplus x$

where $\oplus$ denotes the bitwise XOR operator. Return the number of $x$'s satisfying the criteria.

### Example

$n=4$

There are four values that meet the criteria:

- $4+1=4\oplus 0=4$

- $4+1=4\oplus 1=5$

- $4+2=4\oplus 2=6$

- $4+3=4\oplus 3=7$

Return $4$.

### Function Description

Complete the sumXor function in the editor below.

sumXor has the following parameter(s):

- int n: an integer

### Returns

- int: the number of values found

### Input Format

A single integer, $n$.

### Constraints

- $n\leq n\leq 10$<sup>15</sup>

### Subtasks

- $0\leq n\leq 100$ for 60% of the maximum score.

### Output Format

### Sample Input 0

    5

### Sample Output 0

    2

### Explanation 0

For $n=5$, the $x$ values $0$ and $2$ satisfy the conditions:

- $5+0=5$, $5\oplus 0=5$

- $5+2=7$, $5\oplus 2=7$

### Sample Input 1

    10

### Sample Output 1

    4

### Explanation 1

For $n=10$, the $x$ values $0$, $1$, $4$, and $5$ satisfy the conditions:

- $10+0=10$, $10\oplus 0=10$

- $10+1=11$, $10\oplus 1=11$

- $10+2=14$, $10\oplus 4=14$

- $10+5=15$, $10\oplus 5=15$

<!-- ------------------------------------------------------------ -->

