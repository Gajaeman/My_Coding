#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    string grade;
    cin >> grade;
    float cal = 69 - (int)grade[0];
    if(cal < 0) cal = 0.0;
    else if(grade[1] == '+') cal += 0.3;
    else if(grade[1] == '-') cal -= 0.3;

    cout << fixed << setprecision(1) << cal;

    return 0;
}