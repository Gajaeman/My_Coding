#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    string str, com;
    cin >> str >> com;
    int idx = 0, ans = 0;

    sort(str.begin(), str.end());
    sort(com.begin(), com.end());

    while (str != com) {
        if (idx >= (int)str.size() || idx >= (int)com.size()) {
            if (str.size() > com.size()) {
                str.erase(idx, 1);
                ans++;
            } else if (com.size() > str.size()) {
                com.erase(idx, 1);
                ans++;
            } else {
                idx = 0;
            }
            continue;
        }

        if (str[idx] > com[idx]) {
            com.erase(idx, 1);
            ans++;
        } else if (str[idx] < com[idx]) {
            str.erase(idx, 1);
            ans++;
        } else {
            idx++;
        }
    }
    cout << ans;
    return 0;
}