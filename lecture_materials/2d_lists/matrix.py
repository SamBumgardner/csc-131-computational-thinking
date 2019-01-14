"""
Class: CSC 131
Author: Jamil Saquer
File name: matrix.py
A program that works with 2D lists
"""

import random

def assignValues(matrix):
    """assign random integers between 1 and 1000 to
    the elements in the 2D list matrix""" 
    for rowIndex in range(len(matrix)):
        for columnIndex in range(len(matrix[rowIndex])):
            matrix[rowIndex][columnIndex] = random.randint(1, 1000)

def display(matrix):
    """display the values in a 2D list row by row"""
    for row in matrix:
        for value in row:
            print(value, end =" ")
        print() #move cursor to next line

def findLargest(m):
    """A function that finds and returns the largest value in a 2D list"""
    largest = m[0][0]
    for rowIndex in range(len(m)):
        for columnIndex in range(len(m[rowIndex])):
            if m[rowIndex][columnIndex] > largest:
                largest = m[rowIndex][columnIndex]
    return largest
        
def main():
    rows = 10
    columns = 10
    #cretae a 2D list where all values are initially 0
    m = []
    for row in range(rows):
        m.append([0] * columns)

    display(m)
    #assign random values to the elements
    assignValues(m)
    print("\nThe list after assiging random values to the elements\n")
    display(m)

    largest = findLargest(m)
    print("\nThe largest value is ", largest)

main()

