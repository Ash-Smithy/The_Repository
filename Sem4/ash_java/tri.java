class triangle
{
    double b,h,a; 
    double area(double base, double height)
    {
        b=base;
        h=height;
        a=(b*h)/2;
        return a;
    }
}
class tri
{
    public static void main(String args[])
    {
        triangle t=new triangle();
        triangle t1=new triangle();
        double ar=t.area(3,4);
        System.out.println("Area of t= "+ar);
        System.out.println("Area of t1= "+t1.area(5,6));
    }
}