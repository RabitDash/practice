#include <string>

class Student()
{
	public:

	Student(){} //default constructor

	Student(std::string ID, std::string Name, std::string Gender, std::string ClassNum, int Grade)
	{
		this->id = ID;
		this->name = Name;
		this->gender = Gender;
		this->classNum = ClassNum;
		this->grade = Grade;
	}

	bool operator> (const Student& stu)
	{
		return grade > stu.grade;
	}

	bool operator< (const Student& stu)
	{
		return grade < stu.grade;
	}

	bool operator== (const Student& stu)
	{
		return grade == stu.grade;
	}
	
	string _id;
	string _name;
	string _gender;
	string _classNum;
	int _grade;
}
