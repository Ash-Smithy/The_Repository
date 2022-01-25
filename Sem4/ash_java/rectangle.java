class Rect {
    int l,b;
    void getdata(int x,int y)
    {
        l=x;
        b=y;
    }
    int area()
    {
        int a=l*b;
        return(a);
    }
}
public class rectangle
{
    public static void main(String args[])
    {
        Rect r1=new Rect();
        r1.getdata(10,5);
        int area=r1.area();
        System.out.println("Area of rectangle is: "+area);
    }
}