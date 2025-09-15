#include <iostream>
using namespace std;

int main(){
    int n, p, q, res = 0;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> p >> q;
        res += q % p;
    }
    cout << res;
    return 0;
}