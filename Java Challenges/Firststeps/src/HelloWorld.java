import java.sql.SQLOutput;

public class HelloWorld {
    public static void main(String[] args) {
        for_loop_yes();
        car_arrays();
        day();
        day_with_switches();
        print_tenth_int();
    }

    public static void for_loop_yes() {
        for (int i = 0; i <5; i++) {
            System.out.println("Yes");
        }

    }

    public static void car_arrays() {
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};

        for (String elements : cars){
            System.out.println(elements);
        }

    }


    public static void day() {
        int day = 4;

        if (day == 6) {
            System.out.println("today is Saturday");
        }
        else if (day == 7) {
            System.out.println("today is Sunday");

        }
        else {
            System.out.println("looking forward to the weekend");
        }

    }
    public static void day_with_switches() {
        int day = 6;

        switch (day) {
            case 6:
                System.out.println("today is Saturday");
                break;

            case 7:
                System.out.println("today is Sunday");
                break;

            default:
                System.out.println("looking forward to the weekend");
                break;
        }

    }

    public static void print_tenth_int(){
        int[] myNumbers = {1,2,3};

        try {
            System.out.println(myNumbers[10]);
        }
        catch (ArrayIndexOutOfBoundsException errorName){
            System.out.println(errorName);
        }
    }

}
