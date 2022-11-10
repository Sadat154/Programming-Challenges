public class ChallengeThree {
    public static void main(String[] args) {
        Integer multiply= Integer.parseInt(args[0]);

        for (int i = 0; i < 13; i++) {
            System.out.println(i + " x " + multiply + " = " + (i*multiply));
        }

    }
}
