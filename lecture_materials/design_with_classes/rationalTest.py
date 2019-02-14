'''
Author: Jamil Saquer
date: 2/5/2015
The purpose of this file is to test the rational class and some of its methods
'''

from rational import Rational
from student import Student

def main():
    oneFifth = Rational(2, 10)
    print("The first rational number is:", oneFifth)
    twoThirds = Rational(2, 3)
    print("The second rational number is:", twoThirds)
    print(oneFifth, "+", twoThirds, "=", oneFifth + twoThirds)

    print("\nTesting the overloaded comparison operators")
    print("Is oneFifth == twoThirds?", oneFifth == twoThirds)
    print("Is oneFifth != twoThirds?", oneFifth != twoThirds)
    print("Is oneFifth < twoThirds?", oneFifth < twoThirds)
    print("Is oneFifth <= twoThirds?", oneFifth <= twoThirds)
    print("Is oneFifth > twoThirds?", oneFifth > twoThirds)
    print("Is oneFifth >= twoThirds?", oneFifth >= twoThirds)

    print("\nComparing a fraction with an object of a different type, say a Student")
    s = Student("Mark", 3)
    print("Is oneFifth == s?", oneFifth == s)
    print("Is oneFifth != s?", oneFifth != s)


main()
