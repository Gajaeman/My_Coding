#include <iostream>
using namespace std;

int main() {
    int n, x, minVal = 1000001, maxVal = -1000001;
    cin >> n;
    while (n--) {
        cin >> x;
        if (x < minVal) minVal = x;
        if (x > maxVal) maxVal = x;
    }
    cout << minVal << ' ' << maxVal;

    return 0;
}