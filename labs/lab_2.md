# CSC 131 - Computation Thinking
## Lab 2

The purpose of this lab is to practice working with Python's higher order functions and ternary operator. Write all of your code in one file named lab2.py. You can write the code for items 1 through 6 directly inside the main function. 

Let `numbers` be the list of values produced by `list(range(1, 11))`.


 1. [1 point] Using the `map` function and a `lambda` argument, write an expression that produces a list of the cubes of the values in `numbers`. Assign the result to a variable called `map_result` and print `map_result`.
 
 2. [1 point] Using the `filter` function and a `lambda` argument, write an expression that produces a list of the values in `numbers` that are divisible by 3. Assign the result to a variable called `filter_result` and print `filter_result`.

 3. [1 point] Using the `reduce` function and a `lambda` argument, write an expression that returns the result of concatenating all the digits in `numbers`. Assign the result to a variable called `reduce_result` and print `reduce_result`. The output from this step is the string `'12345678910'`

 4. [1 point] Use a list comprehension to produce the same list as in question 1 (i.e., the new list will contain the cubes of the values in a).

 5. [1 point] Use a list comprehension to produce the same list as in question 2.

 6. [1 point] Use a list comprehension to produce a list containing the cubes of the values in `numbers` that are divisible by 3. The output from this step is the list `[27, 216, 729]`

 7. [2 points] Write a function named `evenFilter` (outside of `main`) that takes as an argument a dictionary of elements indexed by integer keys. Using only a list comprehension, return a list of the values of the elements associated with the keys that are evenly divisible by 2. For example,
    ```python
	>>> data = {1: "one", 3: "three", 4: "four", 5: "five", 8: "eight", 10: "ten"}
    >>> print(evenFilter(data))
    ['four', 'eight', 'ten']
    ```
    add this code (creating the `data` dictionary and printing the result of `evenFilter`) to your `main` function to test your code.

 8. [2 points] Write a function named `findMin(num1, num2)` **that uses the ternary operator** (i.e, conditional expression) to find and return the minimum of its two arguments. Assume that num1 and num2 are numbers. Add code to main to test this function.

Name your file `lab2.py`. Make sure to include your name and the name of your TRACE folder at the top of the file in a docstring. When you are done, demonstrate your code to the instructor and upload your solution in your CSC131 upload folder in a folder called `LABS\lab2`.
 
Lab originally written by Dr. Saquer. See courses.missouristate.edu/JamilSaquer