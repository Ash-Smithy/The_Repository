package test;

import java.util.Scanner;
import java.io.*;

public class FileTest {
	public static void main(String arg[]) throws IOException
	{
		Scanner sc = new Scanner(new File("E:/Subjects/Sem 5/ST/Practical/TestCSV.csv"));
		sc.useDelimiter(",");
		while(sc.hasNext())
		{
			System.out.println(sc.next());
		}
		sc.close();
	}
}
