/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package seleniumjava;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    @Test public void appHasAGreeting() {
        App classUnderTest = new App();
        assertNotNull("app should be running", classUnderTest.running());
    }
}
