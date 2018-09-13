#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

class ZStyleArr
{
public:
  ZStyleArr (int N):width (N)
  {
    // 初始化矩阵 
    for (int i = 0; i < width; i++)
      {
	vector < int > tempA (width, 0);
	  zArr.push_back (tempA);
  }} ~ZStyleArr ()
  {
  }

  void display ()
  {
    fillArr ();
    cout << endl;
    for (int i = 0; i < width; i++)
      {
	for (int j = 0; j < width; j++)
	  cout << setfill (' ') << setw (3) << zArr[i][j] << " ";
	cout << endl;
      }
  }
private:
  void fillArr ()
  {
    int cols = 0, rows = 0;	// 行列坐标 
    int tempSum = 0, crSum = 0;	// 行列和 
    int filledNum = 0;		// 以填充的数量 
    int threshNum = (1 + width) * width / 2;	// 左上角至对角线的数量，大于该数量后，坐标的最小值将递增 
    // 

    int minRowIndex = 0, minColIndex = 0;	// 最小坐标 
    int arrSize = width * width;	// 矩阵大小 

    while (1)
      {
	rows = minRowIndex;	// 初始化行列坐标 
	cols = crSum - rows;

	while (1)
	  {
	    zArr[rows][cols] = ++filledNum;
	    rows += 1;		// 行坐标加1，下一行 
	    cols = crSum - rows;	// 每次循环，行列坐标的和不变,整个矩阵是对称的 
	    // 

	    if (rows > width - 1 || rows < minRowIndex
		|| cols < minColIndex || cols > width - 1)
	      {
		++crSum;	// 上一斜线上的坐标已经填充完成 
		// 
		if (filledNum >= threshNum)	// 填充总数超过对角线后，行列坐标的最小值会递增（不再是0） 
		  // 
		  {
		    ++minRowIndex;
		    ++minColIndex;
		  }
		break;
	      }
	  }
	// 填充总数达到后，退出循环 
	if (filledNum >= arrSize)
	  break;
      }
  }

  const int width;		// 矩形宽度 
  vector < vector < int > > zArr;
}
