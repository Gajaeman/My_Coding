#include <iostream>
#include <vector>
using namespace std;

int main(){
    int inp;
    cin >> inp;
    for(int i=0; i<inp; i++){
        int lim;
        cin >> lim;
        vector<int> dp{1, 2, 4};
        for(int k = 0; k < lim - 3; k++){
            dp.push_back(dp[k] + dp[k+1] + dp[k+2]);
        }
        cout << dp[lim-1] << "\n";
    }
}