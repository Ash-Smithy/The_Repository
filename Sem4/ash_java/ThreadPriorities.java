import java.lang.*;

class A extends Thread
{
    public void run()
    {
        System.out.println("-- Starting of A");
        for(int i=1;i<=4;i++)
        {
            System.out.println("From Thread A: "+i);
        }
        System.out.println("-- Exit thread A --");
    }
}
class B extends Thread
{
    public void run()
    {
        System.out.println("-- Starting of B");
        for(int j=1;j<=4;j++)
        {
            System.out.println("From Thread B: "+j);
        }
        System.out.println("-- Exit thread B --");
    }
}
class C extends Thread
{
    public void run()
    {
        System.out.println("-- Starting of C");
        for(int k=1;k<=4;k++)
        {
            System.out.println("From Thread C: "+k);
        }
        System.out.println("-- Exit thread C --");
    }
}
class ThreadPriorities
{
    public static void main(String args[]) 
    {
        A ThreadA=new A();
        B ThreadB=new B();
        C ThreadC=new C();
        ThreadC.setPriority(Thread.MAX_PRIORITY);
        ThreadB.setPriority(Thread.NORM_PRIORITY);
        ThreadA.setPriority(Thread.MIN_PRIORITY);
        System.out.println("Start thread A");
        ThreadA.start();
        System.out.println("Start thread B");
        ThreadB.start();
        System.out.println("Start thread C");
        ThreadC.start();
        System.out.println("End of main thread");
    }
}