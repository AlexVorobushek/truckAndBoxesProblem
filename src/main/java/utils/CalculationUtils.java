package utils;

import models.Box;
import models.StaticBox;
import models.Truck;
import structsForSendToPython.BoxParams;

import java.io.IOException;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;

public class CalculationUtils {
    public static boolean hasEnoughSpace(Box box, BoxParams boxParams){
        // TODO возвращает истинну, если коробка box можно разместить в параллепипеде с параметрами boxParams, иначе false
        return false;
    }

    public static Truck findBestTruckForTransportation(List<Truck> trucks, Box box, Double kmDistance){
        //todo выбирает наиболее выгодный грузовик из списка для доставки товара   
        return null;
    }

    private static void runPythonAlgorithm() throws IOException, InterruptedException{
        String pythonFilePatch = "src\\main\\python\\main.py";
        Process python_skript = Runtime.getRuntime().exec(new String[]{"python", pythonFilePatch});
        python_skript.waitFor();
    }

    public static boolean areBoxesIncluded() throws IOException, InterruptedException{
        CalculationUtils.runPythonAlgorithm();
        File file = new File("src\\main\\pythonJavaCommonDirectory\\pythonResult.txt");
        Scanner scanner = new Scanner(file);
        return scanner.nextLine().equals("True");
    }
}
