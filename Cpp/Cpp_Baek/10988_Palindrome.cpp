#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    string word;
    cin >> word;

    string rev = word;
    reverse(rev.begin(), rev.end());
    

    if (word == rev) cout << 1;
    else cout << 0;

    return 0;
}