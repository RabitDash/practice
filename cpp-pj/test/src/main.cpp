#include <iostream>

using namespace std;

class Box
{
public:
	double length,breath,height;

	Box(double length, double breath, double height):length(length), breath(breath), height(height){
		cout<<"one object created!";
		cout<<endl;
	}
	~Box(){
		cout<<"one object destroyed!";
	}
};

int main(){
	Box box(12,34,12);
	cout << box.length <<endl << box.breath << endl <<box.height << endl;
	return 0;
}
