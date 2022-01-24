// public class Sample
// {
//     public static void main(String args[])
//     {
//         System.out.println("Hello World");
//     }
// }

//general form of a class
/*
class classname{
    type instance-variable1;
    type instance-variable2;
    ........
    type methodname1(parameter-list)
    {
        ....body of the method
    }
    type methodname2(parameter-list)
    {
        ....body of the method
    }
}
*/
//objects - instances 
//Instance is an occurrence of a class

//creating objects
/*
obtaining objects of a class is a two step process:
1.)Declare a variable of the class type
2.)Acquire an actual, physical copy of the object and assign it to that variable
To allocate a physical memory new() is used. It dynamically allocates memory for an object and returns a reference to it.
In Java, all class objects must be dynamically allocated
reference ----> address

syntax to create an object
Classname objname = new classname();
or
Classname objname; //declaration part
objname = new classname(); //allocate memory at runtime and returns the reference

*/

class Box
{
    //declaring instance variables : Numeric value initialized to 0
    //for other logical values or something : initialized to Null 
    double width;
    double height;
    double depth;
}
class BoxDemo
{
    public static void main(String args[])
    {
        Box mybox,mybox1; //declaration part
        mybox = new Box(); //allocation part
        mybox1 = new Box(); //allocation part
        mybox.width = 10;
        mybox.height = 20;
        mybox.depth = 15;

        mybox1.width = 10;
        mybox1.height = 25;
        mybox1.depth = 5;
        Box b2 = mybox;   //reference variable holds the memory address
                          //It is similar to the pointer
                          //Key difference - cannot manipulate as pointer
        System.out.println(" "+b2.height);

    }
}

class Student
{
    int rno; //instance variables, because they are created 
    //everytime and object is created and an object is
    // also called the instance of that class
    String name; //instead of using character array we use string datatype
}
class mainclass{
    public static void main(String args[])
    {
        Student s1 = new Student(); //the moment we create the object, there is memory allocated for that object
        Student s2 = new Student(); //the moment we created this object s2, there is memory allocated for that object
        s1.rno = 1;
        s1.name = "Jacob";
        
        s2.rno = 2;
        s2.name = "Joseph";
        System.out.println("Student 1 details : "+s1.rno+" "+s1.name);
        System.out.println("Student 2 details : "+s2.rno+" "+s2.name);
    
    }
}

/*
Command line arguments
Are the arguments that are passed to the main method 
from command prompt while executing the program with java command

P s v main(String args[]) //this refers that the main can also take arguemnts 
                          //in form of array of strings
{
    System.out.println("First argument : "+args[0]);
    System.out.println("Second arguemnt : "+args[1]);

}
*/
/*
C:/>javac name.java //compiling
C:/>java name arg1 arg2 arg3 //this statement calls main and main is where execution begins

*/class sample {
    
}
