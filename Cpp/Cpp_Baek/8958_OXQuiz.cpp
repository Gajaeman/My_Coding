#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    string inp;
    for(int i = 0; i < n; i++){
        int res, cal = 0;
        cin >> inp;
        for(int k = 0; k < inp.size(); k++){
            if(k==0){
                if(inp[0] == 'O'){
                    res = 1;
                    cal = 1;
                }
                else res = 0;
                }
            else{
                if(inp[k] == 'O'){
                    cal += 1;
                    res += cal;
                }
                else cal = 0;
            }
        }
        cout << res << endl;
    }
}