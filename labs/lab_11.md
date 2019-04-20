# CSC 131 - Computational Thinking
## Lab 11

Write a program that reads a user-selected file of integers, then writes all even numbers found in the file to `evenFile.txt` and writes all odd numbers to `oddFile.txt`. The `main()` function will be provided for you at the end of this file, so you will only need to implement the program's other functions. A full specification of the program's requirements are listed below.

### Requirements
#### Read and Sort Integers
After your `main` function, write a function named `readAndSort` that **returns nothing** and takes the following parameters:
 * A string representing the user-selected file name to open and read.
 * An array of integers meant to hold even numbers.
     * The contents of the array will be uninitialized.
     * The array size will be reasonably large - there's no need to worry about going out-of-bounds with our example files.
     * Remember that arrays are effectively always "passed by reference", so there's no need for an & operator here.
 * An integer **passed by reference** to track how many `even` numbers were found in the user-selected file.
     * You can assume its initial value will be 0.
     * You will change its value during the function to track how many even numbers were read from the file.
 * An array of integers meant to hold odd numbers.
     * The contents of the array will be uninitialized.
     * The array size will be reasonably large - there's no need to worry about going out-of-bounds with our example files.
     * Remember that arrays are effectively always "passed by reference", so there's no need for an & operator here.
 * An integer **passed by reference** to track how many `odd` numbers were found in the user-selected file.
     * You can assume its initial value will be 0.
     * You will change its value during the function to track how many odd numbers were read from the file.

The function should accomplish the following tasks:
 * Open the file for reading (using the "file name" parameter as the argument to `fopen()`).
     * If the file fails to open, an error message should be displayed and the program should exit with a value of `1`.
 * Using a `while` loop, read each integer from the file. The following steps need to be done for each integer:
     * If the integer is even, do the following:
         * Store the integer in the next unused spot in your "even array" parameter.
         * Increase the "even numbers read" parameter by one.
     * If the integer is odd, do the following:
         * Store the integer in the next unused spot in your "odd array" parameter.
         * Increase the "odd numbers read" parameter by one.
 * Close the file after all numbers have been read.

Write a prototype for the `readAndSort` function before `main` so the program runs without error.


#### Write Numbers to a File
After your `main` function, write a function named `writeNumbersToFile` that **returns nothing** and takes the following parameters:
 * A string representing the user-selected file name to open and write to.
 * An array of integers to write to the file. 
     * This array should not be modified within the function, so use the `const` keyword to prevent any accidental changes to it.
 * An integer representing the number of integers that are contained inside the array.
 
The function should accomplish the following tasks:
 * Open the file for writing (using the "file name" parameter as the argument to `fopen()`).
 * Using a `for` loop, write each integer in the array to the file. 
     * Use the "number of integers in the array" parameter to test if the `for` loop is complete or not.
     * **Note:** Each integer should be on its own line.
 * Close the file after all numbers have been written.

Write a prototype for the `writeNumbersToFile` function before `main` so the program runs without error.
    
### Provided Main()
Paste the following `main()` function into your program to test your functions:
 * Note that this function expects that you have already added `#include <iostream>`, `#include <string>` and `using namespace std;` to your program.
 * You should `#include` other libraries as needed for your other functions.
```c++
int main() {
    string fileName;
    
    cout << "Please enter the name of the file to sort: ";
    cin >> fileName;
    
    int evenNumbers[100], evenCount = 0, oddNumbers[100], oddCount = 0;
    readAndSort(fileName, evenNumbers, evenCount, oddNumbers, oddCount);
    
    writeNumbersToFile("evenFile.txt", evenNumbers, evenCount);
    cout << "Wrote even numbers to \"evenFile.txt\"." << endl;
    
    writeNumbersToFile("oddFile.txt", oddNumbers, oddCount);
    cout << "Wrote even numbers to \"oddFile.txt\"." << endl;
    
    return 0;
}
```

### Expected Results
If this program is run on an input file containing the following numbers:
```
123 456 111 222
333 444 555 777 888
999 000 111 222 333
444 974 123 426 123 

1 2 3 4 5 6 7 8 9

12 32 42 55 75 64 32
```

Then `evenFile.txt` should contain the following:
```
456
222
444
888
000
222
444 
974
426
2
4
6
8
12
32
42
64
32
```

and `oddFile.txt` should contain the following:
```
123
111
333
555
777
999
111
333
123
123
1
3
5
7
9
55
75
```

You may use whatever C++ IDE at home that you like as long as your code works with the C++ 14 standard. During the lab, we will use Code::Blocks or the command line to compile and run the code.

Name your file `lab11.cpp`. Make sure to include your name and the name of your TRACE folder at the top of the file in a multi-line comment. When you are done, demonstrate your code to the instructor and upload an electronic copy of your solution in your CSC131 upload folder in a folder named `LABS\lab11`.
