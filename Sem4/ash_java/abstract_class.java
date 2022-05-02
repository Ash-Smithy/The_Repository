abstract class A{
    abstract void amethod();
    void amethod1()
    {
        System.out.println("This is concrete method in abstract class");
    }
}
class B extends A{
    void amethod()
    {
        System.out.println("B's implementation of amethod abstract method");
    }
}
class abstract_class
{
    public static void main(String args[])
    {
        B b = new B();
        b.amethod();
        b.amethod1();
    }
}