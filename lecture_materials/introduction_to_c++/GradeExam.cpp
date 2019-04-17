//A program that grades multiple-choice tests.
#include <iostream>
using namespace std;

const int NUMBER_OF_QUESTIONS = 10;
  
/*
A function that takes a 2D arrays representing students' answeres for a multiple choice test, a 1D array
representing an answer key, and number of students. the function grades the test and displays the grade
for each students
*/
void gradeExam(const char answers[][NUMBER_OF_QUESTIONS], const char key[], const int num_students)
{
  // Grade all answers
  for (int student = 0; student < num_students; student++)  
  {
    // Grade one student
    int correctCount = 0;
    for (int question = 0; question < NUMBER_OF_QUESTIONS; question++)
    {
      if (answers[student][question] == key[question])
        correctCount++;
    }

    cout << "Student " << student << "'s correct count is "
         << correctCount << endl;
  }

}

int main()
{
  const int NUMBER_OF_STUDENTS = 8;

  // Students' answers to the questions
  const char answers[NUMBER_OF_STUDENTS][NUMBER_OF_QUESTIONS] = 
  {
    {'A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
    {'D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'},
    {'E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'},
    {'C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'},
    {'A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
    {'B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
    {'B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
    {'E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'}
  };

  // Key to the questions
  char key[] = {'D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D'};

  gradeExam(answers, key, NUMBER_OF_STUDENTS);

  return 0;
}
