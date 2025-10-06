#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--){
        int N; string S1, S2;
        cin >> N >> S1 >> S2;

        int cnt1 = count(S1.begin(), S1.end(), 'W');
        int cnt2 = count(S2.begin(), S2.end(), 'W');
        int delta = abs(cnt1 - cnt2);

        int cal = 0;
        for(int j = 0; j < N; ++j)
            if(S1[j] != S2[j]) ++cal;

        cout << (cal + delta) / 2 << '\n';
    }
    return 0;
}


/* #sol_2
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int N; string S1, S2;
        cin >> N >> S1 >> S2;

        int bw = 0, wb = 0;
        for (int i = 0; i < N; ++i) {
            if (S1[i] == S2[i]) continue;
            if (S1[i] == 'B' && S2[i] == 'W') ++bw;
            else if (S1[i] == 'W' && S2[i] == 'B') ++wb;
        }
        cout << max(bw, wb) << '\n';
    }
    return 0;
}
*/