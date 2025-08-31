#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double A, B;
    cin >> A >> B;

    cout << fixed;
    cout << setprecision(9);
    cout << A / B << '\n';

    return 0;
}