#include <iostream>
#include <string>
using namespace std;

int gcd(int a, int b){
    if(a==0) return b;
    return gcd(b%a, a);
}

int main(){
    int a = 0, b = 0;
    cin >> a >> b;

    int cnt = gcd(a,b);
    for(int i = 0; i < cnt; i++) {
        cout << '1';
    }
}