package com.rabitdash.rabyte;

/**
 * @author rabitdash
 */
class Account {
    private long id;
    private String password;
    private String name;
    private String personId;
    private String email;
    private double balance;

    public Account() {
        balance = 0;
    }

    public Account(long id, String password, String name, String personId, String email) {
        this.id = id;
        this.password = password;
        this.name = name;
        this.personId = personId;
        this.email = email;
        this.balance = 0;
    }

    Account deposit(double num) {
        this.balance += num;

        return this;
    }

    Account withdraw(double num) {
        this.balance -= num;

        return this;
    }

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

    private long ceiling;

    CreditAccount() {
        super();
        this.ceiling = 0;
    }

    CreditAccount(long id, String password, String name, String personId, String email, long ceiling) {
        super(id, password, name, personId, email);
        this.ceiling = ceiling;
    }

    @Override
    Account withdraw(double num) {
        return this;
    }


}


//~ Formatted by Jindent --- http://www.jindent.com
