// This program writes data to a file. 
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
   ofstream outputFile;
   outputFile.open("names.txt");

   cout << "Now writing data to the file.\n";

   // Write four names to the file.
   outputFile << "Mark\n";
   outputFile << "George\n";
   outputFile << "Scott\n";
   outputFile << "Mary\n";

   // Close the file
   outputFile.close();
   cout << "Done.\n";
   return 0;
}