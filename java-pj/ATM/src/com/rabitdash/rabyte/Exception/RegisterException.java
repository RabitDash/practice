package com.rabitdash.rabyte;

import com.rabitdash.rabyte.Exception.ATMException;

class RegisterException extends ATMException {

    RegisterException() {
        super();
    }

    RegisterException(String message) {
        super(message);
    }
}
