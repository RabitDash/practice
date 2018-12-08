package pak2;

import pak1.One;

public class Two extends One {
    public static void main(String[] args) {
//        System.out.println(One.a); //a是私有成员，不可被外部类访问
        System.out.println(One.b); //b是保护成员，可以被本包子类和外部子类访问
        System.out.println(One.c); //c是公有成员，可以被任何类访问
    }
}
