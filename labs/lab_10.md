# CSC 131 - Computational Thinking
## Lab 10

Write simple mathematical functions in C++ that demonstrate different advanced features of functions. The `main()` function will be provided for you at the end of this file, so you will only need to implement the program's other functions. A full specification of the program's requirements are listed below.

### Requirements
 * Add
     * After your `main` function, write a function named `add` that takes two integers as parameters and returns their sum as an integer.
     * Overload the `add` function by writing a version of it that takes two doublese as parameters and returns their sum as a double.
     * Write prototypes for the two definitions of `add` before `main` so the program runs without error.
 * Subtract
     * After your `main` function, write a function named `subtract` that takes two integers as parameters and returns the result of subtracting the second number from the first.
         * i.e. int1 - int2
     * Change `subtract` to have default arguments for its two parameters. Pick whatever non-zero numbers you would like.
     * Write a prototype for `subtract` before `main` so the program runs without error.
 * Divide
     * After your `main` function, write a function named `divide` that has integer parameters for `dividend`, `divisor`, `quotient`, and `remainder` and returns **nothing**.
         * Note: `divide`'s goal is to find the integer quotient and remainder of division, not find the exact decimal result.
     * Rather than returning a single value normally, make `quotient` and `remainder` pass-by-reference, then set their values within the function so they contain the results of division.
         * For example, after `divide(5, 2, my_quotient, my_remainder)` the variable `my_quotient` should contain `2` and the variable `my_remainder` should contain `1`.
     * Write a prototype for `divide` before `main` so the program runs without error.
 * Multiply     
    * After your `main` function, write a function named `multiply` that takees two integers as parameters and returns the result of multiplying the two together.
    * Add a static variable to `multiply` that tracks how many times `multiply` has been called.
    * Add code to `multiply` to write a message in the console stating how many times `multiply` has been called.
    * Write a prototype for `multiply` before `main` so the program runs without error.
    

Paste the following `main()` function into your program to test your functions:
 * Note that this function expects that you have already added `#include <iostream>` and `using namespace std;` to your program.
```c++
int main() {
    char dummy;
    
    int int1, int2;
    cout << "Please enter two integers to add: ";
    cin >> int1 >> int2;
    
    cout << "The sum of these numbers is " << add(int1, int2) << endl << endl;
    
    double double1, double2;
    cout << "Please enter two doubles to add: ";
    cin >> double1 >> double2;
    
    cout << "The sum of these numbers is " << add(double1, double2) << endl << endl;
    
    int sub1, sub2;
    cout << "Please enter two integers to subtract: ";
    cin >> sub1 >> sub2;
    
    cout << "The difference of these numbers is " << sub(sub1, sub2) << endl << endl;
    
    cout << "The difference of the default numbers is " << sub() << endl << endl;
    
    int dividend, divisor, quotient, remainder;
    cout << "Please enter two integers to divide: " << endl;
    cout << "Dividend: ";
    cin >> dividend;
    cout << "Divisor: ";
    cin >> divisor;
    
    divide(dividend, divisor, quotient, remainder);
    cout << "The result of division is " << quotient << " remainder " << remainder << endl << endl;
    
    int mul1, mul2, product;
    cout << "Please enter two integers to multiply: ";
    cin >> mul1 >> mul2;
    
    product = multiply(mul1, mul2);
    cout << "The result of multiplication is " << product << endl;
    cout << "Let's do it again!" << endl << endl;
    
    product = multiply(mul1, mul2);
    cout << "The result of multiplication is " << product << endl;
    cout << "Let's do it again!" << endl << endl;
    
    product = multiply(mul1, mul2);
    cout << "The result of multiplication is " << product << endl;
    
    return 0;
}
```

A sample program runs is as follows, where all text after each `:` is input from the user:
```
Please enter two integers to add: 123 764
The sum of these numbers is 887

Please enter two doubles to add: 2.3 817
The sum of these numbers is 819.3

Please enter two integers to subtract: 11 8
The difference of these numbers is 3

The difference of the default numbers is 27

Please enter two integers to divide:
Dividend: 8783
Divisor: 13
The result of division is 675 remainder 8

Please enter two integers to multiply: 3 9
multiply has been called 1 times!
The result of multiplication is 27
Let's do it again!

multiply has been called 2 times!
The result of multiplication is 27
Let's do it again!

multiply has been called 3 times!
The result of multiplication is 27
```

You may use whatever C++ IDE at home that you like as long as your code works with the C++ 14 standard. During the lab, we will use Code::Blocks or the command line to compile and run the code.

Name your file `lab10.cpp`. Make sure to include your name and the name of your TRACE folder at the top of the file in a multi-line comment. When you are done, demonstrate your code to the instructor and upload an electronic copy of your solution in your CSC131 upload folder in a folder named `LABS\lab10`.
