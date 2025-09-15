#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    pair<int, int> arr[100001];
    for (int i = 0; i < N; i++) {
        cin >> arr[i].first >> arr[i].second;
    }

    sort(arr, arr + N, [](pair<int, int> a, pair<int, int> b) {
        if (a.first == b.first) return a.second > b.second;
        return a.first < b.first;
    });

    int day = 0, ans = 0;
    for (int i = 0; i < N; i++) {
        if (day < arr[i].first) {
            day++;
            ans += arr[i].second;
        } else if (arr[i].second > 0) {
            ans += arr[i].second - 1;
        }
    }
    cout << ans;
    return 0;
}