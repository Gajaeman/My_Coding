#include <iostream>
#include <vector>
#include <functional>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; 
    if (!(cin >> N)) return 0;

    vector<int> L(26, -1), R(26, -1);
    vector<bool> isChild(26, false);

    for (int i = 0; i < N; ++i) {
        char p, l, r; 
        cin >> p >> l >> r;
        int pi = p - 'A';
        if (l != '.') { L[pi] = l - 'A'; isChild[l - 'A'] = true; }
        if (r != '.') { R[pi] = r - 'A'; isChild[r - 'A'] = true; }
    }

    int root = -1;
    for (int i = 0; i < 26; ++i) {
        if (!isChild[i] && (L[i] != -1 || R[i] != -1 || i == 0)) {
            root = i; break;
        }
    }
    if (root == -1) root = 0;

    function<void(int)> preorder = [&](int u){
        if (u == -1) return;
        cout << char('A' + u);
        preorder(L[u]);
        preorder(R[u]);
    };
    function<void(int)> inorder = [&](int u){
        if (u == -1) return;
        inorder(L[u]);
        cout << char('A' + u);
        inorder(R[u]);
    };
    function<void(int)> postorder = [&](int u){
        if (u == -1) return;
        postorder(L[u]);
        postorder(R[u]);
        cout << char('A' + u);
    };

    preorder(root);   cout << '\n';
    inorder(root);    cout << '\n';
    postorder(root);  cout << '\n';
    return 0;
}