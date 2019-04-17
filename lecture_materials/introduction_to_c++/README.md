# CSC 131 - Computational Thinking
## Introduction to C++ Reference Materials

### Lecture Slides
 * [C++ Basic Constructs](https://docs.google.com/presentation/d/1j9Ik_DNFQWR4h15vtWa8-tFjRHB8gZPZ8LRyI9Ihjkk/edit?usp=sharing)
 * [Control Statements](https://docs.google.com/presentation/d/1LcwSrsmlZGT4F5mpUied-kkPxLccF9iJezE4N04V2D4/edit?usp=sharing)

### C++ Example Programs
Examples will be added as we go over them in class, and I expect each sub-section of C++ content will end up getting its own little folder of programs. A master list of uploaded examples will be maintained here.
 * **C++ Basic Constructs** example programs:
     * [prog1.cpp](./prog1.cpp) - Basic "hello world" C++ program, good for testing out the whole compilation process.
     * [calculatePay.cpp](./calculatePay.cpp) - Demonstrates use of `cout` to display data to the user and `cin` to read in their input.
     * The following programs all have examples of defining and using simple functions:
         * [function_demo1.cpp](./function_demo1.cpp) - First example program with functions.
         * [function_demo2.cpp](./function_demo2.cpp) - Demonstrates basic use of function prototypes.
         * [function_default_arguments.cpp](./function_default_arguments.cpp)
         * [function_early_return.cpp](./function_early_return.cpp) - When a function has a return type of `void`, it can still use `return` to end function execution early.
         * [function_parameters_promote_demote](./function_parameters_promote_demote.cpp) - C++ automatically promotes/demotes types as necessary to make argument types fit the parameters defined by a function. This can have undesired side effects.
         * [function_global_constants.cpp](./function_global_constants.cpp) - Demonstrates using global variables from within a function.
         * [function_overloading_functions.cpp](./function_overloading_functions.cpp) - Defining a function can be defined multiple times with the same name but different parameter types. When this is done, the compiler will use the types of arguments passed in during a function call to figure out which function definition to actually call.
         * [function_reference_variables.cpp](./function_reference_variables.cpp) - Changes made to a reference variable (including reassignment!) persist after the function ends.
         * [function_static_variables.cpp](./function_static_variables.cpp) - Static variables created within a function are only initialized the first time the function is called. After that, its values persist from function call to function call.
     * [readString.cpp](./readString.cpp) - Demonstrates reading a string from standard input using `cin`.
     * [readString2.cpp](./readString2.cpp) - Demonstrates reading a multi-word string from standard input using the `getline` function.
     * [subtractionQuiz.cpp](./subtractionQuiz.cpp) - Demonstrates random number generation.
     * [dollarFormat.cpp](./dollarFormat.cpp) - Demonstrates use of `string` methods like `find` and `insert`.
     * [setprecision_test.cpp](./setprecision_test.cpp) - Demonstrates basic use of the `setprecision` function from the `iomanip` library.
 * **Control Statements** example programs:
     * [round_off_errors.cpp](./round_off_errors.cpp) - Demonstrates how comparisions with floating point numbers can be unpredictable.
     * [if_else_statement.cpp](./if_else_statement.cpp)
     * [conditional_operator.cpp](./conditional_operator.cpp)
     * The following programs all have examples of using `switch` statements:
         * [switch_statement.cpp](./switch_statement.cpp)
         * [switch_fallthrough.cpp](./switch_fallthrough.cpp) - Example of intentionally letting a switch statement "fall through" by not including `break` after a switch case is complete.
         * [switch_menu.cpp](./switch_menu.cpp) - Example of using a switch statement to control the flow of a menu-driven program.
     * [block_scope.cpp](./block_scope.cpp) - Demonstrates how variables go into and out of scope in a program with nested blocks of code.
     * [same_name.cpp](./same_name.cpp) - Shows that redefining a local variable in a nested block (**while highly inadvisable!**) is valid in C++.
     * [do_while.cpp](./do_while.cpp)
     * [for_loop.cpp](./for_loop.cpp)
     * The following programs all have examples of working with file input and output:
         * [file2.cpp](./file2.cpp) - Demonstrates writing to a file.
         * [files_.cpp](./files_readNumbers.cpp) - Demonstrates reading integers from a file via a while loop.
         * [files1.cpp](./files1.cpp) - A more thorough example of opening and working with a user-selected file that might not exist.
     * [array_argument](./array_argument.cpp) - Demonstrates how to write a function that has an array-type parameter.
     
     

### External Reference
 * [LearnCpp.com](https://www.learncpp.com/) - A truly excellent resource for learning C++. I tend to prefer its approach to learning the language - focusing on topics like header files and multi-file programs early is a particularly appealing to me. It's not required reading, but consider this resource an excellent supplement to everything our in-class lecture focuses on.
 * [General C++ Reference](https://en.cppreference.com/w/) - Not terribly easy to read, but it is a pretty comprehensive source of detailed C++ information.
 * [C++ Standard Library Reference](http://www.cplusplus.com/reference/) - Contains information about objects and functions included in the various C++ standard libraries
 * [Memory Layout of a C Program](https://www.geeksforgeeks.org/memory-layout-of-c-program/) - As we talk about memory addresses, arrays, and pointers this article will serve as a useful reference how memory addresses are determined during program execution. Note that while the article name says "C Program" its contents apply equally to C++.
