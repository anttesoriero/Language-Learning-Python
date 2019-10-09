# Programming-Lanuages-Python
For the python group, fall 2019 Programming Languages class, [Dr. Nancy Tinkham](http://elvis.rowan.edu/~nlt/), at Rowan University.
The purpose of these assignments is to learn a new programming language.

## Assignments
### 1. Beginner's program
Write a program that will read two numbers and will compute the sum of those two numbers. (If you are working in a functional language, you may write a function that takes two numbers as input parameters and returns the sum of the two numbers.)

### 2. Simple repetition
Write a program that will read a sequence of numbers and will compute the sum of those numbers.

Note: If your language supports lists, your input can be a list (e.g., [10, 6, 2, 8, 12]). Otherwise, have the user enter a special value to indicate the end of the input, or ask the user at the beginning of the program how many numbers will be entered. Be prepared to handle any nonnegative quantity of numbers.

### 3. Floating-point calculation
Write a program to read a positive integer N and print out the sum of the first N terms of the alternating harmonic series.

The alternating harmonic series is

1 - 1/2 + 1/3 - 1/4 + 1/5 - ...
For example, if N = 3, then the sum is 1 - 1/2 + 1/3 = 0.83333
If the user enters a negative value for N, print an error message or return an error value instead of attempting to compute the sum of the series. 

### 4. Text file format conversion
Write a program that will take a text file with lines in this format:

```
Last_name:First_name:Number_of_cats:Number_of_dogs:Number_of_fish:Number_of_other_pets
```
and produce a text file with lines in this format:
```
First_name Last_name:Total_number_of_pets
```
For example, if the original text file looks like this:
```
Chawla:Kalpana:0:0:3:0
Davis:Jo Ann:0:0:5:2
de Vries:Gustav:3:1:0:1
Goldberg:Adele:2:1:1:0
Noriega:Carlos:2:2:0:0
Ride:Sally:0:1:0:2
Turing:Alan:0:0:0:0
```
the new text file should look like this:
```
Kalpana Chawla:3
Jo Ann Davis:7
Gustav de Vries:5
Adele Goldberg:4
Carlos Noriega:4
Sally Ride:3
Alan Turing:0
```
Note that first and last names can contain spaces. The delimiter between fields in the original file will be colon (:), not space. 

### 5. Concurrency

### 6. Semester homework problem

## Authors
* Anthony Tesoriero, B.S. in Computer Science at Rowan University - [Info](http://anttes.com)
* Joseph Salemo
* Joshua Lunsk

## Credits
* All credit for these questions go to [Dr. Nancy Tinkham](http://elvis.rowan.edu/~nlt). Questions are from her class document.
