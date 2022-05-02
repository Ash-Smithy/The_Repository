//Packages in java ~~ Package file
package MyPackage;
public class balance
{
    String name;
    double bal;
    public balance(String s, double b)
    {
        name = s;
        bal = b;
    }
    public void show()
    {
        if (bal<0)
        {
            System.out.println("-->");
        }
        System.out.println(name+":Rs"+bal);
    }
}
