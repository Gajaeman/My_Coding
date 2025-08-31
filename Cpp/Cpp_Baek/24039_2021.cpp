#include <iostream>
#include <vector>
using namespace std;

bool isPrime(int x) {
    if (x < 2) return false;
    for (int i = 2; i * i <= x; i++) {
        if (x % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;

    vector<int> primes;
    for (int i = 2; i <= 1000; i++) {
        if (isPrime(i)) primes.push_back(i);
    }

    for (int i = 0; i+1 < primes.size(); i++) {
        long long prod = 1LL * primes[i] * primes[i+1];
        if (prod > n) {
            cout << prod;
            return 0;
        }
    }
}