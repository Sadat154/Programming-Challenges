public class ChallengeFour {
    public static void main(String[] args) {
        Integer factorial = Integer.parseInt(args[0]);
        int answer = 1;


        for (int i = 1; i <= factorial ; i++) {
            System.out.println(i);
            answer = answer*i;


        }

        System.out.println(answer);

    }



}
