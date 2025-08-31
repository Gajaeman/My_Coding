#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;

    for (char &c : s) {
        if (c >= 'a' && c <= 'z') c = c - 'a' + 'A';
        else if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';
    }
    cout << s;
    return 0;
}