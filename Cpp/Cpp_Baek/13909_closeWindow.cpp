#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, cal;
    cin >> N;
    while (cal * cal <= N) cal++;

    cout << cal - 1;
    return 0;
}