interface intf1
{
    int x=10;
    void m1();
}
interface intf2 extends intf1
{
    void m2(int i);
}
class abc implements intf2
{
    public void m1()
    {
        System.out.println("x = "+x);
    }
    public void m2(int i)
    {
        System.out.println("x*1= "+(x*i));
    }
    public static void main(String args[])
    {
        abc a=new abc();
        a.m1();
        a.m2(13);
    }
}