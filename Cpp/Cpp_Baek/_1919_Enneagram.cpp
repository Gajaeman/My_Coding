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
        // 한쪽 끝까지 왔으면, 더 긴 쪽에서 현재 위치의 문자 삭제
        if (idx >= (int)str.size() || idx >= (int)com.size()) {
            if (str.size() > com.size()) {
                str.erase(idx, 1);
                ans++;
            } else if (com.size() > str.size()) {
                // str이 더 짧음 → com[idx]를 지움
                com.erase(idx, 1);
                ans++;
            } else {
                // 같은 길이인데 여기 왔다? 이론상 불가하지만 안전장치
                idx = 0;
            }
            // 길이가 줄었으니 다음 비교로
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
}
