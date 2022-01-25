class classname
{
    int x=10,y=20;
    void putdata()
    {
        System.out.println("x="+x);
        System.out.println("y="+y);
    }
class jaba_class
{
    public static void main(String args[])
    {
        classname c1=new classname();
        c1.putdata();//calls the method for c1 object
    }
}
}