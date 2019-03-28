# CSC 131 - Computational Thinking
## Exam 2 Study Guide
### General Information
This exam will allow up to **5** front & back standard-size pages of prepared notes. There's a lot of information to remember about the individual widgets in Tkinter, so use those note pages make the test much easier.

#### Assumed Background Knowledge

The exam will assume that you are familiar with Python's basic language features, functions, and types (and their built-in methods) if we've been using them consistently in class. Please note that **these topics will not be listed in the "main" study guide at the end of this page**.

I've included a list of topics to be familiar with below. I'll do my best to include everything relevant, I do NOT guarantee that this list is 100% accurate.

List of Assumed Familiarity:
 * **Language features**
     * Import statments: `import <module_name>` or `from <module_name> import <thing>`
     * Class definitions: `class`
     * Function definitions: `def`
     * Optional parameters: `some_function(param_1, optional_param = 10)`
     * Conditional statements: `if`, `elif`, and `else`
     * Boolean operators: `and`, `or`, `not`
     * Math operators: `+`, `-`, `*`, `/`, `%`, `**`
     * Loops: `for` and `while`
     * Functions as First-Class data objects
     * Anonymous functions - how to create them and how they work
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
     * Sequence slicing: `l[0:2]`

### List of Topics

The test will be over the information listed below. Information on all topics should be available in the class lecture slides to some extent. However, there have been many examples, questions, and discussions in class that are not completely captured by the raw presentations. **Any information discussed during class lecture may appear on the test**.

I recommend reviewing notes, **writing practice programs**, studying with other students, reviewing past homework / lab programs, reading the book, or looking up information online in addition to looking over presentation slides to prepare for this test.

If you have a solid foundation of knowledge (with well-prepared pages of notes) and plenty of practice, you should understand these topics on both a theoretical and practical level. If you're armed with that understanding, this test should be no trouble whatsoever.

The topics that may be covered in the test are as follows:
 * **Class Inheritance**
     * Understand how a child class inherits all parent class methods. (inheritance)
     * Understand that a child class can re-define a method in a parent class. (polymorphism)
         * When an object's method is called, a child's definition is called instead of a parent's when possible.
 * **Data Containers - `IntVar`, `StringVar`, `DoubleVar`**
     * How to instantiate with a default value.
     * How to get value - `.get()`
     * How to set value - `.set()`
 * **Widgets**
     * Creation
     * Configuration
         * Don't forget about how to configure color, font, and size of different widgets.
     * Interactions with widgets after creation
     * NOTE: any content in lecture slides is fair game, and a lot of it falls under this category. A list of widgets follows.
         * Label
         * Button
         * Entry
         * Frame
         * Radiobutton
         * Checkbutton
         * Canvas
         * Listbox
         * Text
 * **Grid Logic**
     * Basic grid logic - positioning widgets with column, row, and span grid parameters.
     * Uses of "sticky" griding:
         * Aligning widgets within a grid cell.
         * Setting a widget to expand horizontally, vertically, or in all directions.
     * How to use nested frames for complex layouts.
 * **Mouse and Keyboard Events**
     * How to bind an event to a widget.
         * Remember the requriments for an event-triggered function - must take a parameter to hold event information.
     * Know all event types (mouse and keyboard) mentioned in the slides.
         * Know what each event type means, e.g. `"<ButtonPress-1>"` means the left mouse button was clicked on the widget.
     * Know what data is included in the passed-in event object and how it is accessed.
 * **Specification Interpretation**
     * Given a set of specifications or picture of the expected GUI, can identify what code will correctly create that GUI.
