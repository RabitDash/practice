package com.rabitdash.rabyte;

/**
 * @author rabitdash
 */
enum accountType {
    SavingAccount, CreditAccount
}

abstract class Account {
    private static long id = 100000;
    accountType type;
    private String password;
    private String name;
    private String personId;
    private String email;
    private double balance;

    public Account() {
        balance = 0;
        id++;
    }

    public Account(long id, String password, String name, String personId, String email) {
        this.id++;
        this.password = password;
        this.name = name;
        this.personId = personId;
        this.email = email;
        this.balance = 0;
    }

    final Account deposit(double num) {
        this.balance += num;

        return this;
    }

    abstract Account withdraw(double num);

    public double getBalance() {
        return balance;
    }

    void setBalance(double balance) {
        this.balance = balance;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    long getId() {
        return id;
    }

    void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    String getPersonId() {
        return personId;
    }

    public void setPersonId(String personId) {
        this.personId = personId;
    }
}

//储蓄账户
class SavingAccount extends Account {
    public static final accountType type = accountType.SavingAccount;

    SavingAccount() {
        super();
    }

    SavingAccount(long id, String password, String name, String personId, String email) {
        super(id, password, name, personId, email);
    }

    @Override
    Account withdraw(double num) {
        //是否透支
        if (num > this.getBalance()) {
            return this;
        } else {
            this.setBalance(this.getBalance() - num);
            return this;
        }
    }
}

class CreditAccount extends Account {
    public static final accountType type = accountType.CreditAccount;
    private double ceiling;

    CreditAccount() {
        super();
        this.ceiling = 0;
    }

    CreditAccount(long id, String password, String name, String personId, String email) {
        super(id, password, name, personId, email);
    }

    double getCeiling() {
        return ceiling;
    }

    void setCeiling(double ceiling) {
        this.ceiling = ceiling;
    }

    @Override
    Account withdraw(double num) {
        //是否透支
        if (num > this.getBalance() + this.getCeiling()) {
            throw new IllegalArgumentException("余额不足");
        } else if (num > this.getBalance()) {
            this.setCeiling(this.getCeiling() + this.getBalance() - num);
            this.setBalance(0);
            return this;
        } else {
            this.setBalance(this.getBalance() - num);
            return this;
        }
    }


}









//~ Formatted by Jindent --- http://www.jindent.com
