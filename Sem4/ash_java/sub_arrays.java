public class sub_arrays {
    public static void main(String args[])
    {
        int a[][]={{1,3,4},{2,4,3},{1,2,4}};    
        int b[][]={{1,3,4},{2,4,3},{3,4,5}};   
        int s[][]={{0,0,0},{0,0,0},{0,0,0}};
        for(int i=0;i<3;i++)
            {    
                for(int j=0;j<3;j++)
                {
                    s[i][j]=b[i][j]-a[i][j];
                    System.out.print(s[i][j]+" ");
                }
                System.out.println();
            }     
    }    
}
