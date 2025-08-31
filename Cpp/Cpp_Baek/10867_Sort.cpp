#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;
    int tc, n;
    cin >> tc;

    while (tc--) {
        cin >> n;
        s.insert(n);
    }

    for (int x : s) cout << x << " ";
}