#include <memory>
#include <ctime>
#include "tools.h"

int randInt(int a, int b)
{
	static int seed;
	return int(std::rand() % 10  * double(b - a)/10.0 + a);
}
