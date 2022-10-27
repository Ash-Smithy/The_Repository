package practicals;
import java.util.List;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;
class ComboTest {
 @Test
 void test() {
 
System.setProperty("webdriver.chrome.driver","(chromedriverpath)");
 ChromeDriver driver = new ChromeDriver();
 driver.get(combobox-html-file);
 
 Select dropDown = new 
Select(driver.findElement(By.id("cars")));
 List<WebElement> elementCount = dropDown.getOptions();
 System.out.println("Number of items : " + 
elementCount.size());
 }
}