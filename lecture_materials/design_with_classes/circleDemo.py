"""
circleDemo.py
The purpose of this file is to test and use the Circle class
"""

from circle import Circle

def main():
    circle1 = Circle(5)
    print(circle1)
    print("The area of circle1 is %0.2f" % circle1.getArea())
    print("The circumference of circle1 is %0.2f" % circle1.getCircumference())

    circle2 = Circle(10)
    print()
    print(circle2)
    print("The area of circle2 is %0.2f" % circle2.getArea())
    print("The circumference of circle2 is %0.2f" % circle2.getCircumference())

    circle3 = Circle()
    print()
    print(circle3)
    print("The area of circle3 is %0.2f" % circle3.getArea())
    print("The circumference of circle3 is %0.2f" % circle3.getCircumference())

main()

    



    
