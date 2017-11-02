#include <iostream>
using namespace std;

int main()
{
	string fuck;
	int n;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cin >> fuck;
		int lh = 0,rh = 0,ly = 0,ry = 0; //左花括号，右花括号，左圆括号，右圆括号
		for(int i = 0; i < fuck.size(); i++)
		{
			switch(fuck[i])
			{
				case '{':
					++lh;
					break;
				case '}':
					++rh;
					break;
				case '(':
					++ly;
					break;
				case ')':
					++ry;
					break;
			}
		}
		if((lh == rh) && (ly == ry))
		{
			cout << "Yes" << endl;
		}
		else
		{
			cout << "No" << endl;
		}
	}
	return 0;
}
