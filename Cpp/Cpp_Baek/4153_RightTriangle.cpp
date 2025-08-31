#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    while (true) {
        int a, b, c;
        cin >> a >> b >> c;
        if (a == 0 && b == 0 && c == 0) break;

        int sides[3] = {a, b, c};
        sort(sides, sides + 3);

        if (sides[2]*sides[2] == sides[0]*sides[0] + sides[1]*sides[1])
            cout << "right\n";
        else
            cout << "wrong\n";
    }
    
    return 0;
}