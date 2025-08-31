#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    while (cin >> n) {
        int mod = 1, len = 1;
        while (mod % n != 0) {
            mod = (mod * 10 + 1) % n;
            len++;
        }
        cout << len << '\n';
    }
    return 0;
}