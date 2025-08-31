#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;
    while(t--){
        int a, b, c, cnt = 0;
        cin >> a >> b >> c;
        for(int x = 1; x <= a; x++){
            for(int y = 1; y <= b; y++){
                for(int z = 1; z<= c; z++){
                    if(x%y == y%z && y%z == z%x) {
                        cnt += 1;
                    }
                }
            }
        }
    cout << cnt << '\n';
    }
}