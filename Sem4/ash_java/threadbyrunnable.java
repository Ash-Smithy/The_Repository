//Program to implement runnable interfaces
class MyThread4 implements Runnable
{
    public void run()
    {
        for(int i=0;i<5;i++)
        {
            System.out.println("Class MyThread4: "+i);
        }
        System.out.println("Exit My Thread");
    }
}
class MyThread5 implements Runnable
{
    public void run()
    {
        for(int j=0;j<5;j++)
        {
            System.out.println("Class MyThread5: "+j);
        }
        System.out.println("Exit My Thread");
    }
}
class threadbyrunnable
{
    public static void main(String args[])
    {
        MyThread4 t4=new MyThread4();           // creating object
        Thread Thread4=new Thread(t4);          //Converting object to thread
        Thread4.start();
        MyThread5 t5=new MyThread5();           // creating object
        Thread Thread5=new Thread(t5);          //Converting object to thread
        Thread5.start();
        System.out.println("Exit main thread");
    }
}