#include <bits/stdc++.h>
using namespace std;

static bool A[50][50];
static int qx[2500], qy[2500];
const int dx[4]={1,0,-1,0}, dy[4]={0,1,0,-1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while(T--){
        int M,N,K; cin >> M >> N >> K;
        vector<pair<int,int>> pos; pos.reserve(K);
        for(int i=0;i<K;i++){ int x,y; cin>>x>>y; A[y][x]=true; pos.emplace_back(x,y); }

        int ans=0;
        for(auto [sx,sy]: pos){
            if(!A[sy][sx]) continue;
            ans++;
            int h=0,t=0; qx[t]=sx; qy[t]=sy; t++; A[sy][sx]=false;
            while(h<t){
                int x=qx[h], y=qy[h]; h++;
                for(int d=0; d<4; d++){
                    int nx=x+dx[d], ny=y+dy[d];
                    if(nx<0||ny<0||nx>=M||ny>=N||!A[ny][nx]) continue;
                    A[ny][nx]=false; qx[t]=nx; qy[t]=ny; t++;
                }
            }
        }

        for(auto [x,y]: pos) A[y][x]=false;

        cout << ans << '\n';
    }
    return 0;
}