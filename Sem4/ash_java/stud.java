class Student
{
    int id;
    String name;
    String add;
}
public class stud {
    public static void main(String []args)
    {
        Student s1  = new Student();
        Student s2 = new Student();
        s1.id = 1;
        s1.name = "Ash";
        s1.add = "Wakanda";
        s2.id = 2;
        s2.name = "Vamshi";
        s2.add = "Uppal";
        System.out.println("Student 1 : ");
        System.out.println("id = "+s1.id+" name : "+s1.name+" address : "+s1.add);
        System.out.println("Student 2 : ");
        System.out.println("id = "+s2.id+" name : "+s2.name+" address : "+s2.add);
    }
}
