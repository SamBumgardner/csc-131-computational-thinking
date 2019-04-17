/*
A program for a first grader to practice subtraction. The program randomly generates two single-digit 
integers number1 and number2 with number1 >= number2 and displays a question such as “What is 9 – 2?” 
to the student. After the student types the answer, the program displays a message to indicate whether 
the answer is correct. 
*/
#include <iostream>
#include <ctime> // for time function
#include <cstdlib> // for rand and srand functions
using namespace std;

int main()
{
  // Generate two random single-digit integers
  srand(time(0));
  int number1 = rand() % 10;
  int number2 = rand() % 10;
 
  int x = max(number1, number2);
  number2 = min(number1, number2); 
  number1 = x;

  // Prompt the student to answer “what is number1 – number2?”
  cout << "What is " << number1 << " - " << number2 << "? ";
  int answer;
  cin >> answer;

  // Grade the answer and display the result
  if (number1 - number2 == answer)
    cout << "You are correct!";
  else
  {
    cout << "Your answer is wrong." << endl;
    cout << number1 << " - " << number2 << " should be " << (number1 - number2) << endl;
  }

  return 0;
}
