class box{
    int x,y;
    void area()
    {
        System.out.println("x = "+x);
        System.out.println("y = "+y);
        System.out.println("area = "+(x*y));
    }
}
public class box1 {
    public static void main(String []args)
    {
        box b1 = new box();
        box b2 = new box();
        b1.x = 10;
        b1.y = 20;
        b2.x = 5;
        b2.y = 15;
        b1.area();
        b2.area();
    }
}
