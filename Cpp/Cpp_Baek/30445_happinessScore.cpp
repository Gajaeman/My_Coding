#include <iostream>
#include <cstring>
#include <iomanip>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s; getline(cin, s);
    long long hap = 0, sad = 0;
    for (char c : s) {
        if (strchr("HPY", c)) hap++;
        if (strchr("SD",  c)) sad++;
        if (c == 'A') { hap++; sad++; }
    }

    if (hap + sad == 0) {
        cout << "50.00\n";
    } else {
        long long total = hap + sad;
        long long res = (10000 * hap + total / 2) / total;
        cout << res / 100 << '.' << setw(2) << setfill('0') << res % 100 << '\n';
    }
}