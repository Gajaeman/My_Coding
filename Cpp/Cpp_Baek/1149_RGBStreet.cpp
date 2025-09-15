#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; 
    cin >> n;

    int r = 0, g = 0, b = 0;
    for (int i = 0; i < n; ++i) {
        int R, G, B; 
        cin >> R >> G >> B;

        int nr = min(g, b) + R;
        int ng = min(r, b) + G;
        int nb = min(r, g) + B;

        r = nr; g = ng; b = nb;
    }
    cout << min(r, min(g, b));
    return 0;
}