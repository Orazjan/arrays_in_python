import java.util.Scanner;

public class summa {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            System.out.print("Введите сумму: ");
            int amount = scan.nextInt();
            int[] denominations = { 500, 100, 10, 3 };
            int[] count = new int[denominations.length];

            for (int i = 0; i < denominations.length; i++) {
                if (amount >= denominations[i]) {
                    count[i] = amount / denominations[i];
                    amount %= denominations[i];
                }
            }

            System.out.println("Размен суммы:");
            for (int i = 0; i < denominations.length; i++) {
                if (count[i] > 0) {
                    System.out.println(denominations[i] + ": " + count[i]);
                }
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
