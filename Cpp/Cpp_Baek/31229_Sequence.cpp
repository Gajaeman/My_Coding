#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;

    for (int i = 1; i <= N; ++i) {
        if (i > 1) cout << ' ';
        cout << (2*i - 1);
    }
    return 0;
}
