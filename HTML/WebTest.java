package test;
import org.junit.Test;
import org.openqa.selenium.chrome.ChromeDriver;

public class WebTest {
	
	@Test
	public void Test()
	{
		System.setProperty("webdriver.chrome.driver","E:\\Subjects\\Sem 5\\ST\\Selenium Projects\\chromedriver.exe");
		ChromeDriver driver = new ChromeDriver();
		driver.get("E:\\Subjects\\Sem 5\\ST\\Practical\\ATestPage.html");
	}
	
}
