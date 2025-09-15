#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    map<string, int> nameToNum;
    vector<string> numToName(N + 1);

    for (int i = 1; i<= N; i++){
        string name;
        cin >> name;
        nameToNum.insert({name, i});
        numToName[i] = name;
    }
    while (M--){
        string q;
        cin >> q;
        if (isdigit(q[0])){
            int num = stoi(q);
            cout << numToName[num] << "\n";
        } else {
            cout << nameToNum[q] << "\n";
        }
    }
}