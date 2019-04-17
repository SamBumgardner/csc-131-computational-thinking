// This program shows how parameters are promoted and demoted
#include <iostream>
using namespace std;

void foo(int x, double y)
{
  cout << x + y; 
}

int main()
{
    foo(2.5, 45);
    return 0;
 }
