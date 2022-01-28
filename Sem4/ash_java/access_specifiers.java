//access specifiers
class Test
{
    public int a;
    private int b;
    public void setb(int i)
    {
        b=i;
    }
    public int retb()
    {
        return b;
    }
}
public class access_specifiers
{
    public static void main(String args[])
    {
        Test t=new Test();
        t.a=10;
        //t.b=20; gives an error
        System.out.println("Public vairable access directly: "+t.a);
        t.setb(20);
        System.out.println("Private variable accessed thorugh the method: "+t.retb());
    }
}