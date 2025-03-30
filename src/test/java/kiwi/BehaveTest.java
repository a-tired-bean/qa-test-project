package kiwi;

import java.util.ArrayList;
import org.junit.jupiter.api.Test;

public class BehaveTest {

  @Test
  public void main() {
    ArrayList<String> command = new ArrayList<String>();
    command.add("behave");
    String includeTests = System.getProperty("include");
    if (includeTests != null) {
      command.add("-i");
      command.add(includeTests);
    }
    String excludeTests = System.getProperty("exclude");
    if (excludeTests != null) {
      command.add("-e");
      command.add(excludeTests);
    }
    ProcessBuilder processBuilder = new ProcessBuilder(command);
    processBuilder.redirectErrorStream(true);
    processBuilder.redirectOutput(ProcessBuilder.Redirect.INHERIT);
    try {
      Process process = processBuilder.start();
      process.waitFor();
    } catch (Exception exception) {
      exception.printStackTrace();
    }
  }

}
