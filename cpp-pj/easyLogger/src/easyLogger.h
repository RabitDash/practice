#pragma once
#include <memory>
#include <ctime>
#include <iostream>
#include <fstream>

using namespace std;

class easyLogger
{
public:
    static easyLogger *myInst(){
        if (NULL == _instance.get()){
	    _instance = auto_ptr<easyLogger>(new easyLogger);
        }
        return _instance.get();
    }
    void Log(const string& logInfo);
private:
    easyLogger(void){}
    ~easyLogger(void){}
    friend class auto_ptr<easyLogger>;
    static auto_ptr<easyLogger> _instance;
};

void easyLogger::Log(const string& logInfo) {
    ofstream ofs;
    time_t t = time(0);
    char tmp[12];
    // [2017.07.12 13:50:36 Wednesday]
    strftime(tmp, sizeof(tmp), "[%Y.%m.%d %X %A]", localtime(&t));
    // write to easyLogger.log
    ofs.open("shiyanloulogger.log");
    ofs.write(logInfo.c_str(), logInfo.size());

    ofs << tmp;
    ofs.close();
}

