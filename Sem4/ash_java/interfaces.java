interface area
{
    final static float pi = 3.14F;
    float compute(float x,float y);
}
class rectangle implements area
{
    public float compute(float x,float y)
    {
        return (x+y);
    }
}
class circle implements area
{
    public float compute(float x,float y)
    {
        return pi*x*y;
    }
}
class interfaces
{
    public static void main(String args[])
    {
        rectangle rect = new rectangle();
        circle ci = new circle();
        System.out.println("Area of rectangle = "+rect.compute(10,20));
        System.out.println("Area of circle = "+ci.compute(10,10));

    }
}