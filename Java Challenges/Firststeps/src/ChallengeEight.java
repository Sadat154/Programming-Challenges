public class ChallengeEight {
    public static void main(String[] args) {
        int num1 = 48;
        int num2 = 56;
        System.out.println("The HCF of " + num1 + " and " + num2 + " is: " + common_factors(num1,num2));
    }


    public static int common_factors(int a, int b) {
        int hcf = 0;
        for (int i = 1; i <= a || i <= b; i++) {
            if (a % i == 0 && b % i == 0) {
                hcf = i;
            }
        }
        return hcf;

    }
}