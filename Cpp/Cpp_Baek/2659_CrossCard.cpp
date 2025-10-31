#include <iostream>
#include <set>
#include <vector>

using namespace std;

int clock_num(int a, int b, int c, int d) {
    int n1 = 1000*a + 100*b + 10*c + d;
    int n2 = 1000*b + 100*c + 10*d + a;
    int n3 = 1000*c + 100*d + 10*a + b;
    int n4 = 1000*d + 100*a + 10*b + c;
    return min(min(n1, n2), min(n3, n4));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c, d;
    cin >> a >> b >> c >> d;

    int target = clock_num(a, b, c, d);

    set<int> uniq;
    for (int i = 1; i <= 9; ++i)
        for (int j = 1; j <= 9; ++j)
            for (int k = 1; k <= 9; ++k)
                for (int l = 1; l <= 9; ++l) {
                    uniq.insert(clock_num(i, j, k, l));
    }

    vector<int> all(uniq.begin(), uniq.end());

    int rank = lower_bound(all.begin(), all.end(), target) - all.begin() + 1;
    cout << rank << '\n';
    return 0;
}