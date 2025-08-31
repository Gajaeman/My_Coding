#include <iostream>
using namespace std;

int main() {
    int maxVal = 0, idx = 0;
    for (int i = 1; i <= 9; i++) {
        int x;
        cin >> x;
        if (x > maxVal) {
            maxVal = x;
            idx = i;
        }
    }
    cout << maxVal << '\n' << idx << '\n';

    return 0;
}