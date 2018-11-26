package com.rabitdash.rabyte;

class ATMException extends Exception {
    public ATMException() {
        super();
    }

    public ATMException(String message) {
        super(message);
    }
}

class BalanceNotEnoughException extends ATMException {
    public BalanceNotEnoughException() {
        super();
    }

    public BalanceNotEnoughException(String message) {
        super(message);
    }
}

class RegisterException extends ATMException {

    RegisterException() {
        super();
    }

    RegisterException(String message) {
        super(message);
    }
}

class LoginException extends ATMException {
    LoginException() {
        super();
    }

    LoginException(String message) {
        super(message);
    }
}

class LoanException extends ATMException {
    LoanException() {
        super();
    }

    LoanException(String message) {
        super(message);
    }
}
