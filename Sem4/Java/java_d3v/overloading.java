package java_d3v;
/*
1.) Constructor overloading
2.) Method overloading
3.) Arrays

There are 2 types of constructors 
-> Default constructors
    -> We will not pass any parameters
    ->
-> Parameterized constructors
    ->We will pass parameters 
    ->

Method overloading
This is allowed in java
The methods are given the same name but different behavious
Name,return type and the count and type of arguments passed 

*/

class perimeter
{
    int length,breadth;
    //default constructor
    perimeter()
    {
        length = 0;
        breadth = 0;
    }
    //parameterized constructor 
    perimeter(int x,int y)
    {
        length = x;
        breadth = y;
    }
    void display()
    {
        System.out.println("Length = "+length+" Breadth = "+breadth+" Perimeter = "+(2*(length+breadth)));
    }
}
class method1 
{
    int add(int x,int y)
    {
        return (x+y);
    }
    void add(int x)
    {
        System.out.println("x+x="+(x+x));
    }
}

/*
Static data members and methods:
1.)Common variable for all the objects,
2.)It does not belong to any one object as such,
3.)There is only one copy of it available or created      
4.) Accessed with the classname

instance variables : Variables that are created for every object created,
and are accessed with the object name
Syntax for static variable 
"static returntype variablename;"

*/
class Mathoperation
{
    static float mul(float d,float e)
    {
        return (d*e);
    }
    static float divide(float x,float y)
    {
        return (x/y);
    }
}
public class overloading{
    public static void main(String args[])
    {
        //types of constructors
        perimeter p1 = new perimeter(); //default constructor
        perimeter p2 = new perimeter(10,20); //parameterized constructor
        p1.display();
        p2.display();
        //static methods and stuff
        float a = Mathoperation.mul((float)(4.0),(float)(5.0));
        float b = Mathoperation.divide((float)a,(float)2.0);
        System.out.println("B = "+b);
    }
}