// This program demonstrates the vector data type
#include <iostream>
#include <vector> 
using namespace std;

int main()
{
   // Define a vector of vectors
   vector <vector<int>> vv;
   
   // Define vectors
   vector<int> v1 {1, 2, 3};
   vector<int> v2(5, 1);
   vector<int> v3(v1);
   
   // Add vectors to vector of vectors
   vv.push_back(v1);
   vv.push_back(v2);
   vv.push_back(v3);
   
   
   cout <<"size of vv is "<< vv.size() << endl;
   
   // Display and count elements in vector of vectors
   int count = 0;
   cout <<"\nContents of vv is: " << endl;
   for (auto v : vv)
   {
     for (auto element : v)
     {
       cout << element << " ";
       count++;
     }
     cout << endl;
   } 
   
   cout <<"\nNumber of individual elements in vv is: " << count << endl;
   return 0;
}
