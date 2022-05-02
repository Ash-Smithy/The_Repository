import java.io.*;

class prac
{
    public static void main(String a[]) throws IOException
    {
       FileInputStream f=new FileInputStream("output.txt");
       int size=f.available();
       int nwords=0;
       int nlines=0;
       char ch;
       for(int i=0;i<size;i++)
       {
        ch=(char)f.read();
        System.out.println(ch);
        if(ch==' ') nwords++;
        if(ch== '\n') nlines++;
       }
       nwords++;
       System.out.println("Number of characters= "+size);
       System.out.println("No of words: "+nwords);
       System.out.println("No of lines: "+nlines);
    }    
}