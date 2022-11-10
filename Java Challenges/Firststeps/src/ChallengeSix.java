import java.util.Scanner;

public class ChallengeSix {
    public static void main(String[] args) {
        Scanner userChoic = new Scanner(System.in);

        System.out.println("Please enter the digits you would like reversed: ");
        int reverse_digits = userChoic.nextInt();
        String converted_digit = convert_to_string(reverse_digits);

        String answer = "";


        for (int i = converted_digit.length()-1; i >-1 ; i--) {
            answer += converted_digit.charAt(i);
        }

        System.out.println("The answer is: " + Integer.parseInt(answer));

    }

    public static String convert_to_string(int a) {
        String conversion = Integer.toString(a);

        return conversion;

    }


}
