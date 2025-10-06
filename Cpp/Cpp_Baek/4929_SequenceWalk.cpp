#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
ll v1[10001];
ll v2[10001];
ll hap[10001];
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    while (true) {
        int s1 = 0, s2 = 0, num = 0, st1 = 0;
        int st2 = 0, ed1=0, ed2=0, cal1 = 0, cal2 = 0;
        int rst = 0;
        cin >> s1;
        if (s1 == 0) {
            return 0;
        }
        for (int i = 0; i < s1; i++) {
            cin >> num;
            v1[i] = num;
        }
        cin >> s2;
        for (int i = 0; i < s2; i++) {
            cin >> num; 
            v2[i] = num;
        }
        for (int i = 0; i < s1; i++) {
            for (int j = 0; j < s2; j++) {
                if (v1[i] == v2[j]) {
                    cal1 = 0; cal2 = 0;
                    ed1 = i; 
                    ed2 = j;
                    for (int p = st1; p < ed1; p++) {
                        cal1 += v1[p];
                    }
                    st1 = ed1;
                    for (int p = st2; p < ed2; p++) {
                        cal2 += v2[p];
                    }
                    st2 = ed2;
                    rst += max(cal1, cal2);
                }
            } 
        }
        cal1 = 0; cal2 = 0;
        for (int i = st1; i < s1; i++) {
            cal1 += v1[i];
        }
        for (int i = st2; i < s2; i++) {
            cal2 += v2[i];
        }
        rst += max(cal1, cal2);
        cout << rst << endl;
    }
    return 0;
}