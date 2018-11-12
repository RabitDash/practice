package com.rabitdash.rabyte;

public class Main {

    public static void main(String[] args) {
        // write your code here
        Bank b = Bank.getInstance();
        System.out.println(b.register(1, "1", "1", "1", "10@110", accountType.SavingAccount));
        System.out.println(b.deposit(1, 100));
        System.out.println(b.register(2, "2", "3", "1", "1", accountType.CreditAccount));
        System.out.println(b.setCeiling(2, 100));
        System.out.println(b.deposit(2, 300));
        System.out.println(b.allBalance());


    }
}

