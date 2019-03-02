# CSC131: Computational Thinking 
## Homework Assignment # 4
**Due: Monday, March 11th** - Yeah, this is during spring break. If you'd rather not have homework due during spring break, just pretend like it's due on the Friday before.

**Note:** Due to the random nature of this program, this homework assignment will be graded manually, and thus we will **NOT** allow multiple attempts. Instead, the program will be graded once for some score out of 10 points.

A common memory matching game played by young children is to start with a deck of cards that contains identical pairs. For example, given six cards in the deck, two might be labeled 1, two labeled 2 and two labeled 3. The cards are shuffled and placed face down on a board. A player then selects two cards that are face down, turns them face up, and if the cards match they are left face up. If the two cards do not match, they  are returned to their original face down position. The game continues until all cards are face up.

Write a program that plays the memory matching game. When it starts, the program prompts the user for the number of rows and columns for the game board that contains the cards. The total number of cards must be even. Assume that the board dimensions are at most 8 by 9 or 9 by 8. Your cards must be numbered from 1 through (number of rows * number of columns) / / 2. Your program allows the player to specify the cards that she would like to select through a coordinate system as shown in the sample program run below. All the cards that are face down are indicated by *. For example, in the following layout of a 4 by 4 game board

```
     1   2   3   4
    _______________
1  | 8   *   *   *
   |
2  | *   *   *   *
   |
3  | *   8   *   *
   |
4  | *   *   *   *
```

the pair of 8 which are face up are at coordinates (1,1) and (3,2). Pay attention to how the coordinates are specified: row number followed by column number, **both start at index 1**, not zero. A sample run of the game is as follows:

```
>>> main()
Enter number of rows 3
Enter number of columns 2
* *
* *
* *
Enter coordinates for first card 1 1
Enter coordinates for second card 3 1
Not an identical pair. Found 2 at (1,1) and 1 at (3,1)
* *
* *
* *
Enter coordinates for first card 1 2
Enter coordinates for second card 2 2
Not an identical pair. Found 2 at (1,2) and 3 at (2,2)
* *
* *
* *
Enter coordinates for first card 1 1
Enter coordinates for second card 1 2
2 2
* *
* *
Enter coordinates for first card 3 1
Enter coordinates for second card 3 2
Not an identical pair. Found 1 at (3,1) and 3 at (3,2)
2 2
* *
* *
Enter coordinates for first card 2 1
Enter coordinates for second card 3 1
2 2
1 *
1 *
Enter coordinates for first card 3 2
Enter coordinates for second card 2 2
2 2
1 3
1 3
>>> 
Another sample run is as follows:
>>> main()
Enter number of rows 3
Enter number of columns 3
***The value of rows X columns must be even. Try again.***
Enter number of rows 2
Enter number of columns 3
* * *
* * *
Enter coordinates for first card 3 1
***Invalid coordinates! Try again.***
Enter coordinates for first card 1 3
Enter coordinates for second card 2 3
* * 1
* * 1
Enter coordinates for first card 1 1
Enter coordinates for second card 2 1
2 * 1
2 * 1
Enter coordinates for first card 1 2
Enter coordinates for second card 2 2
2 3 1
2 3 1
>>> 
A third sample run is as follows:
>>> main()
Enter number of rows 2
Enter number of columns 2
* *
* *
Enter coordinates for first card 1 1
Enter coordinates for second card 2 2
Not an identical pair. Found 1 at (1,1) and 2 at (2,2)
* *
* *
Enter coordinates for first card 1 1
Enter coordinates for second card 2 1
Not an identical pair. Found 1 at (1,1) and 2 at (2,1)
* *
* *
Enter coordinates for first card 2 1
Enter coordinates for second card 2 2
* *
2 2
Enter coordinates for first card 1 1
Enter coordinates for second card 1 2
1 1
2 2
>>> 
```

Design Requirements: You need to use three classes: `Card`, `Deck` and `Game`. 

`Card` stores both the card's value and face (a string or Boolean variable to indicate whether the card is facing up or down). 

`Deck` contains the cards needed for the game. It will contain among its methods a method to deal a card, another for shuffling the deck, and a method that returns number of cards left in the deck. These two classes are not identical to the classes `Card` and `Deck` discussed in the book but are very similar. 

The class `Game` simulates playing a single game and represents the interaction between the user and the other classes. Its instance members store a 2D list (of card objects) representing the game board where the cards are placed, number of rows and number of columns of the game board. Among the instance methods of the `Game` class:  `play()`, which simulates playing the game; `isGameOver()`, which checks whether or not the game is over; `displayBoard()`, which displays the board; `populateBoard()`, which creates the initial 2D list of identical pairs of cards with all the cards facing down. Most probably, you will need to write other instance methods as you see appropriate.    

Use the following test program:

```python
def main():
    while True:
        # Force user to enter valid value for number of rows
        while True:
            rows = input("Enter number of rows ")
            if rows.isdigit() and ( 1 <= int(rows) <= 9):
                rows = int(rows)
                break
            else:
                print ("    ***Number of rows must be between 1 and 9! Try again.***")
                # Adding *** and indenting error message makes it easier for the user to see

        # Force user to enter valid value for number of columns
        while True:
            columns = input("Enter number of columns ")
            if columns.isdigit() and ( 1 <= int(columns) <= 9):
                columns = int(columns)
                break
            else:
                print ("    ***Number of columns must be between 1 and 9! Try again.***")

        if rows * columns % 2 == 0:
            break
        else:
            print ("    ***The value of rows X columns must be even. Try again.***")

    game = Game(rows, columns)
    game.play()

if __name__ == "__main__":
    main()
```

The format of the output and input of your program must be the same as what is shown in the sample runs above. 
Please give your program the name `hw4.py`. Use comments to document and explain your code where needed. Make sure to upload an electronic copy of your source code in a folder called `HW\hw4` in your CSC 131 TRACE folder. No grade above 6 will be given for a program that does not run.
