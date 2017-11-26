1364:[2017 江苏科技大学 程序设计竞赛] D. 重复成绩统计 (改编)
难度： 秩序白银    时间限制： 1000MS   空间限制： 64MB   提交数： 110   通过数： 11
题目内容

[2017 江苏科技大学 程序设计竞赛]
D. 重复成绩统计 (改编)
题目描述

上海闵行膜法学院刚刚结束了高等膜法期中考试，现在有 N ( 0 < N < 1000000) 个学生的成绩需要统计，管理教学的长者们想要知道成绩的总体分布情况，请将不同分数的成绩和人数统计好并分别输出。
输入描述

有多组测试数据，每组测试数据占若干行。

在第 1 行中，有一个数字 N。

在第 2 到第 N + 1 行中，每行一个数字，代表这是一个学生的成绩。

所有数据保证在 32 位有符号整数范围内。
输出描述

每一行的输出格式为：成绩 取得这个成绩的人数。

注意：成绩和取得这个成绩的人数中间有一个空格! 同时，输出的时候。请按成绩的大小从低到高输出

由于数据量较大，请尽量使用时间复杂度较低的排序算法。
输入样例

5

45

45

45

60

60

6

100

60

100

100

50

60
输出样例

45 3

60 2

50 1

60 2

100 3
改编者留言

这题利用 STL 中的 sort 做显然不是最快的方法，你知道怎么做更快吗？ 滑稽