package com.rabitdash.rabyte;
import com.rabitdash.rabyte.Accounts.Account;
import com.rabitdash.rabyte.Exception.*;
public abstract interface Loanable{
    public Account requestLoan(double money) throws LoanException;

    public Account payLoan(double money) throws LoanException;

    public double getLoan();
}
