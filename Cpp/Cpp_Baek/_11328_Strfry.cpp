#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    while (n--) {
        string a, b;
        cin >> a >> b;

        if (a.size() != b.size()) {
            cout << "Impossible\n";
            continue;
        }

        int count[26] = {0};
        for (char c : a) count[c - 'a']++;
        for (char c : b) count[c - 'a']--;

        bool possible = true;
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                possible = false;
                break;
            }
        }

        cout << (possible ? "Possible" : "Impossible") << '\n';
    }

    return 0;
}