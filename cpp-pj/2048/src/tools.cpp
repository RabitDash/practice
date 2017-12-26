#include <memory>
#include <ctime>

int randInt(int a, int b)
{
	return int(std::rand() % 10  * double(b - a)/10.0 + a);
}

