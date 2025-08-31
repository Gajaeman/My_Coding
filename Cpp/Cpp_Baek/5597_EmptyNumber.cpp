#include <iostream>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int num, arr[31] = {false};
    for(int i = 0; i < 28; i++){
        cin >> num;
        arr[num] = true;
    }
    
    for(int i = 1; i<=30; i++){
        if (!arr[i]) cout << i << '\n';
    }
    return 0;
}