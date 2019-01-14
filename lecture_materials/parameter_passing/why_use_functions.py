'''
Class: CSC 131
Author: Sam Bumgardner
Purpose: Discuss (and give examples to show) why functions are useful and important.

To use, first navigate your command line to where this file is located, then run the following command:
    python why_use_functions.py
'''

# Remember, any code sitting at the most base level of a python file executes whenever it is run
print("I'm code running outside of any function!", end="\n\n")
# While this is pretty straightforward to use, it's difficult to organize when writing larger programs.

print("I'm about to run some more complicated code outside of a function.", end="\n\n")
'''
Example Problem: Calculate a student's weighted grade.
 
Each grading category has three scores (graded out of 100).
First, we need to calculate the final score for each category by averaging its three scores. 
Then, we need to multiply each average by its weight to get that category's weighted value.
Finally, we add all weighted scores together to get the student's final grade.
'''
# Here are the student's scores and the weight each category should use:
test_score_1 = 82
test_score_2 = 89
test_score_3 = 91
test_weight = .55

homework_score_1 = 90
homework_score_2 = 100
homework_score_3 = 100
homework_weight = .30

lab_score_1 = 85
lab_score_2 = 77
lab_score_3 = 100
lab_weight = .15

# Here's the code to solve the problem, done without functions:
test_score_sum = test_score_1 + test_score_2 + test_score_3
test_score_average = test_score_sum / 3.0
test_weighted_value = test_score_average * test_weight

homework_score_sum = homework_score_1 + homework_score_2 + homework_score_3
homework_score_average = homework_score_sum / 3.0
homework_weighted_value = homework_score_average * homework_weight

lab_score_sum = lab_score_1 + lab_score_2 + lab_score_3
lab_score_average = lab_score_sum / 3.0
lab_weighted_value = lab_score_average * lab_weight

final_grade = test_weighted_value + homework_weighted_value + lab_weighted_value

print("Student's final grade is: " + str(final_grade))

# The code above works, but it isn't very easy to read.
# Also, it becomes even harder to read if we want to solve the same problem for multiple students.
# For the sake of an example, I'll add data for two more students and calculate their grades as well.

# Alice's scores
alice_test_score_1 = 93
alice_test_score_2 = 97
alice_test_score_3 = 99

alice_homework_score_1 = 100
alice_homework_score_2 = 100
alice_homework_score_3 = 100

alice_lab_score_1 = 65
alice_lab_score_2 = 50
alice_lab_score_3 = 88

# Bob's scores
bob_test_score_1 = 76
bob_test_score_2 = 100
bob_test_score_3 = 98

bob_homework_score_1 = 90
bob_homework_score_2 = 88
bob_homework_score_3 = 77

bob_lab_score_1 = 100
bob_lab_score_2 = 100
bob_lab_score_3 = 100

# It's easy to overlook a mistake in the following pile of code... can you find the one I made?

alice_test_score_sum = alice_test_score_1 + alice_test_score_2 + alice_test_score_3
alice_test_score_average = alice_test_score_sum / 3.0
alice_test_weighted_value = alice_test_score_average * test_weight

alice_homework_score_sum = alice_homework_score_1 + alice_homework_score_2 + alice_homework_score_3
alice_homework_score_average = alice_homework_score_sum / 3.0
alice_homework_weighted_value = alice_homework_score_average * homework_weight

alice_lab_score_sum = alice_lab_score_1 + alice_lab_score_2 + alice_lab_score_3
alice_lab_score_average = alice_lab_score_sum / 3.0
alice_lab_weighted_value = alice_lab_score_average * lab_weight

alice_final_grade = alice_test_weighted_value + alice_homework_weighted_value + alice_lab_weighted_value

print("Alice's final grade is: " + str(alice_final_grade))

bob_test_score_sum = bob_test_score_1 + bob_test_score_2 + bob_test_score_3
bob_test_score_average = bob_test_score_sum / 3.0
bob_test_weighted_value = bob_test_score_average * test_weight

bob_homework_score_sum = bob_homework_score_1 + bob_homework_score_2 + bob_homework_score_3
bob_homework_score_average = alice_homework_score_sum / 3.0
bob_homework_weighted_value = bob_homework_score_average * homework_weight

bob_lab_score_sum = bob_lab_score_1 + bob_lab_score_2 + bob_lab_score_3
bob_lab_score_average = bob_lab_score_sum / 3.0
bob_lab_weighted_value = bob_lab_score_average * lab_weight

bob_final_grade = bob_test_weighted_value + bob_homework_weighted_value + bob_lab_weighted_value

print("Bob's (incorrect) final grade is: " + str(bob_final_grade), end="\n\n")

# Line 109 is incorrect - I'm using Alice's summed homework score instead of bob's.

'''
To organize your code, identify the individual jobs your program must do to complete the full program.
Usually you can turn each of those individual jobs into its own function.

To put it another way, any time you're copying and pasting sections of code, it could be a function.

In the above example, we had one particular job we were repeating over and over again:
calculate the weighted value of a category.

To make our program simpler and easier to read, we'll make a function to contain that job for us.
'''

'''
When writing a function to handle a job for us, we should first identify what information *we* needed
    when we were handling that job ourselves.

For our example, we needed a few things when calculating any category's final weighted value:
    The first score for that category
    The second score
    The third score
    The category's weight

If we have exactly those four pieces of information, we can always calculate a category's weighted value.
The function works in the same way; it needs those four pieces of information to do its calculation.
    After we know what data the function will need to do its job, we make those its parameters.
'''
# The parameters to the function go inside the parenthesis below
def calculate_weighted_category_value(score_1, score_2, score_3, category_weight):
    # The body of the function uses those parameters to complete its job.
    sum_score = score_1 + score_2 + score_3
    avg_score = sum_score / 3.0
    weighted_value = avg_score * category_weight
    
    return weighted_value


# Now that we have our function, we can use it to calculate our original student's grades much more simply:
print("Calculating Student's grade again, this time with functions...")

test_weighted_value = calculate_weighted_category_value(test_score_1, test_score_2, test_score_3, test_weight)
homework_weighted_value = calculate_weighted_category_value(homework_score_1, homework_score_2, homework_score_3, homework_weight)
lab_weighted_value = calculate_weighted_category_value(lab_score_1, lab_score_2, lab_score_3, lab_weight)

final_grade = test_weighted_value + homework_weighted_value + lab_weighted_value
print("Student's final grade is: " + str(final_grade))

'''
And viola, the resulting code is both easier to read and less error-prone!
Of course, there are plenty more things we could do to keep improving this process, 
    but this is a fine stopping point for now.
'''

'''
A quick aside about how much you should break down a job when making functions:
    You could also break down the "calculate weighted value" job even further into its pieces:
        calculate sum
        find average
        multiply average and category weight
    
    Using those three mini-functions to replace the original messy mega-program would also be valid.
    When deciding how small your functions should be, I usually consider whether breaking down a job
        further ends up making pieces that are useful on their own. If so, then I'll break down. If not,
        I'll typically keep them bundled together for now.
    
    That said, experience is an excellent teacher! Trying things out will help you get a better
        understanding of how granular you'd like your functions to be.
'''
