#include <iostream>
#include <queue>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    priority_queue<int> maxHeap;

    int N;
    cin >> N;
    while(N--){
        long long x;
        cin >> x;
        if (x == 0){
            if(maxHeap.empty()) cout << "0\n";
            else {
                cout << maxHeap.top() << '\n';
                maxHeap.pop();
            }
        }
        else maxHeap.push(x);
    }
    return 0;
}