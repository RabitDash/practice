package com.rabitdash.rabyte;

/**
 * @author rabitdash
 */
enum ACCOUNTTYPE {
    SavingAccount,
    CreditAccount,
    LoanSavingAccount,
    LoanCreditAccount,
}

abstract class Account {
    private static long id = 100000;
    ACCOUNTTYPE type;
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
        this.id = id;
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

    abstract Account withdraw(double num) throws BalanceNotEnoughException;

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

    @Override
    public String toString() {
        return String.format("id:%d\nbalance:%f\npersonid:%s\ntype:%s\n", id, balance, personId, type);
    }

    @Override
    public boolean equals(Object o) {

        return this.id == ((Account) o).getId();
    }
}


//~ Formatted by Jindent --- http://www.jindent.com
