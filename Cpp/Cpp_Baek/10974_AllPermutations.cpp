#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    int a[9];
    for (int i = 0; i < n; i++) a[i] = i + 1;
    do {
        for (int i = 0; i < n; i++) {
            cout << a[i] << (i + 1 == n ? '\n' : ' ');
        }
    } while (next_permutation(a, a + n));
    return 0;
}