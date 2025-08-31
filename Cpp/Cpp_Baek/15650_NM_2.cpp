#include <iostream>
using namespace std;

int n, m;
int arr[9];

void dfs(int idx, int start) {
    if (idx == m) {
        for (int i = 0; i < m; i++) cout << arr[i] << ' ';
        cout << '\n';
        return;
    }
    for (int i = start; i <= n; i++) {
        arr[idx] = i;
        dfs(idx + 1, i + 1);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    dfs(0, 1);
    return 0;
}