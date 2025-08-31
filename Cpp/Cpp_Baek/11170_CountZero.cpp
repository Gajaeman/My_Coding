#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t; cin >> t;
        
    while(t--){
        int n, m; 
        cin >> n >> m;
        int cnt = 0;
        for(int i = n; i <= m; i++){
            int cal = i;
            if(cal == 0) cnt += 1;
            while(cal > 0){
                if(cal % 10 == 0) cnt++;
                cal /= 10;
            }
        }
        cout << cnt << '\n';
    }
    return 0;
}