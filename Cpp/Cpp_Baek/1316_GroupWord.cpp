#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int t, cnt = 0;
    cin >> t;

    while (t--) {
        string s;
        cin >> s;

        vector<bool> vec(26, false);
        bool is_group = true;
        char ch = 0;

        for (char c : s) {
            if (c != ch) {
                if (vec[c - 'a']) {
                    is_group = false;
                    break;
                }
                vec[c - 'a'] = true;
            }
            ch = c;
        }

        if (is_group) cnt++;
    }

    cout << cnt;
    return 0;
}
