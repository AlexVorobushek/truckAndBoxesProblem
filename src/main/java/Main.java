import java.io.IOException;

import utils.CalculationUtils;

public class Main {

    public static void main(String[] args) throws IOException, InterruptedException {

        // var processBuilder = new ProcessBuilder("python", "hello.py");
        

        // processBuilder.redirectErrorStream(true);

        // Process process = processBuilder.start();
        // List<String> results = IOException.readProcessOutput(process.getInputStream());

        // assertThat("Results should not be empty", results, is(not(empty())));
        // assertThat("Results should contain output of script: ", results, hasItem(
        // containsString("Hello Baeldung Readers!!")));

        // int exitCode = process.waitFor();
        // assertEquals("No errors should be detected", 0, exitCode);
        System.out.println(CalculationUtils.areBoxesIncluded());
    }
}