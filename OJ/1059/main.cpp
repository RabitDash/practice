#include <iostream>
#include <vector>
using namespace std;

int dp(vector<vector<int> > mat, int n)
{
	for(int i = 2; i <= n; i++)
	{
		for(int j = 1; j <= i; j++)
		{
				if( 1 == j)//左边界线上的元素
					mat[i][j] = mat[i-1][j] + mat[i][j];
				if( i == j)//右边界线上的元素
					mat[i][j] = mat[i-1][j-1] + mat[i][j];
				else
				{
					mat[i][j] = (mat[i-1][j-1] < mat[i-1][j] ? mat[i-1][j-1] : mat[i-1][j]) + mat[i][j];//该节点和 = [左父亲和 + 右父亲和]min + 该节点值
				}
		}
	}
	int min;
	min = mat[n][1];
	for(int j = 2; j <= n; j++)
	{
		min = (min < mat[n][j]? min : mat[n][j]);
	}
	return min;
}
int main()
{
	int n;
	while(cin >> n)
	{
		int tmp;
		vector<vector<int> > mat;
		mat.resize(n+1);
		for(int i = 0; i < n+1; i++)
		{
			mat[i].resize(n+1);
		}
		for(int i =1; i <= n; i++)
		{
			for(int j = 1; j <= i; j++)
			{
				cin >> tmp;
				mat[i][j] = tmp;
			}
		}

		cout << dp(mat, n)<< endl;
	}
}
