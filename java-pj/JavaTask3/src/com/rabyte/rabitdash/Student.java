package com.rabyte.rabitdash;

class Student implements Sortable {
    long id;
    int score;

    Student(long id, int score) {
        this.id = id;
        this.score = score;
    }

    @Override
    public int compare(Sortable s) {
        if (this.score < ((Student) s).score) {
            return 1;
        } else if (this.score > ((Student) s).score) {
            return -1;
        }
        return 0;
    }

}
