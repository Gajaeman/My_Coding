#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int n; cin >> n;
        unordered_map<string, int> clothes;
        while (n--) {
            string name, type;
            cin >> name >> type;
            clothes[type]++;
        }
        long long ans = 1;
        for (auto &p : clothes) {
            ans *= (p.second + 1);
        }
        cout << ans - 1 << '\n';
    }
    return 0;
}