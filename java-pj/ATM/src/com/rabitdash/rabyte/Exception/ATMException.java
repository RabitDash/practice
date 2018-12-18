package com.rabitdash.rabyte;

import javax.swing.*;

public class ATMException extends Exception {
    public ATMException() {
        super();
    }

    public ATMException(String message) {
        super(message);
    }

    @Override
    public void printStackTrace() {
        JOptionPane.showMessageDialog(null,this.getMessage(),"错误",JOptionPane.ERROR_MESSAGE);
    }

}




class LoginException extends ATMException {
    LoginException() {
        super();
    }

    LoginException(String message) {
        super(message);
    }
    @Override
    public void printStackTrace() {
        super.printStackTrace();
    }
}

class LoanException extends ATMException {
    LoanException() {
        super();
    }

    LoanException(String message) {
        super(message);
    }

    @Override
    public void printStackTrace() {
        super.printStackTrace();
    }
}
