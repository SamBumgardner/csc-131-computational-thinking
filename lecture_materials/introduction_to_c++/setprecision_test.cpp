/*
 * console_input_string.cpp
 *
 * Reading a string
 */
#include<iostream>
#include<iomanip>
using namespace std;

int main () {
  double a = 123.456;
     cout << setprecision(4) << a << endl; 
     cout << setprecision(5) << a << endl;
     cout << setprecision(10) << a << endl;
     cout << setprecision(15) << a << endl;

     return 0;
}
