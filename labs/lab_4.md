# CSC 131 - Computational Thinking
## Lab 4

Write the code for a class named `Point` to represent a point in the Cartesian plane with x and y coordinates. The class contains:
 * Two instance variables named `x` and `y` that represent the coordinates with `getX()` and `getY()` methods.
 * A constructor that constructs a point with specified coordinates, or with default values `0` and `0`.
 * An `__str__` method to return a string representation in the form `(x, y)`.
 * A method named `distance` that returns the distance from this point to another point. The formula for finding the distance between the two points (x1,y1) and (x2, y2) is `math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)`
 * A method named `originDistance` that returns the distance from this point to the point of origin (0,0).
 * Additional code so that points can be compared using the comparison operators. Points are compared based on their distance from the origin.
     * **Note:** Your code should allow using `==` and `!=` to compare a `Point` object with an object of a different type.

Add test code that does the following:
 * Creates a `Point` object, named `p0`, that uses the default values for the coordinates.
 * Print `p0`
 * Creates a `Point` object, named `p1`, with coordinates at (3,4)
 * Print `p1`
 * Creates a `Point` object, named `p2`, with coordinates at (3,0). When creating the object, take advantage of the fact that the value of the y-ccordinate is the default value of the corresponding parameter. 
 * Print the X and Y coordinates of `p2` using the `getX()` and `getY()` methods
 * Find and print the distance between `p1` and `p2`
 * Print the results of comparing `p1` and `p2`. Make sure to test all 6 comparison operators.
 * Print the result of using the equality and inequality operators to compare `p1` with the string `"Hello"`.

Name your file `lab4.py`. Make sure to include your name and the name of your TRACE folder at the top of the file in a docstring. When you are done, demonstrate your code to the instructor and upload your solution in your CSC131 upload folder in a folder called `LABS\lab4`.
