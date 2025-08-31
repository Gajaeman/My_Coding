#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i*i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n, x, cnt = 0;
    cin >> n;
    while (n--) {
        cin >> x;
        if (isPrime(x)) cnt++;
    }
    cout << cnt;

    return 0;
}