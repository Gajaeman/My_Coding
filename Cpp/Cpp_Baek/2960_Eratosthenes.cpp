#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    vector<bool> erased(N+1, false);
    int cnt = 0;

    for (int i = 2; i <= N; i++) {
        if (!erased[i]) {
            for (int j = i; j <= N; j += i) {
                if (!erased[j]) {
                    erased[j] = true;
                    cnt++;
                    if (cnt == K) {
                        cout << j;
                        return 0;
                    }
                }
            }
        }
    }
}