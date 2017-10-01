#include <iostream>
using namespace std;

int main()
{
    cout << "Please enter two numbers" << endl;
    int x,y;
    cin >> x >> y;
    cout << "x:"<< x;
    cout << "y:"<< y;
    if(x < y)
    {
        cout << "fuck!" << endl;
        while(x <= y)
        {
            cout << x << endl;
            x++;
        }
    }
    else{
        cout << "shit!" << endl;
        while(y <= x)
        {
            cout << x << endl;
            x--;
        }
    }
}