package com.rabitdash.rabyte.Accounts;

import com.rabitdash.rabyte.Accounts.Account;
import com.rabitdash.rabyte.Exception.*;

public interface Loanable {
    Account requestLoan(double money) throws LoanException;

    Account payLoan(double money) throws LoanException;

    double getLoan();
}
