#include <iostream>
#include <string>
using namespace std;

int main() {
    string N;
    cin >> N;
    long long num = stoll(N);
    int cnt = 0;
    while (num) {
        size_t pos = N.find('1');
        if (pos != string::npos) N.erase(pos, 1);
        else N = to_string(--num);
        cnt++;
        if (!N.size()) break;
        num = stoll(N);
    }
    cout << cnt;
}
