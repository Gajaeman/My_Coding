#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, A, B;
    cin >> N >> A >> B >> M;
    int graph[101][101] = {0,};
    bool visited[101] = {false,};
    int ans = -1;
    for (int i = 0; i < M; i++) {
        int x, y;
        cin >> x >> y;
        graph[x][y] = 1;
        graph[y][x] = 1;
    }
    visited[A] = true;
    int q[10000] = {0,};
    int front = 0, rear = 0;
    q[rear++] = A;
    int level = 0;
    while (front < rear) {
        int qs = rear - front;
        for (int i = 0; i < qs; i++) {
            int cur = q[front++];
            if (cur == B) {
                ans = level;
                front = rear;
                break;
            }
            for (int j = 1; j <= N; j++) {
                if (graph[cur][j] == 1 && !visited[j]) {
                    visited[j] = true;
                    q[rear++] = j;
                }
            }
        }
        level++;
    }
    cout << ans;
    return 0;
}