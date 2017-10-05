#include "easyLogger.h"
using namespace std;

int main(){
    cout << easyLogger::myInst()<<endl;
    easyLogger::myInst()->Log("shiyanlou logger test start");
    easyLogger::myInst()->Log("info info info");
    easyLogger::myInst()->Log("shiyanlou logger test end");
    return 0;
}
