main: main.o Student.o Manager.o
	g++ obj/Student.o obj/Manager.o obj/main.o -o main
main.o: main.cpp
	g++ -c src/main.cpp -o main.o
Student.o: Student.cpp
	g++ -c src/Student.cpp -o Student.o
Manager.o: Manager.cpp
	g++ -c src/Manager.cpp -o Manager.o

