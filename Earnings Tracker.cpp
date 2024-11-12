#include <iostream>

using namespace std;

class AcelIT{
public:
    int hours_worked;
    void Hours(){
        cout << "Enter the number of hours you worked this summer: ";
        cin >> hours_worked;
    }
};

class Grass: public AcelIT{
public:
    int weeks;
    void Weeks(){
        cout << "Enter the number of weeks you have cut this year: ";
        cin >> weeks;
    }
};

class Total: public Grass{
    int total_hours;
    int total_weeks;
    int total_earned;
public:
    void Lagistics(){
        total_hours = hours_worked * 15.4;
        total_weeks = weeks * 175;

        total_earned = total_hours + total_weeks;
        cout << "You earned a total of $" << total_earned << " this summer!";
    }
};


int main(){

    Total t;
    t.Hours();
    t.Weeks();
    t.Lagistics();

    return 0;
}