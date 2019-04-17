#include <iostream>
#include <ctime> // for time function
#include <cstdlib> // for rand and srand functions
using namespace std;

int main()
{
  srand(time(0));
  const int rowSize = 3, columnSize = 4;
  int matrix[rowSize][columnSize];
  
  for (int row = 0; row < rowSize; row++) 
  {
    for (int column = 0; column < columnSize; column++) 
    {
      matrix[row][column] = rand() % 100;
    }
  }
  
  //display the 2D array
  for (int row = 0; row < rowSize; row++) 
  {
    for (int column = 0; column < columnSize; column++) 
    {
        cout << matrix[row][column] << " ";
    }
    cout << endl;
  }   
 
  return 0;
}
