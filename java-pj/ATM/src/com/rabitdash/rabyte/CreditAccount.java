package com.rabitdash.rabyte;

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
    Account withdraw(double num) throws BalanceNotEnoughException {
        //是否透支
        if (num > this.getBalance() + this.getCeiling()) {
            throw new BalanceNotEnoughException("透支余额不足");
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
