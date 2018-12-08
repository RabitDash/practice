package com.rabyte.rabitdash;

import java.util.Arrays;
import java.util.Random;
public class Main {
    private static void sortAndPrint(Shape[] shapes) {
        System.out.println("Before: ");
        for (Shape shape : shapes) {
            System.out.print(shape + " ");
        }
        System.out.println();
        Arrays.sort(shapes, Shape::compare);
        System.out.println("After: ");
        for (Shape shape : shapes) {
            System.out.print(shape + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // write your code here
        Shape[] shapes = new Shape[10];
        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            shapes[i] = new Triangle(random.nextDouble(), random.nextDouble(), random.nextDouble());
        }
        sortAndPrint(shapes);
        for (int i = 0; i < 10; i++) {
            shapes[i] = new Rectangle(random.nextDouble(), random.nextDouble());
        }
        sortAndPrint(shapes);


    }
}
