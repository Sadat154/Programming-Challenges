public class ChallengeSeven {
    public static void main(String[] args) {
        int userChoice = Integer.parseInt(args[0]);
        int i = 2;
        boolean primeOrNot = true;

        while (i != userChoice) {

            if (userChoice % i == 0) {
                primeOrNot = false;
                break;
            }

            i++;
        }


        if (primeOrNot) {
            System.out.println(userChoice + " is a prime number");
        }

        else {
            System.out.println(userChoice + " is not a prime number");
        }
        
    }
}
