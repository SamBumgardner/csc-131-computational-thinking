# CSC 131 - Computational Thinking
## Assignment Information
This page serves as an info dump for generic homework assignment-related information. If the information you're looking for isn't in the homework assignment itself, check here next. 

If you can think of any information that would be useful to have here (but isn't already) feel free to bring it up with me in person, via email, or (if you're feeling adventurous) by making a suggesting changes via a pull request from a forked repository.

### Automated Grading Policy
Most assignments in this class will be graded through an automated process. This is very likely to be different from any of your previous classes, so please read the sections below carefully to make sure you understand how grading will work.

#### Why Automate Grading?
I prefer automated grading because it makes grading homework much, much, *much* faster. This has a few different benefits:

 * Students get feedback on their work faster. Results of grading are sent back to students the same day the assignment is due.
 * Grading takes less of the instructor and/or their grader's time.
 * Allowing multiple submissions for each assignment becomes feasible. I'll talk more about this later.

However, there are some downsides as well:

 * Automated grading can be a bit finicky - the location, input, and output to a program must be exactly right for it to work.
     * This isn't all bad, though. The ability to very precisely match expectations is an important thing to develop as a computer scientist. 
 * Automated grading doesn't provide feedback on *how* the result was accomplished. It only cares if the final answers were correct.
 
I feel that the benefits outweigh the downsides, so when possible I will aim to automate grading for this class.

#### How it Works
On the day an assignment is due, students are expected to have a completed homework program uploaded to their \\\\TRACE folder with the naming and folder location specified in the homework assignment. At some point later that day (after the official due date/time) the assignments will be automatically graded. 

If an assignment passes all automated tests, then it is considered complete. It is awarded a full 10 / 10 points for being completed on the day it was due.

If an assignment did not pass all automated tests (whether due to error or incorrect output), then it is considered incomplete. No grade will be recorded for it until it becomes complete.

The results of the automated testing will be emailed to each student individually. In the event that their assignment was incomplete, the email will include an explanation of what went wrong. If an error occurred, the error message is provided. If the program provided incorrect output for a test, then the following information will be included for each failed test:
 * The input for the test.
 * The expected output (result) of that test.
 * The actual output that the student's program provided.
 
With this information, a student should be able to replicate and troubleshoot the incorrect behavior. After fixing their errors and/or fixing incorrect behavior, the students are expected to upload the updated version of their file to their \\\\TRACE folder, overwriting the previous (incorrect) version of their file.

On the day following the original due date, the automated grading process will be run again (the specific time will be mentioned in the feedback email, typically no earlier than 7:00 PM). The programs will be evaluated in the same manner as they were the first day, with reduced credit for a successful program:

If an assignment passes all automated tests, then it is considered complete. It is awarded partial credit - **(10 - the number of days that have passed since the original due date) / 10** points for being completed after the original due date.

If an assignment did not pass all automated tests (whether due to error or incorrect output), then it is considered incomplete again. No grade will be recorded for it until it becomes complete. 

This process is repeated a total of 4 times, with the last possible submission being worth 6 / 10 points. After that, any request to turn in homework for less credit will need to be made directly to the instructor.

#### Step-by-Step Homework Guide
**This is the most important part of this file.** I'll aim to be as clear and precise as possible here, so please read carefully.

When an assignment is created, follow the following steps for success:
 1. Read the assignment carefully. Make sure to pay close attention to the following pieces of information:
     * Expected inputs to the program
     * Expected outputs of the program
     * What the program should be named
     * The folder(s) the program should be contained within on \\\\TRACE
 2. Complete the assignment, uploading it to the correct location in \\\\TRACE when finished.
     * Make sure to visit the tutoring lab early and often for assistance if you're having trouble.
     * Test your program with any sample inputs provided with the assignment.
     * Test your program with other inputs that you can think of that would be useful. 
     * **The last thing you should do with your program is run it from its location in \\\\TRACE.** If you have to make further changes, do that final run again.
 3. Wait until the due date
     * This should take a while, since you got your homework done so early :D
 4. On the evening of / the morning following the grading **check your email for results!**
 5. If your program was successful, celebrate! You're done. If not, go to step 6.
 6. If your program was unsuccessful, go to step 7 to fix it.
 7. Fixing your program:
     1. Attempt to recreate the incorrect behavior by running the program yourself with the problematic inputs. 
     2. Re-read the assignment, make sure to understand why the behavior is incorrect.
     3. Identify what part of your program is causing the incorrect behavior. This may take some time.
     4. Correct the program to follow the assignment's specifications correctly.
     5. Run the problematic inputs again, verifying that they now give the desired result.
     6. Upload the fixed program to trace, overwriting the old incorrect program.
 8. Wait until the next grading occurs, then go to step 4.
 
 Hopefully the above steps make navigating the grading process easier. If you have any questions, suggestions, or thoughts on the step-by-step guide (or anything else about automated grading) please bring it up with me. It is my goal to make this grading system useful everyone involved, and hopefully help everyone learn better along the way.
   
