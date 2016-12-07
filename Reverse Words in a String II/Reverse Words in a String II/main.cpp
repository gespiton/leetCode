#include<iostream>
#include<vector>
#include<string>
using namespace std;

string reverse(string s);
void reverse(string& s, int bg, int ed);
int main(int args, const char* argv[]) {
	
	cout << reverse("you should try to do");

	system("pause");
	return 0;
}

string reverse(string s) {
	reverse(s, 0, s.size()-1);

	for (size_t i = 0; i < s.size(); i++)
	{
		int bg = i, ed = i;
		while (ed<s.size()&&s[ed]!=' ')
			++ed;
		reverse(s, bg, ed-1);
		i = ed;
	}

	return s;
}
void reverse(string& s,int bg, int ed) {
	int mid2 = ed+bg;
	int mid = mid2/2;
	for (size_t i = bg; i <= mid; i++)
	{
		auto buf = s[i];
		s[i] = s[mid2-i];
		s[mid2 - i] = buf;
	}
}

