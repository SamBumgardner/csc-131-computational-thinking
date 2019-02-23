# CSC 131 - Computational Thinking
## Lab 5

Download and study the class [`GeometricObject`](./geometricObject.py). Save the class in a file named `geometricObject.py`. 

Write the code for a class named `Circle` that extends the `GeometricObject` class. The `Circle` class contains:
 * An instance variable `radius` that represents the radius of the `Circle`.
 * An initializer that creates a circle with specified `radius`, `color`, and `filled`. Use default values `1.0` for `radius`, `"white"` for `color`, and `True` for `filled`. Notice that the instance variables for `color` and `filled` are inherited from the superclass. Also remember that, in Python, every class is responsible for initializing the instance variables defined in it.
 * A method named `getArea()` that returns the area of this `Circle`.
 * A method named `getPerimeter()` that returns the perimeter of this `Circle`.
 * An `__str__` method to return a string representation of the form `"Circle: radius = 3 color: red and filled: True"`. (assume that `3`, `red`, and `True` are the values for the corresponding instance variables of the `Circle` object on whose behalf the method was called.) This `__str__` method should append the string representation returned from `GeometricObject.__str__(self)` to get the part of the message that says `"color: red and filled: True"`.

Write the code for a class named `Triangle` that extends the `GeometricObject` class. The `Triangle` class contains:
 * Instance variables `side1`, `side2`, and `side3` that denote the three sides of the `Triangle`.
 * An initializer that creates a triangle with specified `side1`, `side2`, `side3`, `color`, and `filled`. Use default values `1.0` for the sides, `"white"` for color, and `True` for filled. Notice that the instance variables for `color` and `filled` are inherited from the superclass.
 * A method named `getArea()` that returns the area of this triangle. The formula for computing the area of a triangle is:
   ```python
   s = (side1 + side2 + side3) / 2
   area = sqrt(s(s - side1)(s - side2)(s - side3))
   ```
 * A method named `getPerimeter()` that returns the perimeter of this triangle .
 * An `__str__` method to return a string representation of the form `"Triangle: side1 = 3 side2 = 4 side3 = 5 color: blue and filled: True"`. (assume that `3`, `4`, `5`, `blue`, and `True` are the values for the corresponding instance variables of the `Triangle` object on whose behalf the method was called.)

Add a test program to test your `Circle` and `Triangle` classes and some of the methods inherited from the class `GeometricObject`. A sample main program is as follows:

```python
def main():
    #Testing Circle class
    c = Circle(5, "blue", False)
    print(c)
    print()
    
    print("Entering input values for a circle")
    r = float(input('Enter value for radius: '))

    c1 = Circle(r)
    
    print(c1)
    print("%.2f" % c1.getArea())
    print("%.2f" % c1.getPerimeter())
    print(c1.getColor())
    print(c1.isFilled())

    #Testing Triangle class
    print("\nEntering input values for a triangle")
    s1 = float(input('Enter value for side1: '))
    s2 = float(input('Enter value for side2: '))
    s3 = float(input('Enter value for side3: '))
    color = input('Enter color of the triangle: ')
    filled = input('Is the triangle filled (1/0)? ')
    filled = (filled == "1")
    t1 = Triangle(s1, s2, s3, color, filled)

    print(t1)
    print("%.2f" % t1.getArea())
    print("%.2f" % t1.getPerimeter())
    print(t1.getColor())
    print(t1.isFilled())
 ```
 
Place the code for the `Circle` class, `Triangle` class, and the main program in one file named `lab5.py`. Make sure to include your name and the name of your TRACE folder at the top of the file in a docstring. When you are done, demonstrate your code to the instructor and upload your solution in your CSC131 upload folder in a folder called `LABS\lab5`. Also, place a copy of `geometricObject.py` in this folder.
