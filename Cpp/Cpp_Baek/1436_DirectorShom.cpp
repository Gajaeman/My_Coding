#include <iostream>
#include <string>
using namespace std;

int main() {
    int num = 665, cnt = 0, n;
    cin >> n;
    while(cnt < n){
        num++;
        string s = to_string(num);
        if (s.find("666") != string::npos) {
            cnt ++;
        }
    }
    cout << num;
}
/*
pos는 size_t (unsigned)

-1은 int (signed)

비교할 때 int → size_t 변환 발생

이때 -1이 unsigned로 바뀌면서 엄청 큰 값이 됨

의도는 맞을 수도 있지만, 플랫폼/컴파일러/경고 설정에 따라 예상치 못한 버그나 경고 발생
*/