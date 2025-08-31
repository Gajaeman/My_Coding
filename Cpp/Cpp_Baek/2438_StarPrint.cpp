#include <iostream>
using namespace std;

int main(){
    int n, c;
    c = 0;
    cin >> n;
    while (n--){
        c++;
        cout << string(c, '*') << '\n';
    }
    return 0;
}