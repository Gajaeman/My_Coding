#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string str, key;
    getline(cin, str);
    getline(cin, key);

    int k = 0;
    for (char c : str) {
        if (c == ' ') {
            cout << ' ';
        } else {
            int shift = key[k % key.size()] - 'a' + 1;
            char res = c - shift;
            if (res < 'a') res += 26;
            cout << res;
        }
        k++;
    }
    cout << '\n';

    return 0;
}