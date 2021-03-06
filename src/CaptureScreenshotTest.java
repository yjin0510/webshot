import java.io.File;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxBinary;
import org.openqa.selenium.firefox.FirefoxDriver;

public class CaptureScreenshotTest
{
    private static int      DISPLAY_NUMBER  = 99;
    private static String   XVFB            = "/usr/bin/Xvfb";
    private static String   XVFB_COMMAND    = XVFB + " :" + DISPLAY_NUMBER;
    private static String   URL             = "http://www.google.com";
    private static String   RESULT_FILENAME = "/tmp/screenshot.png";

    public static void main ( String[] args ) throws IOException
    {
        //Process p = Runtime.getRuntime().exec(XVFB_COMMAND);
        FirefoxBinary firefox = new FirefoxBinary();
        //firefox.setEnvironmentProperty("DISPLAY", ":" + DISPLAY_NUMBER);
	System.err.println("3");
        WebDriver driver = new FirefoxDriver(firefox, null);
	System.err.println("4");
        driver.get(URL);
	System.err.println("5");
        File scrFile = ( (TakesScreenshot) driver ).getScreenshotAs(OutputType.FILE);
	System.err.println("6");
        FileUtils.copyFile(scrFile, new File(RESULT_FILENAME));
	System.err.println("7");
        driver.close();
        //p.destroy();
    }
}

