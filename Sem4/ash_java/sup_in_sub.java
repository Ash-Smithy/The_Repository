//Program to illustrate super in sub class
class a
{
    int i;
    void a(int j)
    {
        this.i=j;
        System.out.println(" in the constructor of super class");
    }
}
class super1 extends a
{
    int k;
    super1(int i,int k)
    {
        super();
        this.k=k;
        System.out.println("i= "+i);
        System.out.println("k= "+k);
    }
}
class sup_in_sub
{
    public static void main(String args[])
    {
        super1 ob=new super1(4,5);
    }
}