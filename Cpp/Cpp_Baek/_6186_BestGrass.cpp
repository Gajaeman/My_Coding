#include <iostream>
#include <vector>
using namespace std;

int R, C;
vector<string> g;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

void dfs(int y, int x){
    g[y][x] = '.';
    for(int dir=0; dir<4; ++dir){
        int ny = y + dy[dir], nx = x + dx[dir];
        if(ny<0 || ny>=R || nx<0 || nx>=C) continue;
        if(g[ny][nx] == '#') dfs(ny, nx);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> R >> C;
    g.resize(R);
    for(int i=0;i<R;++i) cin >> g[i];

    int patches = 0;
    for(int i=0;i<R;++i){
        for(int j=0;j<C;++j){
            if(g[i][j] == '#'){
                ++patches;
                dfs(i, j);
            }
        }
    }
    cout << patches << '\n';
    return 0;
}