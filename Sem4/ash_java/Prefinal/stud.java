//Program to print student details using class concept

class student //creating a class student.
{
    int id;
    String name,addr;
}
public class stud 
{
    public static void main(String args[])
    {
        student s1=new student(); // Creating objects for student class 
        student s2=new student();  
        student s3=new student();
        System.out.println("Student 1 Details: ");
        s1.id=1;
        s1.name="Ash";
        s1.addr="Telangana";
        s2.id=2;
        s2.name="Smith";
        s2.addr="Tennessee";
        s3.id=3;
        s3.name="John";
        s3.addr="Kerala";
        System.out.println("Name: "+s1.name);
        System.out.println("ID: "+s1.id);
        System.out.println("From: "+s1.addr);
        System.out.println("Student 2 Details: ");
        System.out.println("Name: "+s2.name);
        System.out.println("ID: "+s2.id);
        System.out.println("From: "+s2.addr);
        System.out.println("Student 3 Details: ");
        System.out.println("Name: "+s3.name);
        System.out.println("ID: "+s3.id);
        System.out.println("From: "+s3.addr);
    }    
}
