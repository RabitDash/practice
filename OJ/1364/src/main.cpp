#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector<int> score;
	vector<int> number;
	// score记录分数， number 记录人数
	int n;
	while(cin >> n)
	{
		int shit;
		for(int i = 0; i < n; ++i)
		{
			cin >> shit;
			if(score.empty() || score[score.size() - 1] == shit)
			{
				score.push_back(shit);
				number.push_back(1);
			}
			else
				//TODO
