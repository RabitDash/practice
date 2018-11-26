package com.rabyte.rabitdash;
import java.util.Arrays;
import java.util.Random;
public class Main {
    public static void main(String[] args) {
	// write your code here
        Random random = new Random();
        Student[] students = new Student[10];
        for (int i = 0; i < 10; i++)
        {
            students[i] = new Student(i, random.nextInt(100));
        }
        System.out.println("Before: ");
        for(Student stu:students)
        {
            System.out.print(stu.score + " ");
        }
        Arrays.sort(students, Student::compare);
        System.out.println();
        System.out.println("After: ");
        for(Student stu:students)
        {
            System.out.print(stu.score + " ");
        }
        System.out.println();
        Rectangle[] rectangles = new Rectangle[10];
        for (int i = 0; i < 10; i++)
        {
            rectangles[i] = new Rectangle(random.nextInt(20), random.nextInt(20));
        }
        System.out.println("Before: ");
        for(Rectangle rect:rectangles)
        {
            System.out.print(rect.area + " ");
        }
        Arrays.sort(rectangles, Rectangle::compare);
        System.out.println();
        System.out.println("After: ");
        for(Rectangle rect:rectangles)
        {
            System.out.print(rect.area + " ");
        }


    }
}
