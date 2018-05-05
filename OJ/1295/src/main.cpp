#include <iostream>
using namespace std;

class Vector2
{
public:
	Vector2(int a1, int a2)
	{
		x1 = a1;
		x2 = a2;
	}
	int x1;
	int x2;
};
		
	
void move(Vector2 from, Vector2 to)
{
	cout << from.x1 << "," << from.x2 << "-->" << to.x1 << "," << to.x2 << endl;
}

void fun(int n)
{
	if(n == 4)
	{
		cout << "4,5-->9,10"<< endl;

		cout << "8,9-->4,5"<< endl;

		cout << "2,3-->8,9"<< endl;

		cout << "7,8-->2,3"<< endl;

		cout << "1,2-->7,8"<< endl;
	}
	else
	{
		move(Vector2(n, n+1), Vector2(2*(n+1)-1, 2*(n+1)));
		move(Vector2(2*n-1, 2*n), Vector2(n, n+1));
		fun(--n);
	}
}

int main()
{
	int n;
	cin >> n;
	fun(n);
	return 0;
}
