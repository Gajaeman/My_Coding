#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Student {
    string name;
    int kor, eng, math;
};

bool cmp(const Student &a, const Student &b) {
    if (a.kor != b.kor) return a.kor > b.kor;
    if (a.eng != b.eng) return a.eng < b.eng;
    if (a.math != b.math) return a.math > b.math;
    return a.name < b.name;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<Student> v(N);

    for (auto &s : v) {
        cin >> s.name >> s.kor >> s.eng >> s.math;
    }

    sort(v.begin(), v.end(), cmp);

    for (auto &s : v) {
        cout << s.name << '\n';
    }
}

'''#sol 2
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	int n;
	cin >> n;

	vector<tuple<int, int, int, string>> data;
	while(n--) {
		string student;
		int lang, eng, math;
		cin >> student >> lang >> eng >> math;
		data.emplace_back(-lang, eng, -math, student);
	}

	sort(data.begin(), data.end());

	for (auto t : data) {
		cout << get<3>(t) << "\n";
	}
}
'''
