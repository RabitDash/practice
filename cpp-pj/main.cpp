#include <iostream>

using namespace std;

class Box
{
public:
	double length,breath,height;

	Box(double length, double breath, double height):length(length), breath(breath), height(height){
		cout<<"one object created!";
	}
	~Box(){
		cout<<"one object destroyed!";
	}
};

int main(){
	Box box(12,34,12);
	return 0;
}
