# Programming-Lanuages-Python
For the python group, fall 2019 Programming Languages class, [Dr. Nancy Tinkham](http://elvis.rowan.edu/~nlt/), at Rowan University.
The purpose of these assignments is to learn a new programming language.

## Assignments
### 1. Beginner's program
###### Status: Complete (9-Oct-19)
Write a program that will read two numbers and will compute the sum of those two numbers. (If you are working in a functional language, you may write a function that takes two numbers as input parameters and returns the sum of the two numbers.)

### 2. Simple repetition
###### Status: Complete (9-Oct-19)
Write a program that will read a sequence of numbers and will compute the sum of those numbers.

Note: If your language supports lists, your input can be a list (e.g., [10, 6, 2, 8, 12]). Otherwise, have the user enter a special value to indicate the end of the input, or ask the user at the beginning of the program how many numbers will be entered. Be prepared to handle any nonnegative quantity of numbers.

### 3. Floating-point calculation
###### Status: Complete (9-Oct-19)
Write a program to read a positive integer N and print out the sum of the first N terms of the alternating harmonic series.

The alternating harmonic series is

1 - 1/2 + 1/3 - 1/4 + 1/5 - ...
For example, if N = 3, then the sum is 1 - 1/2 + 1/3 = 0.83333
If the user enters a negative value for N, print an error message or return an error value instead of attempting to compute the sum of the series. 

### 4. Text file format conversion
###### Status: Complete (9-Oct-19)
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
###### Status: In progress
Two agents are exploring a 9x9 grid of square rooms:
```
 	1	2	3
 	4	5	6
 	7	8	9
```
You can think of the agents as human or robotic explorers who are moving through the rooms looking for treasures. Each square is connected to the adjacent squares above, below, and next to it; for example, square 2 is connected to squares 1, 5, and 3. There are no diagonal connections. Agent 1 starts at square 1, and agent 2 starts at square 9. The goal is for all of the treasures to have been found by one of the two agents. (Typically, some of the treasures will be found by agent 1 and some by agent 2, although this may vary from one run to the next.) The two agents should work concurrently, using two different search strategies for exploring the maze. (For example, one strategy might be to go north if that's possible, then east as a second choice, south as a third choice, and west as a fourth choice. Another might be to choose a random direction at each step.) As soon as all the treasures have been found, both agents should stop looking for treasures.
There are four treasures: an emerald, a crown, a coin, and a rare book. At the beginning of the game, place the four treasures into four different rooms in the maze. As each treasure is found, the program should print which treasure was found, and which agent found it. This will give the user a sense of the progress of the search. At the end, the program should inform the user that the search has been successful and that all the treasures have been found.

(If you are working in a language in which conventional output is difficult, you may accumulate the information about treasure-finding in a list or similar data structure, and then return or display this list at the end of the program run.)

### 6. Semester homework problem
###### Status: Not started
Solve the semester homework problem (that is, the problem you've solved in Scheme, Ada, and Prolog) in your chosen language. If needed, you may adapt the input/output format of the problem to fit your language. For example, you may use conventional input/output, or you may write a function that takes the "input" as its parameters and returns the "output" value, or you may use a web-based interface.

## Built with
* [Python](https://www.python.org) - Programming language
* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Enscript](https://medium.com/@tashian/print-out-your-code-on-paper-7c760a376bca) - Printing out code efficiently

## Authors
* Anthony Tesoriero, B.S. in Computer Science at Rowan University - [Info](http://anttes.com)
* Joseph Salemo
* Joshua Lunsk

## Credits
* All credit for these questions go to [Dr. Nancy Tinkham](http://elvis.rowan.edu/~nlt). Questions are from her class document.
