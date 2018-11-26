package com.rabitdash.rabyte;

public class Main {

    public static void main(String[] args) {
        // write your code here
        Bank b = Bank.getInstance();
        try
        {
            System.out.println(b.register(1, "1", "1", "1", "10@110", ACCOUNTTYPE.SavingAccount));
            System.out.println(b.deposit(1, 100));
            System.out.println(b.register(2, "2", "3", "1", "1", ACCOUNTTYPE.CreditAccount));
            System.out.println(b.setCeiling(2, 100));
            System.out.println(b.deposit(2, 300));
        }
       catch (RegisterException e)
       {
           System.out.println(e.getMessage());
       }
        System.out.println(b.allBalance());
        System.out.println(b.allCeiling());
        Account[] a = new Account[3];
        a[0] = new LoanCreditAccount();
        a[1] = new LoanSavingAccount();
        a[2] = new SavingAccount();
        System.out.println(a[0].type);
        System.out.println(a[1].type);
        System.out.println(a[2].type);

    }
}

