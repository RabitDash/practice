package com.rabitdash.rabyte;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

public class Bank {


    private static volatile Bank instance = null;
    private static int nAccounts;// number of accounts
    private List<Account> accounts;

    private Bank() {
        accounts = new ArrayList<Account>();
        nAccounts = 0;
    }

    public static Bank getInstance() {
        if (instance == null) {
            synchronized (Bank.class) {
                if (instance == null) {
                    instance = new Bank();
                }
            }
        }
        return instance;
    }

    Account getAccountById(long id) {
        for (Account a : accounts) {
            if (a.getId() == id) {
                return a;
            }
        }
        throw new NoSuchElementException("未找到账户");

    }

    Account register(long id, String password, String name, String personId, String email, ACCOUNTTYPE type) throws RegisterException{
        Account account;
        switch (type) {
            case SavingAccount:
                account = new SavingAccount(id, password, name, personId, email);
                break;
            case CreditAccount:
                account = new CreditAccount(id, password, name, personId, email);
                ((CreditAccount) account).setCeiling(100);
                break;
            case LoanCreditAccount:
                account = new LoanCreditAccount(id, password, name, personId, email);
                break;
            case LoanSavingAccount:
                account = new LoanSavingAccount(id, password, name, personId, email);
                break;
            default:
                throw new RegisterException("未知账户类型");
        }
        accounts.add(account);
        nAccounts++;
        return account;
    }

    Account deposit(long id, double num) {
        return getAccountById(id).deposit(num);
    }

    Account withdraw(long id, double num) {
        Account account;
        try{
            account = getAccountById(id).withdraw(num);
            return account;
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
            return null;
        }
    }

    Account requestLoan(long id, double num) throws LoanException{
        Account account = getAccountById(id);
        if (account.type == ACCOUNTTYPE.LoanCreditAccount || account.type == ACCOUNTTYPE.LoanSavingAccount)
            ((Loanable) account).requestLoan(num);
        return account;
    }

    Account payLoan(long id, double num) throws LoanException{
        Account account = getAccountById(id);
        if (account.type == ACCOUNTTYPE.LoanCreditAccount || account.type == ACCOUNTTYPE.LoanSavingAccount)
            ((Loanable) account).payLoan(num);
        return account;
    }

    Account setCeiling(long id, double num) {
        Account account = getAccountById(id);
        if (account.type == ACCOUNTTYPE.CreditAccount || account.type == ACCOUNTTYPE.LoanCreditAccount) {
            ((CreditAccount) account).setCeiling(num);
            System.out.println("fuck");
        }
        return account;
    }

    boolean transfer(long from, long to, double money) {
        try {
            withdraw(from, money);
            deposit(to, money);
        } catch (Exception e) {
            return false;
        }
        return true;
    }

    Account login(long id, String password) throws LoginException{
        if (getAccountById(id).getPassword().equals(password))
            return getAccountById(id);
        throw new LoginException("账户名或密码错误");
    }

    double allBalance() {
        double sumBalance = 0.0;
        for (Account i : accounts) {
            sumBalance += i.getBalance();

        }
        return sumBalance;
    }

    double allCeiling() {
        double sumCeiling = 0.0;
        for (Account a : accounts) {
            if (a.type == ACCOUNTTYPE.CreditAccount || a.type == ACCOUNTTYPE.LoanCreditAccount)
                sumCeiling += ((CreditAccount) a).getCeiling();
        }
        return sumCeiling;
    }

    double allLoan() {
        double sumLoan = 0.0;
        for (Account a : accounts) {
            if (a.type == ACCOUNTTYPE.LoanCreditAccount || a.type == ACCOUNTTYPE.LoanSavingAccount)
                sumLoan += ((Loanable) a).getLoan();

        }
        return sumLoan;
    }


}
