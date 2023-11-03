import java.util.Scanner;

public class naturalNumber {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            System.out.print("Введите число: ");
            int number = scan.nextInt();

            if (number % 4 == 0) {
                System.out.println(number + " кратно четырем.");
            } else {
                System.out.println(number + " не кратно четырем.");
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
