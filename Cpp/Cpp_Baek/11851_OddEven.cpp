#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        long long x;
        cin >> x;
        long long root = sqrt(x);
        if (root * root == x) cout << 1 << ' ';
        else cout << 0 << ' ';
    }

    return 0;
}