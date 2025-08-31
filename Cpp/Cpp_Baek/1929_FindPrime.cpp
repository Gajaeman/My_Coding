#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    cin >> M >> N;

    vector<bool> isPrime(N+1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i*i <= N; i++) {
        if (isPrime[i]) {
            for (int j = i*i; j <= N; j += i)
                isPrime[j] = false;
        }
    }

    for (int i = M; i <= N; i++)
        if (isPrime[i]) cout << i << '\n';
}


''' #sol_2
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    cin >> M >> N;

    vector<bool> isPrime(N+1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i <= N; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= N; j += i)
                isPrime[j] = false;
        }
    }

    for (int i = M; i <= N; i++) {
        if (isPrime[i]) cout << i << '\n';
    }
}
'''