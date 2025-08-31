#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, t;
    getline(cin, s);
    getline(cin, t);

    int count = 0, i = 0;
    int sl = s.length(), tl = t.length();

    while (i <= sl - tl) {
        if (s.compare(i, tl, t) == 0) {
            count++;
            i += tl;
        } else {
            i++;
        }
    }

    cout << count << '\n';
}