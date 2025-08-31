#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string jae, doc;
    cin >> jae >> doc;

    if(jae.length() >= doc.length()) cout << "go";
    else cout << "no";

    return 0;
}