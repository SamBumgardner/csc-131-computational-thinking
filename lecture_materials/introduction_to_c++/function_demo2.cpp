// function_demo2.cpp
#include<iostream>
using namespace std;

constexpr float BONUS_PERCENTAGE = 0.15; // assuming 15% bonus pay

//Function Prototypes
float get_pay (float, float);
float get_bonus (float salary);
void done ();

int main () {
	float wage = 12.5; // hourly
	float hours;
	float pay, bonus;

	cout << "Enter the number of hours you worked this week: ";
	cin >> hours;

	pay = get_pay (wage, hours);
	cout << "You have made $" << pay << " this week!\n";

	bonus = get_bonus (wage * hours);
	cout << "Your bonus would be $" << bonus << " for this week!\n";

	pay = get_pay (wage, 80);
	bonus = get_bonus (wage * 80);
	cout << "If you worked 80 hours, your compensation would be $"
			<< pay + bonus << " then!\n";

	done ();
	return 0;
}

float get_pay (float wage, float hours) {
	return wage * hours;
}

float get_bonus (float salary) {
	return BONUS_PERCENTAGE * salary;
}

void done () {
	cout << "done" << endl;
}
