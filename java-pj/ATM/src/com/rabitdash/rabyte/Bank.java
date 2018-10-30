package com.rabitdash.rabyte;


import java.util.NoSuchElementException;

public class Bank {


    //    private static volatile Bank instance;
    private static int nAccounts;// number of accounts
    private Account[] Accounts;

    public Bank() {
        Accounts = new Account[100];
        nAccounts = 0;
    }

//    public static Bank getInstance() {
//        if (instance == null) {
//            synchronized (Bank.class) {
//                if (instance == null) {
//                    instance = new Bank();
//                }
//            }
//        }
//        return instance;
//    }

    Account register(long id, String password, String name, String personId, String email, accountType type) {
        Account account;
        switch (type) {
            case SavingAccount:
                account = new SavingAccount(id, password, name, personId, email);
                break;
            case CreditAccount:
                account = new CreditAccount(id, password, name, personId, email);
                ((CreditAccount) account).setCeiling(0L);
                break;
            default:
                throw new IllegalArgumentException("未知账户类型");
        }
        Accounts[nAccounts++] = account;
        return account;
    }

    Account deposit(long id, double num) {
        for (int i = 0; i < nAccounts; i++) {
            if (Accounts[i].getId() == id) {
                Accounts[i].deposit(num);
                return Accounts[i];
            }
        }
        throw new NoSuchElementException("未找到账户");
    }

    Account withdraw(long id, double num) {
        for (int i = 0; i < nAccounts; i++) {
            if (Accounts[i].getId() == id) {
                Accounts[i].withdraw(num);
                return Accounts[i];
            }
        }
        throw new NoSuchElementException("未找到账户");
    }

    Account setCeiling(long id, double num) {
        for (int i = 0; i < nAccounts; i++) {
            if (Accounts[i].getId() == id && Accounts[i].type == accountType.CreditAccount) {
                ((CreditAccount) Accounts[i]).setCeiling(num);
                return Accounts[i];
            }
        }
        throw new NoSuchElementException("未找到账户");
    }

    boolean transfer(long from, long to, double money) {
        try {
            for (int i = 0; i < nAccounts; i++) {
                if (Accounts[i].getId() == from) {
                    ((Account) Accounts[i]).withdraw(money);
                }
            }
        } catch (IllegalArgumentException e) {
            return false;
        }
        this.deposit(to, money);
        return true;

    }

    Account login(long id, String password) {
        for (int i = 0; i < nAccounts; i++) {
            if (Accounts[i].getId() == id && Accounts[i].getPassword().equals(password)) {
                return Accounts[i];
            }
        }
        throw new NoSuchElementException("未找到账户");
    }

    double allBalance() {
        double sumBalance = 0.0;
        for (int i = 0; i < nAccounts; i++) {
            sumBalance += Accounts[i].getBalance();
        }
        return sumBalance;
    }

    double allCeiling() {
        double sumCeiling = 0.0;
        {
            for (int i = 0; i < nAccounts; i++) {
                if (Accounts[i].type == accountType.CreditAccount) {
                    sumCeiling += ((CreditAccount) Accounts[i]).getCeiling();
                }
            }
        }
        return sumCeiling;
    }


}
