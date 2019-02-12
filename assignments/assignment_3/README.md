# CSC131: Computational Thinking 
## Homework Assignment # 3 
**Due: TBD**

Python has the complex class for performing complex number arithmetic. For this assignment, you will design and implement your own Complex class. Note that the complex class in Python is named in lowercase, while our custom Complex class is named with C in uppercase.

A complex number is of the form `a + bi`, where `a` and `b` are real numbers and `i` is the square root of -1. The numbers `a` and `b` are known as the real part and the imaginary part of the complex number, respectively. You can perform addition, subtraction, multiplication, and division for complex numbers using the following formulas:

```
(a + bi) + (c + di) = (a + c) + (b + d)i 
(a + bi) - (c + di) = (a - c) + (b - d)i 
(a + bi) * (c + di) = (ac - bd) + (bc + ad)i 
(a + bi) / (c + di) = (ac + bd) / (c^2 + d^2) + (bc - ad)i / (c^2 + d^2) 
```

You can also obtain the absolute value (or length) of a complex number using the formula:

```
|a + bi| = sqrt(a^2 + b^2)
```

**Note:** the above equations are for mathematical reference **only**, and should **not** be treated as something you can insert directly into code.

Implement a class named `Complex` for representing complex numbers with methods `__add__`, `__sub__`, `__mul__`, `__truediv__`, and `__abs__` for performing complex-number operations using `+`, `-`, `*`, `/`, and `abs()`. 

**Important Instructions:** 
 * In python 3, `__truediv__` is used to override `/` and `__floordiv__` is used to override `//`. 
 * The `__abs__(self)` special method is used to override the absolute value function; this will allow you to write `abs(c)`, where `c` is an object of the class `Complex`. 
 * Implement the comparison methods `__eq__`,  `__ne__`, `__lt__`, ...etc.  to compare two `Complex` numbers based on their length. 
 * For the purpose of this assignment, assume that `Complex` numbers are compared based on the values of their lengths. So, for two `Complex` numbers `c1` and `c2`, `c1` is less than `c2`, if and only if `abs(c1) < abs(c2)`. Similarly `c1` equals `c2` if and only if `abs(c1)` equals `abs(c2)`. 
 * The methods `__eq__` and  `__ne__` should **also** allow you to compare a `Complex` number **with objects of other types** for equality and inequality, respectively.
 * Provide a constructor `__init__(self, a = 0, b = 0)` to create a complex number `a + bi` with the default values `0` and `0` for `a` and `b`. 
 * Your `__str__` method returns the `Complex` number as a string of the form `(a, bi)` (it should look as in the sample output below.) If `b` is `0`, it simply returns `a` **without parentheses**. Likewise if `a` is `0`, it returns `bi`. If both `a` and `b` are `0`, it returns the string `0`. So, the parentheses will be part of the string representation only when both `a` and `b` are not `0`.

Use the following main function to test your code **copy and paste after the code of the class**.

```python
def main():
    input_line = input("Enter the first complex number: ")
    input_line = list(map(float,input_line.split()))
    a, b = input_line[0], input_line[1]
    c1 = Complex(a, b)
    input_line = input("Enter the second complex number: ")
    input_line = list(map(float,input_line.split()))
    a, b = input_line[0], input_line[1]
    c2 = Complex(a, b)
    
    print()
    print("c1 is", c1)
    print("c2 is", c2)
    print("|" + str(c1) + "| = " + str(abs(c1)))
    print("|" + str(c2) + "| = " + str(abs(c2)))

    print(c1, " + ", c2, " = ", c1 + c2)
    print(c1, " - ", c2, " = ", c1 - c2)
    print(c1, " * ", c2, " = ", c1 * c2)
    print(c1, " / ", c2, " = ", c1 / c2)

    print("Is c1 < c2?", c1 < c2)
    print("Is c1 <= c2?", c1 <= c2)
    print("Is c1 > c2?", c1 > c2)
    print("Is c1 >= c2?", c1 >= c2)
    print("Is c1 == c2?", c1 == c2)
    print("Is c1 != c2?", c1 != c2)
    print("Is c1 == 'Hello There'?", c1 == 'Hello There')
    print("Is c1 != 'Hello There'?", c1 != 'Hello There')
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
```

The function prompts the user to enter two `Complex` numbers. The input should be provided as two numbers separated by a space. The program displays the two complex numbers, their absolute values, the result of their addition, subtraction, multiplication, and division. It also displays the result of comparing the two Complex numbers using the different comparison operators.

The output from your program must be similar to and use the same format as the following sample output, where input from the user is shown in red:

```
>>> main()
Enter the first complex number: 2.5 4.5
Enter the second complex number: -2.5 11.2

c1 is (2.5, 4.5i)
c2 is (-2.5, 11.2i)
|(2.5, 4.5i)| = 5.1478150704935
|(-2.5, 11.2i)| = 11.475626344561764
(2.5, 4.5i) + (-2.5, 11.2i) = 15.7i
(2.5, 4.5i) - (-2.5, 11.2i) = (5.0, -6.699999999999999i)
(2.5, 4.5i) * (-2.5, 11.2i) = (-56.65, 16.75i)
(2.5, 4.5i) / (-2.5, 11.2i) = (0.335257043055661, -0.2980484471106386i)
Is c1 < c2? True
Is c1 <= c2? True
Is c1 > c2? False
Is c1 >= c2? False
Is c1 == c2? False
Is c1 != c2? True
Is c1 == 'Hello There'? False
Is c1 != 'Hello There'? True
>>> main()
Enter the first complex number: 3 4
Enter the second complex number: 2 -4

c1 is (3.0, 4.0i)
c2 is (2.0, -4.0i)
|(3.0, 4.0i)| = 5.0
|(2.0, -4.0i)| = 4.47213595499958
(3.0, 4.0i) + (2.0, -4.0i) = 5.0
(3.0, 4.0i) - (2.0, -4.0i) = (1.0, 8.0i)
(3.0, 4.0i) * (2.0, -4.0i) = (22.0, -4.0i)
(3.0, 4.0i) / (2.0, -4.0i) = (-0.5, 1.0i)
Is c1 < c2? False
Is c1 <= c2? False
Is c1 > c2? True
Is c1 >= c2? True
Is c1 == c2? False
Is c1 != c2? True
Is c1 == 'Hello There'? False
Is c1 != 'Hello There'? True
>>> main()
Enter the first complex number: 3.5 -2.5
Enter the second complex number: -3.5 2.5

c1 is (3.5, -2.5i)
c2 is (-3.5, 2.5i)
|(3.5, -2.5i)| = 4.301162633521313
|(-3.5, 2.5i)| = 4.301162633521313
(3.5, -2.5i) + (-3.5, 2.5i) = 0
(3.5, -2.5i) - (-3.5, 2.5i) = (7.0, -5.0i)
(3.5, -2.5i) * (-3.5, 2.5i) = (-6.0, 17.5i)
(3.5, -2.5i) / (-3.5, 2.5i) = -1.0
Is c1 < c2? False
Is c1 <= c2? True
Is c1 > c2? False
Is c1 >= c2? True
Is c1 == c2? True
Is c1 != c2? False
Is c1 == 'Hello There'? False
Is c1 != 'Hello There'? True
>>> 
```

Final instructions / reminders:

 * Please give your program the name `hw3.py`. 
 * Please make sure to write your code in functions. No code should be written outside of functions. 
 * Use comments to document and explain your code where needed. 
 * **Make sure to upload an electronic copy of your source code in a folder named `HW\hw3` in your CSC 131 TRACE folder**. 
 * Include your name and TRACE folder name at the top of your file in a comment. 
 * For full credit, your program must follow the problem specifications precisely. 
 * A program that does not pass all provided test cases during grading must be fixed and re-submitted to receive a grade. 
 * A program's final grade can be calculated by taking the maximum score (10 points) and subtracting 1 point for grading attempt made against it after the first.
