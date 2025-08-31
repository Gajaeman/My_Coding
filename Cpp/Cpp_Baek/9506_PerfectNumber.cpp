#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    while (cin >> n && n != -1) {
        vector<int> div;
        int sum = 0;

        for (int i = 1; i <= n/2; i++) { 
            if (n % i == 0) {
                div.push_back(i);
                sum += i;
            }
        }

        if (sum == n) {
            cout << n << " = ";
            for (int i = 0; i < div.size(); i++) {
                cout << div[i];
                if (i != div.size() - 1) cout << " + ";
            }
            cout << '\n';
        } else {
            cout << n << " is NOT perfect." << '\n';
        }
    }
}