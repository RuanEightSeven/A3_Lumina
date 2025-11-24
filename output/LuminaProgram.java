import java.util.Scanner;

public class LuminaProgram {
    public static void main(String[] args) {
        Scanner __sc = new Scanner(System.in);
        int thoughts = 5;
        double clarity = 98.5;
        String idea = "Insight";
        System.out.println("Starting mental process...");
        if (clarity > 50) {
            {
                System.out.println("Mind is focused");
            }
        } else {
            {
                System.out.println("Mind is hazy");
            }
        }
        for (int i = 0; i < thoughts; i = i + 1) {
            {
                System.out.println("Processing thought " + i);
            }
        }
        while (clarity > 0) {
            {
                clarity = clarity - 5;
            }
        }
        idea = __sc.nextLine();
        System.out.println("Final idea: " + idea);
        __sc.close();
    }
}