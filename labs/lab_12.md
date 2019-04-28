# CSC 131 - Computational Thinking
## Lab 12

Write a program that loads sets of grades into a 2-D array, loads a set of student names into a vector, then displays each student's name and grades. 

To make writing this program easier, we will make the following assumptions:
 * This program will always handle exactly data for `5` students.
 * Each student will always have exactly `10` grades.
 * Student names will be stored in a file called `names.txt`
 * Student grades will be stored in a file called `grades.txt`
 * The order of student names and student grades in the files will match - the first 10 grades in `grades.txt` belong to the first student in `names.txt`. 

The `main()` function will be provided for you at the end of this file, so you will only need to implement the program's other functions. A full specification of the program's requirements are listed below.

### Requirements
#### Load Student Names Into Vector
After your `main` function, write a function named `loadNames` that returns a vector of strings and takes the following parameters:
 * A string representing the user-selected file name to open and write to.
 
The function should accomplish the following tasks:
 * Open the file for reading (using the "file name" parameter as the argument to `fopen()`).
     * If the file fails to open, an error message should be displayed and the program should exit with a value of `1`.
 * Create a vector of strings to store student names in.
     * For the sake of the assignment, initialize the vector with size of 0.
 * Using a for loop, read each student name from the file and store it in your student names vector. The structure of your program should probably looks something like this:
     ```c++
     // For students 0 - 4 (should happen a total 5 times), do the following...
         // Read a student name from the file
         // Add student name to the end of the array using push_back()
     ```
 * Close the file after all grades have been read.

Write a prototype for the `loadNames` function before `main` so the program runs without error.

#### Load Grades Into 2-D Array
After your `main` function, write a function named `loadGrades` that **returns nothing** and takes the following parameters:
 * A string representing the user-selected file name to open and read.
 * A 2-D array of integers meant to hold each student's grades.
     * The contents of the array will be uninitialized.
     * The 2-D array contains 5 rows (one for each student) and 10 columns (one for each grade).
         * Remember that the column count must be included in function prototype and header.
     * Remember that arrays are effectively always "passed by reference", so there's no need for an `&` operator here.

The function should accomplish the following tasks:
 * Open the file for reading (using the "file name" parameter as the argument to `fopen()`).
     * If the file fails to open, an error message should be displayed and the program should exit with a value of `1`.
 * Using nested for loops, read each integer from the file and store it in the grades 2-D array. The structure of your program should probably look something like this:
     ```c++
     // For students 0 - 4 (should happen a total 5 times), do the following...
         // For grades 0 - 9 (should happen a total of 10 times), do the following...
             // Read a grade from the file
             // Store the grade in the 2-D array at the correct [student_i][grade_i] position.
     ```
 * Close the file after all grades have been read.

Write a prototype for the `loadGrades` function before `main` so the program runs without error.
    
#### Display Data
After your `main` function, write a function named `displayData` that **returns nothing** and takes the following parameters:
 * A vector of strings that will contain student names.
     * To prevent the computer from copying the vector when passing-by-value, use the reference operator `&` to make the vector pass-by-reference instead.
     * This vector should not be modified within the function, so use the `const` keyword to prevent any accidental changes to it.
 * A 2-D array of integers meant to hold each student's grades.
     * The contents of the array will be uninitialized.
     * The 2-D array contains 5 rows (one for each student) and 10 columns (one for each grade).
         * Remember that the column count must be included in function prototype and header.
     * This array should not be modified within the function, so use the `const` keyword to prevent any accidental changes to it.
 
The function should accomplish the following tasks:
 * Using nested for loops, display each student's name followed by their 10 grades. 
     * When accessing student names from the "student names" vector, use `at()` instead of `[]` to access elements from the array.
     * Student grades should each be separated by a space. See the example output in the "Expected Results" section below.
         * Improvements to formatting (using setw to space the names evenly, adding colon between name and scores, etc) are encouraged, but not required.
     * For extra practice **(not required)** calculate each student's average grade and display it at the end of their line of data.

Write a prototype for the `displayData` function before `main` so the program runs without error.

### Provided Main()
Paste the following `main()` function into your program to test your functions:
 * Note that this function expects that you have already added `#include <iostream>`, `#include <string>`, `#include <vector>`, and `using namespace std;` to your program.
 * You should `#include` other libraries as needed for your other functions.
```c++
int main() {
    cout << "Loading names from "names.txt" now..." << endl << endl;
    vector<int> names = loadNames("names.txt");
    
    cout << "Loading grades from "grades.txt" now..." << endl << endl;
    int grades[5][10];
    loadGrades("grades.txt", grades);
    
    cout << "Here's each student's grade information:" << endl;
    displayData(names, grades);
    
    return 0;
}
```

### Expected Results
If this program is run with `names.txt` containing the following strings:
```
Charlie Emma Johnny Rita Will
These words are after the first 5 names and shouldn't actually be loaded.
```

and `grades.txt` containing the following numbers:
```
69 74 86 68 67 98 95 81 78 76
97 67 86 80 89 78 75 67 81 92
84 84 88 89 69 84 77 100 65 99
94 85 87 89 71 72 98 70 77 97
70 65 81 84 95 89 94 99 75 68
```

Then the output should look like this:
```
Loading names from "names.txt" now...

Loading grades from "grades.txt" now...

Here's each student's grade information:

Charlie 69 74 86 68 67 98 95 81 78 76
Emma 97 67 86 80 89 78 75 67 81 92
Johnny 84 84 88 89 69 84 77 100 65 99
Rita 94 85 87 89 71 72 98 70 77 97
Will 70 65 81 84 95 89 94 99 75 68
```

You may use whatever C++ IDE at home that you like as long as your code works with the C++ 14 standard. During the lab, we will use Code::Blocks or the command line to compile and run the code.

Name your file `lab12.cpp`. Make sure to include your name and the name of your TRACE folder at the top of the file in a multi-line comment. When you are done, demonstrate your code to the instructor and upload an electronic copy of your solution in your CSC131 upload folder in a folder named `LABS\lab12`.
