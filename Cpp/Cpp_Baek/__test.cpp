#include <iostream>
#include <string>
using namespace std;

int main() {
    int num = 665, cnt = 0, n;
    cin >> n;
    while(cnt < n){
        num++;
        string s = to_string(num);
        if (s.find("666") != string::npos) {
            cnt ++;
        }
    }
    cout << num;
}