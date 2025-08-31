#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int x) {
    if (x < 2) return false;
    for (int i = 2; i <= sqrt(x); i++) {
        if (x % i == 0) return false;
    }
    return true;
}

int main() {
    int M, N;
    cin >> M >> N;

    int sum = 0, ch = -1;

    for (int i = M; i <= N; i++) {
        if (isPrime(i)) {
            sum += i;
            if (ch == -1) ch = i;
        }
    }

    if (ch == -1) {
        cout << -1;
    } else {
        cout << sum << '\n' << ch;
    }
}