#include <iostream>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--){
        int N, M; 
        cin >> N >> M;

        vector<long long> row(N, 0), col(N, 0);
        for (int i = 0; i < N; ++i){
            for (int j = 0; j < N; ++j){
                long long x; cin >> x;
                row[i] += x;
                col[j] += x;
            }
        }

        vector<long long> dRow(N+1, 0), dCol(N+1, 0);

        for (int q = 0; q < M; ++q){
            int r1, c1, r2, c2; long long v;
            cin >> r1 >> c1 >> r2 >> c2 >> v;

            int rows = r2 - r1 + 1;
            int cols = c2 - c1 + 1;

            long long addRow = v * cols;
            long long addCol = v * rows;

            dRow[r1-1] += addRow;
            dRow[r2]   -= addRow;

            dCol[c1-1] += addCol;
            dCol[c2]   -= addCol;
        }

        long long acc = 0;
        for (int i = 0; i < N; ++i){ acc += dRow[i]; row[i] += acc; }
        acc = 0;
        for (int j = 0; j < N; ++j){ acc += dCol[j]; col[j] += acc; }

        for (int i = 0; i < N; ++i){ if (i) cout << ' '; cout << row[i]; }
        cout << '\n';
        for (int j = 0; j < N; ++j){ if (j) cout << ' '; cout << col[j]; }
        cout << '\n';
    }
    return 0;
}