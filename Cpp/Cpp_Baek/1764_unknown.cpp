#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    set<string> unheard;
    vector<string> ans;

    string name;
    for (int i = 0; i < N; i++) {
        cin >> name;
        unheard.insert(name);
    }
    
    for (int j = 0; j < M; j++) {
        cin >> name;
        if (unheard.count(name)) {
            ans.push_back(name);
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    for (auto &s : ans) cout << s << '\n';

    return 0;
}