// This program demonstrates accepting a 2D array argument
#include <iostream>
using namespace std;

const int COLUMN_SIZE = 4;

int sum(const int a[][COLUMN_SIZE], int rowSize); //function prototype

int main()
{ 
  const int ROW_SIZE = 3;
  int m[ROW_SIZE][COLUMN_SIZE];
  cout << "Enter " << ROW_SIZE << " rows and "
    << COLUMN_SIZE << " columns: " << endl;
  for (int i = 0; i < ROW_SIZE; i++)
    for (int j = 0; j < COLUMN_SIZE; j++)
      cin >> m [i][j];

  cout << "\nSum of all elements is " << sum(m, ROW_SIZE) << endl;

  return 0;
}

int sum(const int a[][COLUMN_SIZE], int rowSize)
{
  int total = 0;
  for (int row = 0; row < rowSize; row++)
  {
    for (int column = 0; column < COLUMN_SIZE; column++)
    {
      total += a[row][column];
    }
  }

  return total;
}
