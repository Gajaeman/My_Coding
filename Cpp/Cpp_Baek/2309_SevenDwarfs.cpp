#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> height(9);
    int sum = 0;
    for (int i = 0; i < 9; i++) {
        cin >> height[i];
        sum += height[i];
    }

    for (int i = 0; i < 8; i++) {
        for (int j = i + 1; j < 9; j++) {
            if (sum - height[i] - height[j] == 100) {

                vector<int> result;
                for (int k = 0; k < 9; k++) {
                    if (k != i && k != j) result.push_back(height[k]);
                }
                sort(result.begin(), result.end());
                for (int h : result) cout << h << '\n';
                return 0;
            }
        }
    }
}
''' #sol 2

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> ori(9);
vector<int> picked;
bool found = false;

void back(int idx, int cnt, int sum) {
    if (found) return;

    if (cnt == 7) {
        if (sum == 100) {
            sort(picked.begin(), picked.end());
            for (int i : picked)
                cout << i << '\n';
            found = true;
        }
        return;
    }

    for (int i = idx; i < 9; i++) {
        picked.push_back(ori[i]);
        back(i + 1, cnt + 1, sum + ori[i]);
        picked.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < 9; i++) cin >> ori[i];

    back(0, 0, 0);
    return 0;
}
'''