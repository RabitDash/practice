package com.rabitdash.rabyte;

import com.rabitdash.rabyte.Accounts.Account;
import com.rabitdash.rabyte.Accounts.LoanCreditAccount;
import com.rabitdash.rabyte.Accounts.LoanSavingAccount;
import com.rabitdash.rabyte.Accounts.SavingAccount;
import com.rabitdash.rabyte.Exception.ATMException;
import com.rabitdash.rabyte.Exception.RegisterException;
import com.rabitdash.rabyte.Util.ACCOUNT_TYPE;

public class Main {

    public static void main(String[] args) throws ATMException {
        // write your code here
        Bank b = Bank.getInstance();
        try {
            System.out.println(b.register(1, "1", "1", "1", "10@110", ACCOUNT_TYPE.SavingAccount));
            System.out.println(b.deposit(1, 100));
            System.out.println(b.register(2, "2", "3", "1", "1", ACCOUNT_TYPE.CreditAccount));
            System.out.println(b.setCeiling(2, 100));
            System.out.println(b.deposit(2, 300));
            System.out.println("sf" + ACCOUNT_TYPE.values()[0]);
        } catch (RegisterException e) {
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

