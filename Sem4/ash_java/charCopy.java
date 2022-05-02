import java.io.*;

public class charCopy 
{
    public static void main(String args[])
    {
        File inFile=new File("file 1.txt");
        File outFile=new File("output.dat");
        FileReader ins=null;
        FileWriter outs=null;
        try 
        {
                ins=new FileReader(inFile);
                outs=new FileWriter(outFile);
                int ch;
                while((ch=ins.read()) !=-1)
                {
                    outs.write(ch);
                }
        }
        catch (IOException e) 
                {
                    System.out.println(e);
                    System.out.println(-1);
                }
        finally
                {
        try
        {
                        ins.close();
                        outs.close();
        }
                    catch(IOException e)
                    {
                        System.out.println(e);
                    }
                }
    }    
}
