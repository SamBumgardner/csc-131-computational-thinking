//Reading a strin using getline
//File name: readString2.cpp
#include<iostream>
#include <string>

using namespace std;

int main () {
	string name;

	cout << "What's your name? ";
	//cin >> name;
	getline (cin, name);
	cout << "You're " << name << endl;
	return 0;
}
