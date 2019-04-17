// This program demonstrates the the vector data type
#include <iostream>
#include <vector>
using namespace std; 

int main()
{
   // Define and initialize a vector.
   vector<int> numbers { 10, 20, 30, 40, 50 };

   // Display the vector elements.
   for (int val : numbers)
      cout << val << " ";
   cout << endl;
      
   vector<int> v(5);
   v.push_back(1);
   v.push_back(2);
   
   for (int val : v)
      cout << val << " "; 
   cout << endl;
   
   cout << "Size of v is " << v.size() << endl;

   return 0;
}
