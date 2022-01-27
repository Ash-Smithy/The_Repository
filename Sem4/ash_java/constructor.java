class Rectangle_to {
    int l,b;
    Rectangle_to(int x,int y)
    {
        l=x;
        b=y;
    }
    int rtarea()
    {
        int a=l*b;
        return (a);
    }
}
public class constructor {
    public static void main(String args[])
    {
        Rectangle_to r1=new Rectangle_to(10,5);
        int area1=r1.rtarea();
        System.out.println("Area of rectangle = "+area1); //constructor is getting valled and values are passed
        Rectangle_to r2=new Rectangle_to(20,5); //calls rtarea and return area value back
        int area2=r2.rtarea();
        System.out.println("Area of rectangle = "+area2);
    }
}
