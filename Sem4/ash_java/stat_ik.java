class work
{
    static int cnt;
    static void count()
    {
        System.out.println("Welcome");
        cnt = 0;
    }
    work()
    {
        cnt ++;
    }
}
class stat_ik
{
    public static void main(String[] args)
    {
     work t1=new work();
     System.out.println(work.cnt+" Objects are created");
     work t2=new work();
     System.out.println(work.cnt+" Objects are created");
     work t3=new work();
     System.out.println(work.cnt+" Objects are created"); 
    }
}