
import java.util.Scanner;
public class Calculator {


    public static void main(String[] args) {
        Scanner user_choices = new Scanner(System.in);
        System.out.println("Please Choose the following options: \n 1. Addition\n 2. Subtraction\n 3. Multiplications\n 4. Division");


        int operation_choice = user_choices.nextInt();
        System.out.println("Please enter your number choices: ");

        float num1 = user_choices.nextFloat();
        float num2 = user_choices.nextFloat();

        switch (operation_choice) {
            case 1 -> System.out.println(addition(num1, num2));
            case 2 -> System.out.println(subtraction(num1, num2));
            case 3 -> System.out.println(multiplication(num1, num2));
            case 4 -> System.out.println(division(num1, num2));
            default -> System.out.println("Please enter numbers from 1 to 4!");
        }


    }

    private static float addition(float a, float b) {
        float additionanswer = a + b;

        return additionanswer;
    }

    private static float subtraction(float a, float b) {
        float subtractionanswer = a - b;

        return subtractionanswer;
    }

    private static float multiplication(float a, float b){
        float multiplicationanswer = a * b;

        return multiplicationanswer;
    }

    private static float division(float a, float b) {
        float divisionanswer =  a /  b;

        return divisionanswer;
    }



}
