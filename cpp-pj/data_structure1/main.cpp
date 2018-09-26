#include <iostream>
#include <memory>
#include <cstdlib>

#define INIT_SIZE 100

using namespace std;
//复数定义
typedef struct{
    double real;
    double imag;
} Complex;

typedef struct {
    Complex* elem;
    int length; // num of elem
    int size; //size of list
} List;

//四则运算
void CAdd(Complex& res, Complex& a, Complex& b)
{
    res.real = a.real + b.real;
    res.imag = a.imag + b.imag;
}

void CSubtract(Complex& res, Complex& a, Complex& b)
{
    res.real = a.real - b.real;
    res.imag = a.imag - b.imag;
}

void CMultiply(Complex& res, Complex& a, Complex& b)
{
    res.real = a.real * b.real - a.imag * b.imag;
    res.imag = a.real * b.imag + a.imag * b.real;
}

void CDivide(Complex& res, Complex& a, Complex& b)
{
    double b_norm = b.real * b.real + b.imag * b.imag;
    res.real = b.real / b_norm;
    res.imag = b.imag / b_norm;
}

bool CEqual(Complex& a, Complex& b)
{
    return (a.real == b.real && a.imag == b.imag);
}

void InitList(List& l)
{
    l.elem = (Complex*)malloc(INIT_SIZE * sizeof(Complex));
    l.length = 0;
    l.size = INIT_SIZE;
}

void CreateList(List& l)
{
    cout << "Input 5 elems" << endl;
    for(int i = 0; i < 5; i++)
    {
        cout << "input>";
        cin >> l.elem[i].real >> l.elem[i].imag;
        l.length++;
    }

}

//顺序查找
void SearchList(List& l)
{
    Complex tmp;
    cout << "search>";
    cin >> tmp.real >> tmp.imag;
    for(int i = 0; i < l.length; ++i)
    {
        if(CEqual(l.elem[i], tmp))
        {
            cout << "find elem at " << i << endl;
            return;
        }
    }
    cout << "elem not found" << endl;
}

//哨兵法
void SearchList2(List& l)
{
    Complex tmp;
    cout << "search>";
    cin >> tmp.real >> tmp.imag;
    l.elem[l.length] = tmp;
    int i = 0;
    while(!CEqual(l.elem[i], tmp))
    {
        ++i;
    }
    //是否找到
    i == l.length? cout <<"elem not found" << endl : cout << "find elem at " << i << endl;
    //删除元素
    --l.length;
}
int main() {
    List l;
    InitList(l);
    CreateList(l);
    SearchList(l);
    SearchList2(l);
    return 0;
}