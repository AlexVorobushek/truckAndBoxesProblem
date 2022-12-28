import models.Box;
import models.Truck;
import structsForSendToPython.BoxParams;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TruckClassMethodTest {
    @Test
    public void hasEnoughSpaceToPlaceTooBigBox(){
        Truck truck = new Truck(1.0, 1.0, 1.0 ,1.0, new BoxParams(10, 10, 10));
        Box tooBigBox = new Box(100, 100, 100, 1000);

        assertEquals(false, truck.hasEnoughSpaceToPlace(tooBigBox));
    }

    @Test
    public void givenPythonScript_whenPythonProcessInvoked_thenSuccess() throws Exception {
        ProcessBuilder processBuilder = new ProcessBuilder("python", resolvePythonScriptPath("hello.py"));
        processBuilder.redirectErrorStream(true);

        Process process = processBuilder.start();
        List<String> results = readProcessOutput(process.getInputStream());

        assertThat("Results should not be empty", results, is(not(empty())));
        assertThat("Results should contain output of script: ", results, hasItem(
        containsString("Hello Baeldung Readers!!")));

        int exitCode = process.waitFor();
        assertEquals("No errors should be detected", 0, exitCode);
    }

    @Test
    public void givenPythonInterpreter_whenPrintExecuted_thenOutputDisplayed() {
        try (PythonInterpreter pyInterp = new PythonInterpreter()) {
            StringWriter output = new StringWriter();
            pyInterp.setOut(output);

            pyInterp.exec("print('Hello Baeldung Readers!!')");
            assertEquals("Should contain script output: ", "Hello Baeldung Readers!!", output.toString()
            .trim());
        }
    }
}

