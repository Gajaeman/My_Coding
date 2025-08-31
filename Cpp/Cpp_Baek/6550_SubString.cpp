#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, t;

    while (cin >> s >> t) {
        int idx = 0;
        for (char c : t) {
            if (c == s[idx]) idx++;
            if (idx == s.size()) break;
        }

        if (idx == s.size()) cout << "Yes\n";
        else cout << "No\n";
    }

    return 0;
}
