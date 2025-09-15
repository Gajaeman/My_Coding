#include <iostream>
using namespace std;

int main(){
    int n;
    int a, b;
    cin >> n;
    while (n--){
        cin >> a >> b;
        cout << a+b << '\n';
    }
    return 0;
}

'''
#sol_2 (입출력 속도 향상)
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int A, B;
        cin >> A >> B;
        cout << A + B << '\n';
    }
    return 0;
}
'''

'''
#Sol_3 (C표준 입출력 방식)

#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    while (n--) {
        int A, B;
        scanf("%d %d", &A, &B);
        printf("%d\n", A + B);
    }
    return 0;
}
'''