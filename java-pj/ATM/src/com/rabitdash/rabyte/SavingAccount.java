package com.rabitdash.rabyte;

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
    Account withdraw(double num) throws BalanceNotEnoughException{
        //是否透支
        if (num > this.getBalance())
        {
            throw new BalanceNotEnoughException("余额不足");
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
