import java.util.ArrayList;
import java.util.List;

public class ChallengeTen {
    public static void main(String[] args) {
        int num1 = Integer.parseInt(args[0]);

        fibonacci(num1);

    }


    public static void fibonacci(int n) {
        int prev_num = 1;
        List<Integer> fibonacci_sequence = new ArrayList<Integer>();
        fibonacci_sequence.add(1);
        fibonacci_sequence.add(1);
        System.out.println(fibonacci_sequence);
        int counter = 2;
        int i = 1;

        // Ignoring the 1st and 2nd values of the fibonnaci by manually implementing it
        while (counter != n) {
            fibonacci_sequence.add(prev_num+fibonacci_sequence.get(i));
            i++;

            prev_num = fibonacci_sequence.get(i-1);
            counter++;
        }

        System.out.println(fibonacci_sequence);



    }
}