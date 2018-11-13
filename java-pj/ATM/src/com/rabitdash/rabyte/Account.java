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

abstract interface Loanable {
    Account requestLoan(double money);

    Account payLoan(double money);

    double getLoan();
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

    @Override
    public String toString() {
        return String.format("id:%d\nbalance:%f\npersonid:%s\ntype:%s\n", id, balance, personId, type);
    }

    @Override
    public boolean equals(Object o) {

        return this.id == ((Account) o).getId();
    }
}

//储蓄账户
class SavingAccount extends Account {

    SavingAccount() {
        super();
        type = ACCOUNTTYPE.SavingAccount;
    }

    SavingAccount(long id, String password, String name, String personId, String email) {
        super(id, password, name, personId, email);
        type = ACCOUNTTYPE.SavingAccount;
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

    @Override
    public String toString() {
        return String.format("id:%d\nbalance:%f\npersonid:%s\ntype:%s\n", this.getId(), this.getBalance(), this.getPersonId(), type);
    }

    @Override
    public boolean equals(Object o) {

        return this.getId() == ((Account) o).getId();
    }
}

class LoanSavingAccount extends SavingAccount implements Loanable {
    private double loan;

    LoanSavingAccount() {
        super();
        type = ACCOUNTTYPE.LoanSavingAccount;
    }

    LoanSavingAccount(long id, String password, String name, String personId, String email) {
        super(id, password, name, personId, email);
        type = ACCOUNTTYPE.LoanSavingAccount;
    }

    @Override
    public Account requestLoan(double money) {
        this.loan += money;
        return this;
    }

    @Override
    public Account payLoan(double money) {
        this.withdraw(money);
        this.loan -= money;
        return this;
    }

    @Override
    public double getLoan() {
        return loan;
    }

    @Override
    public String toString() {
        return String.format("id:%d\nbalance:%f\npersonid:%s\ntype:%s\n", this.getId(), this.getBalance(), this.getPersonId(), type);
    }

    @Override
    public boolean equals(Object o) {

        return this.getId() == ((Account) o).getId();
    }
}

class CreditAccount extends Account {
    //    protected static ACCOUNTTYPE type = ACCOUNTTYPE.CreditAccount;
//    protected ACCOUNTTYPE type;
    protected double ceiling;

    CreditAccount() {
        super();
        this.ceiling = 0;
        type = ACCOUNTTYPE.CreditAccount;
    }

    CreditAccount(long id, String password, String name, String personId, String email) {
        super(id, password, name, personId, email);
        type = ACCOUNTTYPE.CreditAccount;
    }

    double getCeiling() {
        return ceiling;
    }

    void setCeiling(double ceiling) {
        this.ceiling = ceiling;
        System.out.println("fuck");
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

    @Override
    public String toString() {
        return String.format("id:%d\nbalance:%f\npersonid:%s\ntype:%s\n", this.getId(), this.getBalance(), this.getPersonId(), type);
    }

    @Override
    public boolean equals(Object o) {

        return this.getId() == ((Account) o).getId();
    }

}

class LoanCreditAccount extends CreditAccount implements Loanable {
    private double loan;

    LoanCreditAccount() {
        super();
        type = ACCOUNTTYPE.LoanCreditAccount;
    }

    LoanCreditAccount(long id, String password, String name, String personId, String email) {
        super(id, password, name, personId, email);
        type = ACCOUNTTYPE.LoanCreditAccount;
    }

    @Override
    public Account requestLoan(double money) {
        this.loan += money;
        return this;
    }

    @Override
    public Account payLoan(double money) {
        this.withdraw(money);
        this.loan -= money;
        return this;
    }

    @Override
    public double getLoan() {
        return loan;
    }

    @Override
    public String toString() {
        return String.format("id:%d\nbalance:%f\npersonid:%s\ntype:%s\n", this.getId(), this.getBalance(), this.getPersonId(), type);
    }

    @Override
    public boolean equals(Object o) {

        return this.getId() == ((Account) o).getId();
    }

}


//~ Formatted by Jindent --- http://www.jindent.com
