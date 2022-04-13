package java_d3v;
class Test
{
    public int a;
    private int b;
    public void setb(int i)
    {
        b = i;
    }
    public int retb()
    {
        return b;
    }
}
public class access_specifiers {
    public static void main(String args[])
    {
        Test t = new Test();
        t.a = 10;
        System.out.println("Public variable access directly : "+t.a);
        //t.b = 20 //gives an error
        t.setb(20);
        System.out.println("Private variable access through the method: "+t.retb());
    }
}
