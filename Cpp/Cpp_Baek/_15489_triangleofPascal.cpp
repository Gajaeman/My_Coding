#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R,C,W; (cin>>R>>C>>W);
    int last = R + W - 1;

    vector<long long> row(last+2, 0);
    row[1] = 1;
    long long ans = 0;

    for(int i=1;i<=last;++i){
        if(i>1) for(int j=i;j>=1;--j) row[j] += row[j-1];
        if(i>=R){
            int L = C, Rt = C + (i - R);
            for(int j=L;j<=Rt;++j) ans += row[j];
        }
    }

    cout << ans << '\n';
}

/* sol_2(2차원 배열)
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, W; 
    if (!(cin >> R >> C >> W)) return 0;

    long long tri[35][35] = {};
    tri[1][1] = 1;
    int last = R + W - 1;
    for (int i = 2; i <= last; ++i)
        for (int j = 1; j <= i; ++j)
            tri[i][j] = (j==1 || j==i) ? 1 : tri[i-1][j-1] + tri[i-1][j];

    long long ans = 0;
    for (int i = 0; i < W; ++i)
        for (int j = 0; j <= i; ++j)
            ans += tri[R + i][C + j];

    cout << ans << '\n';
    return 0;
}
*/