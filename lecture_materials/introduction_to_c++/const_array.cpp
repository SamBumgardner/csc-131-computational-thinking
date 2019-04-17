#include <iostream>
using namespace std; 

void p(const int list[], int arraySize)
{
  // Modify array accidentally
  list[0] = 100; // Compile error!
}

int main()   
{
  int numbers[5] = {1, 4, 3, 6, 8};
  p(numbers, 5);

  return 0;
}