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
[Counting Sort 1](#counting-sort-1)

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