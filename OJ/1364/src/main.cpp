#include <iostream>
#include <vector>
#define SWAP(a,b) (a)=(a)^(b);(b)=(b)^(a);(a)=(a)^(b);
using namespace std;

int insertScore(int num, vector < int >&score, vector < int >&number)
{
	for (int i = 0; i < score.size(); i++) {
		if (score.empty() && number.empty()) {
			score.push_back(num);
			number.push_back(1);
			return 0;
		}

		if (score[i] == num) {
			number[i] += 1;
			return 0;
		}
	}
	score.push_back(num);
	number.push_back(1);
	return 0;
}

int sortScore(vector < int >&score, vector < int >&number)
{
	for (int i = 0; i < score.size(); i++) {
		for (int j = 0; j < i; j++) {
			if (score[i] < score[j]) {
				SWAP(score[i], score[j]);
				SWAP(number[i], number[j]);
			}
		}
	}
	return 0;
}

int main()
{

	// score记录分数， number 记录人数
	int n;
	while (cin >> n) {
		vector < int >score;
		vector < int >number;
		int shit;
		for (int i = 0; i < n; i++) {
			cin >> shit;
			insertScore(shit, score, number);
		}
		sortScore(score, number);
		for (int i = 0; i < score.size(); i++) {
			cout << score[i] << " " << number[i] << endl;
		}
	}
	return 0;
}
