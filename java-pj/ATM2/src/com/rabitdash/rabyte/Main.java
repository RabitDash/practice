package com.rabitdash.rabyte;

public class Main {

    public static void main(String[] args) {
        // write your code here
        Bank b = Bank.getInstance();
        b.register(1,"1","1","1","10@110",accountType.SavingAccount);
        b.deposit(1,100);
    }
}

