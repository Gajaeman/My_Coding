#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(long long x) {
    if (x < 2) return false;
    if (x == 2) return true;
    if (x % 2 == 0) return false;
    for (long long i = 3; i*i <= x; i += 2) {
        if (x % i == 0) return false;
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long n;
        cin >> n;
        while (!isPrime(n)) n++;
        cout << n << '\n';
    }
}