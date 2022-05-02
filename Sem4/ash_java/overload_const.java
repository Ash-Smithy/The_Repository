class Box
{
    int l,w,h;
    Box(int l,int w,int h)
    {
        this.l=l;
        this.w=w;
        this.h=h;
    }
    Box(int k)
    {
        l=w=h=k;
    }
    int volume()
    {
        return (l*w*h);
    }
}
public class overload_const {
    public static void main(String a[])
    {
        Box b1=new Box(4,6,2);
        Box b2=new Box(4);
        System.out.println("Volume of cuboid: "+b1.volume());
        System.out.println("Volume of cube: "+b2.volume());
    }
}
