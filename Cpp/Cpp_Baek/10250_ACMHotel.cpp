#include <iostream>
using namespace std;

int main() {
    int t, h, w, n;
    cin >> t;
    while (t--) {
        cin >> h >> w >> n;
        int y = (n - 1) % h + 1;
        int x = (n - 1) / h + 1;
        printf("%d%02d\n", y, x);
    }

    return 0;
}