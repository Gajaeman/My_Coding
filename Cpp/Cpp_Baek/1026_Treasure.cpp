// BOJ 1026 Treasure: sort A asc, B desc, sum products
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; 
    cin >> n;
    vector<int> A(n), B(n);
    for (int &x : A) cin >> x;
    for (int &x : B) cin >> x;

    sort(A.begin(), A.end()); 
    sort(B.begin(), B.end(), greater<int>());

    long long ans = 0;
    for (int i = 0; i < n; i++) ans += A[i] * B[i];
    cout << ans << '\n';
}