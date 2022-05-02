//JTable Demo

import java.awt.*;
import javax.swing.*;

public class JTableDemo extends JApplet
{
    public void init()
    {
            Container cp = getContentPane();
            cp.setLayout(new FlowLayout());
            String[]colHeads= {"Name","Extension","ID#"};
            Object[][] data={{"Sandeep","4567","42"},{"Ravi","7566","43"}};
            JTable table=new JTable(data,colHeads);
            JScrollPane jsp=new JScrollPane(table);
            add(jsp);
    }
}
