# CSC 131 - Computational Thinking
## Lab 9

Write a C++ program that asks the user to enter an item's description (see sample program runs below for examples). The program then asks for the item's wholesale cost and its markup percentage. It should then display the item's retail price. For example, if an item's wholesale cost is `5.00` and its markup percentage is `50`%, then the item's retail price is calculated as `5.0 * 1.5`, which results in a final price of `7.50`.

Your program should have a function named `calculateRetail` that receives the wholesale cost and the markup percentage as arguments and returns the retail price of the item.

Sample program runs are as follows, where all text after each `:` is input from the user:
```
Enter item description: gallon of milk
You entered gallon of milk
Enter item wholesale cost: 1.5
You entered 1.5
Enter item markup percentage: 150
You entered 150

Retail price for gallon of milk is 3.75
```
```
Enter item description: pair of shoes
You entered pair of shoes
Enter item wholesale cost: 60
You entered 60
Enter item markup percentage: 62.50
You entered 62.5

Retail price for pair of shoes is 97.5
```
```
Enter item description: bicycle
You entered bicycle
Enter item wholesale cost: 80
You entered 80
Enter item markup percentage: 75
You entered 75

Retail price for bicycle is 140
```
Notice that whenever the program reads input from the user, it displays that input back to the user. Make sure that your program does the same.

You may use whatever C++ IDE at home that you like as long as your code works with the C++ 14 standard. During the lab, we will use Code::Blocks or the command line to compile and run the code.

Name your file `lab9.cpp`. Make sure to include your name and the name of your TRACE folder at the top of the file in a multi-line comment. When you are done, demonstrate your code to the instructor and upload an electronic copy of your solution in your CSC131 upload folder in a folder named `LABS\lab9`.
