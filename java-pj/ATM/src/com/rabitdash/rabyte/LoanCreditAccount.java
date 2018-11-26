package com.rabitdash.rabyte;

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
    public Account payLoan(double money) throws LoanException {
        try {
            this.withdraw(money);
        } catch (BalanceNotEnoughException e) {
            throw new LoanException(e.getMessage());
        }
        if (this.loan < money) {
            this.setBalance(money - this.loan);
            this.loan = 0.0;
        } else {
            this.loan -= money;
        }
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
