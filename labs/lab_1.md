# CSC 131 - Computation Thinking
## Lab 1

For this lab, you will work with two-dimensional lists in Python. Do the following:

 1. Write a function that returns the sum of all the elements in a specified column in a matrix using the following header:
    ```python
    def sumColumn(matrix, columnIndex):
    ```
 
 2. Write a function display() that displays the elements in a matrix row by row, where the values in each row are displayed on a separate line. Use a single space to separate different values. Sample output from this function when it is called on a 3 X 4 matrix is as follows:
    ```python
    2.5 3.0 4.0 1.5
    1.5 4.0 2.0 7.5
    3.5 1.0 1.0 2.5
    ```
	
 3. Given this partial code 
    ```python
    def getMatrix(numRows, numColumns):
        '''returns a matrix with the specified number of rows and columns'''
        m = [] # the 2D list (i.e., matrix), initially empty
        for row in range(numRows):
            matrix_dimensions_string = str(numRows) + "-by-" + str(numColumns)
            line = input("Enter a " + matrix_dimensions_string + " matrix row for row " + str(row) + ": ")


        return m
    ```
	write a function called getMatrix(numRows, numColumns) that returns a matrix with numRows rows and numColumns columns. The function  reads the values of the matrix from the user on a row by row basis. The values of each row must be entered on one line using a space to separate the values. Use loops in your solution. A sample run of this function when it is caled as getMatrix(3, 4) to return a 3 by 4 matrix is as follows. The numbers after the colon are entered by the user:

    ``` python
    Enter a 3-by-4 matrix row for row 0: 2.5 3 4 1.5
    Enter a 3-by-4 matrix row for row 1: 1.5 4 2 7.5
    Enter a 3-by-4 matrix row for row 2: 3.5 1 1 2.5
    ```


Use the following function to test your code:

```python
def main():
    m = getMatrix(3, 4)
    print("\nThe matrix is")
    display(m)

    print()
    for col in range(len(m[0])):
        print("Sum of elements for column %d is %.2f" % (col, sumColumn(m,col)))

main()
```

A sample program run is as follows:

```
Enter a 3-by-4 matrix row for row 0: 1 22 3.7869 8
Enter a 3-by-4 matrix row for row 1: 4 5.6543 3 3
Enter a 3-by-4 matrix row for row 2: 1 1 1 1

The matrix is
1.0 22.0 3.7869 8.0 
4.0 5.6543 3.0 3.0 
1.0 1.0 1.0 1.0 

Sum of elements for column 0 is 6.00
Sum of elements for column 1 is 28.65
Sum of elements for column 2 is 7.79
Sum of elements for column 3 is 12.00
```

The format of the input and output of your program must be as in the sample run. When you are done, demonstrate your code to the instructor and upload your solution to your CSC131 upload folder in a folder called LABS. Please name your file `lab1.py`.

Lab originally written by Dr. Saquer. See courses.missouristate.edu/JamilSaquer