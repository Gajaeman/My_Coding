#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    unordered_set<string> st;
    while (N--){
        string name, state;
        cin >> name >> state;
        if (state == "enter") st.insert(name);
        else st.erase(name);
    }
    vector<string> v(st.begin(), st.end());
    sort(v.rbegin(), v.rend());
    for (const auto& s : v) cout << s << '\n';
    return 0;
}

/* #sol_2 (시간 초과)
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<string> v;
    v.reserve(N);

    for (int i = 0; i < N; ++i){
        string name, state;
        cin >> name >> state;
        if (state == "enter"){
            v.push_back(name);
        } else {
            auto it = remove(v.begin(), v.end(), name);
            v.erase(it, v.end());
        }
    }

    sort(v.rbegin(), v.rend());
    for (const string& s : v){
        cout << s << '\n';
    }
    return 0;
}
*/
