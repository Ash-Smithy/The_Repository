class sup
{
    int i,j;
    void showij()
    {
        System.out.println("from super class");
        System.out.println("i="+i);
        System.out.println("j="+j);
    }
}
class sec extends sup
{
    int k;
    void showijk()
   {
    System.out.println("from base class");
    System.out.println("i="+i);
    System.out.println("j="+j);
    System.out.println("k="+k);
    }
}
class single_ih
{
    public static void main(String args[])
    {
     sup oa=new sup();
     oa.i=10;
     oa.j=20;
     oa.showij();
     sec ob=new sec();
     ob.i=30;
     ob.j=40;
     ob.k=80;
     ob.showijk();
    }
}
