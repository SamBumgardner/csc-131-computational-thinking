# CSC 131 - Computational Thinking
## Exam 1 Study Guide
### General Information
#### Review Presentation
The original set of [review slides](https://docs.google.com/presentation/d/1cgZ7rctS1eEiy1D9nuuq7ukL-iMWvLc4Qel-yDgb-AQ/edit?usp=sharing) are provide a nice overview of pre-Design With Classes content. Do **NOT** rely on these slides alone; read through the rest of this review to get a full picture of the exam's content.

#### Definitions vs. Application
The test questions will focus on the application of concepts more than definitions. Expect code to be involved in most, if not all of the exam questions. 

For example, there will not be a test question that says “What does ‘immutable’ mean?” 

Instead, expect a question that tests your understanding of immutability, like:

Consider the following code, then answer the questions below.
```python
a = “z,x,y”
b = a

a.upper()

c = b.split(“,”)
d = c

d.sort()
```

After running the above code, what is the value of `a`?
 1. `“Z,X,Y”`
 2. `“z,x,y”`
 3. `["z", "x", "y"]`
 4. `["Z", "X", "Y"]`
 5. `["x", "y", "z"]`
 6. `["X", "Y", "Z"]`

After running the above code, what is the value of `b`?
 1. `“Z,X,Y”`
 2. `“z,x,y”`
 3. `["z", "x", "y"]`
 4. `["Z", "X", "Y"]`
 5. `["x", "y", "z"]`
 6. `["X", "Y", "Z"]`

etc.

(For the curious, the variable values are as follows: `a` = `"z,x,y"`, `b` = `"z,x,y"`, `c` = `["x", "y", "z"]`, `d` = `["x", "y", "z"]`)

That said, the definition of a concept can often serve as a good reminder when trying to understand how a concept works.

#### Assumed Background Knowledge

The exam will assume that you are familiar with Python's basic language features, functions, and types (and their built-in methods) if we've been using them consistently in class. Please note that **these topics will not be listed in the "main" study guide at the end of this page**.

Aside from methods we've specifically lectured over (like `map()`, `filter()`, `reduce()`, etc.), don't expect questions to focus on built-in functions. That said, remembering what they do may be important for solving a question, like in the mutability example earlier. So, while there won't be questions specifically asking about how these functions and types work, **remembering their inputs, outputs, and side-effects is important**.

I've included a list of topics to be familiar with below. I'll do my best to include everything relevant, I do NOT guarantee that this list is 100% accurate.

List of Assumed Familiarity:
 * **Language features**
     * Function definitions: `def`
     * Conditional statements: `if`, `elif`, and `else`
     * Boolean operators: `and`, `or`, `not`
     * Math operators: `+`, `-`, `*`, `/`, `%`, `**`
     * Loops: `for` and `while`
 * **Built-in functions**
     * `print()`
     * `range()`
     * `len()`
     * `min()`
     * `max()`
     * `sum()`
     * `int()`
     * `float()`
     * `str()`
     * `list()`
 * **String type**
     * `s.upper()`
     * `s.lower()`
     * `s.split()`
     * `s.strip()`
     * `s[some_index]`
 * **List type**
     * `l.sort()`
     * `l.append()`
     * `l[some_index]`


### List of Topics

The test will be over the information listed below. Information on all topics should be available in the class lecture slides to some extent. However, there have been many examples, questions, and discussions in class that are not completely captured by the raw presentations. **Any information discussed during class lecture may appear on the test**.

I recommend reviewing notes, **writing practice programs**, studying with other students, reviewing past homework / lab programs, reading the book, or looking up information online in addition to looking over presentation slides to prepare for this test.

If you have a solid foundation of knowledge and plenty of practice, you should understand these topics on both a theoretical and practical level. If you're armed with that understanding, this test should be no trouble whatsoever.

The topics that may be covered in the test are as follows:
 * **Parameter Passing**
     * Variables as labels (how variable assignment works)
     * Mutabilility vs. Immutability
         * Know which types are Mutable and which are Immutable
         * Understand how those types' methods differ
     * Understand how a changes to a parameter inside a function may affect variables outside that function
 * **2D Lists**
     * Valid ways to create a 2D list
     * How to access individual items inside nested lists (number of nested lists may be greater than 2)
     * Different ways of looping through 2D lists
 * **Higher Order Functions**
     * Functions as First-Class data objects
     * `map()` - inputs, functionality, output
     * `filter()` - inputs, functionality, output
     * `reduce()` - inputs, functionality, output
     * Anonymous functions - how to create them and how they work
     * List comprehensions
     * Ternary Operator (aka Conditional Expressions) 
 * **Recursion**
     * Recursive definitions
         * Identify if a definition is recursive
         * Understand and follow a recursive definition
     * Elements of a recursive solution
         * Identify and understand base cases
         * Identify and understand recursive cases
     * Evaluating a recursive solution
         * Identify if a recursive solution will never complete
         * Judge if a recursive solution accurately solves a problem
 * **Design With Classes** - up to content covered on Friday, Feb 15.
     * Defining Classes
         * Evaluate if a class is defined correctly
         * Evaluate if a class's methods are defined correctly   
     * Understand definition and usage of instance variables
     * Interpret a class's interface - understand how that class can / should be used
     * Special class methods
         * Understand purpose and correct usage of `__init__` method
         * Understand purpose and correct usage of `__str__` method
         * Understand purpose and correct usage of math methods: `__add__`, `__sub__`, `__mul__`, `__truediv__`
         * Understand purpose and correct usage of comparison methods: `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`
     * Class variables
         * Understand how they are created
         * Understand how they are shared
         * Understand how they can be accessed & changed.
     * Ability to design class(es) to solve a problem
         * Identify behaviors each instance of the class can do 
         * Identify attributes each instance of the class should have
         * Create an interface for a class, including
             * Name for each method
             * Parameters each method needs
             * Short description of what the method does
         * Decide how attributes should be stored
         
