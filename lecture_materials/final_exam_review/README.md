# CSC 131 - Computational Thinking
## Final Exam Study Guide
### General Information
This exam will allow up to **2** front & back standard-size pages of prepared notes. Please take advantage of all space allotted to you - preparation makes tests 1000000% easier.

### List of Topics

The test will be over the information listed below. Information on all topics should be available in the class lecture slides to some extent. However, there have been many examples, questions, and discussions in class that are not completely captured by the raw presentations. **Any information discussed during class lecture may appear on the test**.

I recommend reviewing notes, **writing practice programs**, studying with other students, reviewing past homework / lab programs, reading the book, or looking up information online in addition to looking over presentation slides to prepare for this test.

If you have a solid foundation of knowledge (with well-prepared pages of notes) and plenty of practice, you should understand these topics on both a theoretical and practical level. If you're armed with that understanding, this test should be no trouble whatsoever.

The topics that may be covered in the test are as follows:

#### Basic Constructs: Slides 5 - 82
 * What is the purpose of a compiler?
 * Comment syntax 
     * `//` for single line
     * `/* ... */` for multi-line
 * Basic namespace rules
     * How do we use keywords from standard libraries (like `cout` or `endl`) if we don't put `using namespace std` in a program?
 * Basic output with `cout` and `endl`
     * How to import stream i/o into a program: `#include<iostream>`
 * "Identifier" (variable and function) name rules
     * Recognize if an identifier is illegal
 * Knowledge of basic types. For each type mentioned in the slides, know the following:
     * Type name
     * Purpose / use case for the type. When is it appropriate to use?
 * Defining and initializing variables - be familiar with all methods in slides.
 * C++ operators
     * Addition: \+
     * Subtraction: \-
     * Multiplication: \*
     * Division: /
     * Modulo: %
     * Increment: ++
     * Decrement: --
     * Assignment: =
     * Compound Assignment: +=, -=, *=, /=
 * The `string` type basic usage
     * It's important to note the differences between `string` and `char`
     * How to import strings into a program: `#include<string>`
 * Basic input with `cin`
     * Also understand usage of `getline()`
 * `constexpr` and `const`
     * Understand the difference between the two
 * Function definition syntax
 * Function prototype syntax
     * Understand why prototypes are useful (and sometimes necessary in C++)
 * How functions work in C++
     * parameters
     * default pass-by-value behavior
     * optional pass-by-reference behavior (using `&` operator)
     * defining a function with default parameters
     * `return` behavior
 * How overloading function definitions work
 * Global variables
     * How to define a global variable
     * Default initialization value - how is it different from local variables?
 * Static local variables
     * How to define a static local variable
     * Default initialization value - how is it different from non-static local variables?
     * What do static local variables do?
 * Usage of `exit()` function
     * How to import system commands like `exit()` into a program: `#include<cstdlib>`
 
#### Control Statements
 * Relational operators
     * less than: `<`
     * less than or equal to: `<=`
     * greater than: `>`
     * greater than or equal to: `>=`
     * equal to: `==`
     * not equal to: `!=`
 * Pay attention to slide 19, which notes that the result of using a relational operator is always a true/false value
 * Logical operators
     * not: `!`
     * logical and: `&&`
     * logical or: `||`
 * Understand short-circuit evaluation with logical operators
 * `if`, `else if`, `else` syntax and usage
 * Usage of the conditional operator
 * `switch` statmeents
 * `break`- purpose and usage
 * `while` loops
 * `for` loops - standard and range-based
 * File input and output with `ifstream` and `ofstream`
     * How to import file stream types: `#include<fstream>`
 * Arrays
     * How to create
     * How to modify / assign data to array
     * How to retrieve / use data from array
     * How to write a function that takes an array as a parameter
 * 2-D Arrays
     * How to create
     * How to modify / assign data to 2-D array
     * How to retrieve / use data from 2-D array
     * How to write a function that takes a 2-D array as a parameter
 * Vectors
     * How to create a vector that stores different types
     * How to modify / assign data to a vector
     * How to retrieve / use data from a vector
     * Understand usage of vector member functions
         * `.at()`
         * `.size()`
         * `.push_back()`
         * `.pop_back()`
     * How to import vectors into a program: `#include<vector>`

#### Pointers
 * address operator `&`
 * declaring pointer variables - `int *myIntPointer`
 * indirection operator `*`
 * allocating memory with `new` - for single objects and arrays.
 * de-allocating memory with `delete` - for single objects and arrays.
 * pointer and integer addition - using a pointer to access array indexes.
