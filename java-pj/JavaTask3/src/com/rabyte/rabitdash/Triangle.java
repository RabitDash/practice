package com.rabyte.rabitdash;
import java.lang.Math;
public class Triangle extends Shape implements Sortable{
    double a,b,c;

    Triangle()
    {
        a=b=c=area=0;
    }

    Triangle(double a, double b, double c)
    {
        this.a = a;
        this.b = b;
        this.c = c;
        var p = (a + b + c) / 2.0;
        this.area = Math.sqrt(p*(p-a)*(p-b)*(p-c));
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
