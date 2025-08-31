#include <iostream>
using namespace std;

int main() {
    int n, sum = 0;
    string s;
    cin >> n >> s;

    while(n--) sum += s[n] - '0';

    cout << sum << '\n';
    return 0;
}
