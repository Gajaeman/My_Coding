#include <iostream>
using namespace std;

int count_arr[10001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, x;
    cin >> n;

    while (n--) {
        cin >> x;
        count_arr[x]++;
    }

    for (int i = 1; i <= 10000; i++) {
        while (count_arr[i]--) {
            cout << i << '\n';
        }
    }

    return 0;
}