# CSC 131 - Computational Thinking
## Homework Assignment # 1
**Due: Beginning of class on Friday, January 23, 2018.**

The Lo Shu Magic Square is a 3 by 3 grid with the following properties:

 * The grid contains the numbers 1 through 9 where each number appears exactly once in the grid.
 * The sum of each row, each column, and each diagonal all add up to the same number, 15.
 An example of a  Lo Shu Magic Square is as follows: 

![Example Magic Square](/assignments/assignment_1/magic_square1.jpg)

 Remark: Image adopted from http://en.wikipedia.org/wiki/Magic_square

In a program, you can simulate a magic square by using a two-dimensional list. Write a Python program that tests whether or not a 3 by 3 grid is a valid magic square. The program reads the input from a text file named input.txt. Each line in the file contains exactly 9 numbers that correspond to the values in a possible magic square. The first three numbers correspond to the values in the first row, the next three values correspond to the second row, and the last three values correspond to the last row. For example, the above magic square would appear in the file as the line `4 3 8 9 5 1 2 7 6`. Sample input file is as follows:
```
4 3 8 9 5 1 2 7 6
8 3 4 1 5 9 6 7 2
6 1 8 7 5 3 2 9 4
6 9 8 7 5 3 2 1 4
6 1 8 7 5 3 2 1 4
6 1 3 2 9 4 8 7 5
5 5 5 5 5 5 5 5 5
```

The output from the program is the word valid if the corresponding grid is a valid magic square and the word invalid if it is not. Sample program run using the above input file is as follows:

```
valid
valid
valid
invalid
invalid
invalid
invalid
```
Notice that a different input file with a different number of lines may be used to test your code. All your code must be written inside functions. Make sure to use loops where needed instead of writing many additions. Please give your program the name `hw1.py`. Use comments to document and explain your code where needed. To be graded, you **MUST** upload an electronic copy of your source code in a folder called HW\hw1\ in your CSC 131 TRACE folder. It is always a good idea to make sure that your code runs correctly from inside your TRACE folder. 

Assignment originally written by Dr. Saquer. See https://courses.missouristate.edu/jamilsaquer/
