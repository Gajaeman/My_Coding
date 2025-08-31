#include <iostream>
using namespace std;

int main() {
    int cnt = 0;

    for (int i = 0; i < 8; i++) {
        string row;
        getline(cin, row);

        for (int j = 0; j < 8; j++) {
            if ((i + j) % 2 == 0 && row[j] == 'F') {
                cnt++;
            }
        }
    }
    cout << cnt << '\n';
    return 0;
}