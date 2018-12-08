package com.rabyte.rabitdash;

public class Shape implements Sortable{
    double area;
    double getArea()
    {
        return area;
    }

    @Override
    public String toString() {
        return String.valueOf(area);
    }

    @Override
    public int compare(Sortable s) {

        if (this.area < ((Shape) s).area) {
            return -1;
        } else if (this.area > ((Shape) s).area)
        {
            return 1;
        }
        return 0;
    }
}
