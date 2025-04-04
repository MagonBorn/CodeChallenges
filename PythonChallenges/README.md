# HackerRank Python Challenges
[PlusMinus](#plusminus)\
[Mini-Max Sum](#mini-max-sum)\
[Time Conversion](#time-conversion)\
[Breaking The Records](#breaking-the-records)\
[Divisible Sum Pairs](#divisible-sum-pairs)

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