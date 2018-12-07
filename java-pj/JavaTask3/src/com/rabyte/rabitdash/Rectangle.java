package com.rabyte.rabitdash;

public class Rectangle extends Shape implements Sortable{
    double length;
    double width;

    Rectangle()
    {
        length=width=area=0;
    }

    Rectangle(double length, double width)
    {
        this.length=length;
        this.width=width;
        this.area = length*width;
    }

    @Override
    public int compare(Sortable s)
    {
        if (this.area < ((Triangle) s).area) {
            return -1;
        } else if (this.area > ((Triangle) s).area)
        {
            return 1;
        }
        return 0;
    }

}
