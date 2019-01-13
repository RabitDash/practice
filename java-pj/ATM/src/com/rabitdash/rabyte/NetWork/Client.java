<<<<<<< HEAD
package com.rabitdash.rabyte.NetWork;

import com.rabitdash.rabyte.NetWork.TO.TO;

import java.io.*;
import java.net.Socket;

public class Client {
    private Socket socket = null;
    private InputStream in = null;

    private OutputStream out = null;

    private ObjectOutputStream oos = null;

    private ObjectInputStream ois = null;

    public Client(Socket socket) {
        this.socket = socket;
        try {
            in = socket.getInputStream();
            out = socket.getOutputStream();
            oos = new ObjectOutputStream(out);
            ois = new ObjectInputStream(in);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

//    public static void main(String[] args) {
//        Socket socket = null;
//        String debugString = "rua";
//        try {
//            socket = new Socket("localhost", 9000);
//            Client client = new Client(socket);
//            System.out.println("Cilent send:" + new TO(ActionEnum.DEBUG, debugString));
//            client.sendMsg(new TO(ActionEnum.DEBUG, debugString));
//            System.out.println("Cilent receive:" + client.receiveMsg());
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }

    public boolean sendMsg(TO msg) {
        boolean success = false;
        try {
            oos.writeObject(msg);
            oos.reset();
            oos.flush();
            success = true;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return success;
    }

    public TO receiveMsg() {
        TO to = null;
        try {
            to = (TO) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return to;
    }
}
=======
package com.rabitdash.rabyte.NetWork;

import com.rabitdash.rabyte.NetWork.TO.TO;

import java.io.*;
import java.net.Socket;

public class Client {
    private Socket socket = null;
    private InputStream in = null;

    private OutputStream out = null;

    private ObjectOutputStream oos = null;

    private ObjectInputStream ois = null;

    public Client(Socket socket) {
        this.socket = socket;
        try {
            in = socket.getInputStream();
            out = socket.getOutputStream();
            oos = new ObjectOutputStream(out);
            ois = new ObjectInputStream(in);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

//    public static void main(String[] args) {
//        Socket socket = null;
//        String debugString = "rua";
//        try {
//            socket = new Socket("localhost", 9000);
//            Client client = new Client(socket);
//            System.out.println("Cilent send:" + new TO(ActionEnum.DEBUG, debugString));
//            client.sendMsg(new TO(ActionEnum.DEBUG, debugString));
//            System.out.println("Cilent receive:" + client.receiveMsg());
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }

    public boolean sendMsg(TO msg) {
        boolean success = false;
        try {
            oos.writeObject(msg);
            oos.reset();
            oos.flush();
            success = true;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return success;
    }

    public TO receiveMsg() {
        TO to = null;
        try {
            to = (TO) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return to;
    }
}
>>>>>>> dev
