class circle
{
    double r;
    double pi=3.14;
    double ar;
    void area(double radius)
    {
        r=radius;
        ar=pi*r*r;
    }
}
public class circle1 {
    public static void main(String args[])
    {
        circle c = new circle();
        c.area(52);
        System.out.println("radius= "+c.r);
        System.out.println("area= "+c.ar);
        
    }
}
