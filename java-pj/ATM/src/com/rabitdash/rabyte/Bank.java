package com.rabitdash.rabyte;

import com.rabitdash.rabyte.Accounts.*;
import com.rabitdash.rabyte.Exception.ATMException;
import com.rabitdash.rabyte.Exception.LoanException;
import com.rabitdash.rabyte.Exception.LoginException;
import com.rabitdash.rabyte.Exception.RegisterException;
import com.rabitdash.rabyte.Util.ACCOUNT_TYPE;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.List;

public class Bank {


    private final static long startIdNum = 0;
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

    public static void main(String[] args) {
        getInstance().save();
    }

    Account getAccountById(long id) throws ATMException {
        for (Account a : accounts) {
            if (a.getId() == id) {
                return a;
            }
        }
        throw new ATMException("未找到账户");

    }

    public Account register(long id, String password, String name, String personId, String email, ACCOUNT_TYPE type) throws RegisterException {
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

    public Account register(String password, String name, String personId, String email, ACCOUNT_TYPE type) throws RegisterException {
        Account account;
        long id = startIdNum + nAccounts;
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

    public Account deposit(long id, double num) throws ATMException {
        return getAccountById(id).deposit(num);
    }

    public Account withdraw(long id, double num) {
        Account account;
        try {
            account = getAccountById(id).withdraw(num);
            return account;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return null;
        }
    }

    public Account requestLoan(long id, double num) throws LoanException, ATMException {
        Account account = getAccountById(id);
        if (account.type == ACCOUNT_TYPE.LoanCreditAccount || account.type == ACCOUNT_TYPE.LoanSavingAccount)
            ((Loanable) account).requestLoan(num);
        return account;
    }

    public Account payLoan(long id, double num) throws LoanException, ATMException {
        Account account = getAccountById(id);
        if (account.type == ACCOUNT_TYPE.LoanCreditAccount || account.type == ACCOUNT_TYPE.LoanSavingAccount)
            ((Loanable) account).payLoan(num);
        return account;
    }

    public Account setCeiling(long id, double num) throws ATMException {
        Account account = getAccountById(id);
        if (account.type == ACCOUNT_TYPE.CreditAccount || account.type == ACCOUNT_TYPE.LoanCreditAccount) {
            ((CreditAccount) account).setCeiling(num);
//            System.out.println("fuck");
        }
        return account;
    }

    public boolean transfer(long from, long to, double money) {
        try {
            withdraw(from, money);
            deposit(to, money);
        } catch (Exception e) {
            return false;
        }
        return true;
    }

    public Account login(long id, String password) throws LoginException, ATMException {
        if (getAccountById(id).getPassword().equals(password))
            return getAccountById(id);
        throw new LoginException("账户名或密码错误");
    }

    public double allBalance() {
        double sumBalance = 0.0;
        for (Account i : accounts) {
            sumBalance += i.getBalance();

        }
        return sumBalance;
    }

    public double allCeiling() {
        double sumCeiling = 0.0;
        for (Account a : accounts) {
            if (a.type == ACCOUNT_TYPE.CreditAccount || a.type == ACCOUNT_TYPE.LoanCreditAccount)
                sumCeiling += ((CreditAccount) a).getCeiling();
        }
        return sumCeiling;
    }

    public double allLoan() {
        double sumLoan = 0.0;
        for (Account a : accounts) {
            if (a.type == ACCOUNT_TYPE.LoanCreditAccount || a.type == ACCOUNT_TYPE.LoanSavingAccount)
                sumLoan += ((Loanable) a).getLoan();

        }
        return sumLoan;
    }

    public void save() {
        try {
            ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("id.ser"));
            out.writeObject(accounts);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void load() {

    }

}
