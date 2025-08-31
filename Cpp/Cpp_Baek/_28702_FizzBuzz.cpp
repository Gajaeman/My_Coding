#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, res;
    int idx;
    for (int i = 0; i < 3; i++) {
        cin >> s;
        if (!(s == "Fizz" || s == "Buzz" || s == "FizzBuzz")) {
            idx = i;
            res = s;
        }
    }
    int val = stoi(res) + (3 - idx);
    if (val % 15 == 0) cout << "FizzBuzz";
    else if (val % 3 == 0) cout << "Fizz";
    else if (val % 5 == 0) cout << "Buzz";
    else cout << val;
    return 0;
}
