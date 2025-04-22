# HackerRank Python Challenges
[PlusMinus](#plusminus)\
[Mini-Max Sum](#mini-max-sum)\
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
[Maximum Perimeter Triangle](#maximum-perimeter-triangle)

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