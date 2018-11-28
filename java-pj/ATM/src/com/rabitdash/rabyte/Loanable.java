package com.rabitdash.rabyte;

abstract interface Loanable{
    Account requestLoan(double money) throws LoanException;

    Account payLoan(double money) throws LoanException;

    double getLoan();
}
