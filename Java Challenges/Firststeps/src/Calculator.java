
public class Calculator {


    public static void main(String[] args) {
        int operation = Integer.parseInt(args[0]);
        int num1 = Integer.parseInt(args[1]);
        int num2 = Integer.parseInt(args[2]);

        System.out.println(" Option 1. Addition \n Option 2. Subtraction \n Option 3. Multiplication \n Option 4: Division \n Option 5: Square \n Option 6: Cube \n Option 7: Multiply a to the power of b");

        switch (operation) {
            case 1 -> System.out.println(addition(num1, num2));
            case 2 -> System.out.println(subtraction(num1, num2));
            case 3 -> System.out.println(multiplication(num1, num2));
            case 4 -> System.out.println(division(num1, num2));
            case 5 -> System.out.println(square(num1));
            case 6 -> System.out.println(cube(num1));
            case 7 -> System.out.println(powerOf(num1,num2));
            default -> System.out.println("Please enter numbers from 1 to 7!");
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

    private static float square(float a) {
        float squareanswer = a*a;

        return squareanswer;

    }

    private static float cube(float a) {
        float cubeanswer = a*a*a;

        return cubeanswer;


    }

    private static double powerOf(double a, double b) {
        return (Math.pow(a,b));

    }
}
