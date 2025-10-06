#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s;
    while (true) {
        cin >> s;
        if (s == "0") break;

        string rev = s;
        reverse(rev.begin(), rev.end());

        cout << (s == rev ? "yes" : "no") << '\n';
    }
    return 0;
}