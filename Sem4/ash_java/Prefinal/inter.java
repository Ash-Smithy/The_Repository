//Program to implement interface

interface area  //declaring interface
{
    static int l=0,w=0,h=0;
}
class cuboid implements area  //inheriting area interface in cuboid class
{
    int showa(int l,int w,int h)
    {
        return (l*w*h);
    }
}
class cube implements area //inheriting area interface in cube class
{
    int dispa(int l,int w, int h)
    {
        return (l*l*l);
    }
}
public class inter  //main class
{
    public static void main(String args[]) // main 
    {
        cuboid ob1=new cuboid(); //creating object for cuboid class
        cube ob2=new cube(); //creating object for cube class
        System.out.println("Are of cuboid: "+ob1.showa(4,5,6));
        System.out.println("Area of cube: "+ob2.dispa(3,3,3));
    }
}
