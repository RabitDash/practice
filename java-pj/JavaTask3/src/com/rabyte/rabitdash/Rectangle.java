package com.rabyte.rabitdash;

public class Rectangle implements Sortable{
    int length;
    int width;
    int area;

    Rectangle()
    {
        length=width=area=0;
    }

    Rectangle(int length, int width)
    {
        this.length=length;
        this.width=width;
        this.area = length*width;
    }

    @Override
    public int compare(Sortable s)
    {
        if (this.area < ((Rectangle) s).area) {
            return 1;
        } else if (this.area > ((Rectangle) s).area)
        {
            return -1;
        }
        return 0;
    }

}
