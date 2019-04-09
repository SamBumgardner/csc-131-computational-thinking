# CSC131: Computational Thinking 
## Homework Assignment # 6 
**Due: TBD** - at the moment, I cannot guarantee that we'll actually end up turning this in, but I can guarantee that working through this short assignment will help you feel more comfortable with C++ and its string operations.

**Objective:** Write a C++ program that reads a user-provided time in a 12-hour format and converts it into 24-hour format military time. 

### Requirements
 * The user-provided time will be in the format `"HH:MM AM"` or `"HH:MM PM"`. 
     * Hours can be one or two digits 
     * Minutes are exactly two digits 
     * AM/PM can be in any mixture of uppercase and lowercase. 
     * For example, `"1:10 am"`, `"12:05 PM"`, and `"12:45 aM"` are valid inputs. 
 * Your program should include a function that takes a string parameter containing the time. 
     * This function should convert the time into a four-digit military time based on a 24-hour clock. 
     * For example, calling this function with an argument of `"1:10 AM"` would output `"0110 hours"`, `"11:30 PM"` would output `"2330 hours"`, `"12:15 AM"` would output `"0015 hours"`, and `"5:05 Pm"` would output `"1705 hours"`. 
     * The function should return a string to be written to the screen by the main function.
 * All output your program displays in the console (including the prompt for user input) should match the example programs below exactly.
     * Don't forget to include an extra space before getting user input (**e.g.** `"Enter time: "` instead of `"Enter time:"`)

Sample program runs are as follows, where user input follows `:`

```
Enter time: 1:10 AM

Corresponding military time is 0110 hours
```
```
Enter time: 11:30 pm

Corresponding military time is 2330 hours
```
```
Enter time: 12:30 AM

Corresponding military time is 0030 hours
```
```
Enter time: 5:35 pm

Corresponding military time is 1735 hours
```
```
Enter time: 5:05 Pm

Corresponding military time is 1705 hours
```

Final instructions / reminders:

 * Please give your program the name `hw6.cpp`. 
 * Use comments to document and explain your code where needed. 
 * **Make sure to upload an electronic copy of your source code in a folder named `HW\hw6` in your CSC 131 TRACE folder**. 
 * Include your name and TRACE folder name at the top of your file in a comment. 
 * For full credit, your program must follow the problem specifications precisely. 
 * A program that does not pass all provided test cases during grading must be fixed and re-submitted to receive a grade. 
 * A program's final grade can be calculated by taking the maximum score (10 points) and subtracting 1 point for grading attempt made against it after the first.
