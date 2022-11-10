public class ChallengeNine {
    public static void main(String[] args) {
        String num = "153";
        double answer_test = 0;
        for (int i = 0; i < num.length(); i++) {
            System.out.println(num.charAt(i));
            answer_test += Math.pow(Integer.parseInt(String.valueOf(num.charAt(i))), 3);
        }
        System.out.println(answer_test);
    }
}