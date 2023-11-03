import java.util.Scanner;

public class BoxAndDoor {
    public static boolean willBoxFit(int a, int b, int c, int k, int m) {
        // Проверяем, что размеры коробки по всем измерениям меньше или равны размерам
        // двери
        if (a <= k && b <= m) {
            return true;
        } else if (a <= m && b <= k) {
            return true;
        } else if (a <= k && c <= m) {
            return true;
        } else if (a <= m && c <= k) {
            return true;
        } else if (b <= k && c <= m) {
            return true;
        } else if (b <= m && c <= k) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            System.out.println("Введите размер коробки а, b и c");
            System.out.print("a: ");
            int a = scan.nextInt();
            System.out.print("b: ");
            int b = scan.nextInt();
            System.out.print("c: ");
            int c = scan.nextInt();
            System.out.println("Введите размер двери k и m");
            System.out.print("k: ");
            int k = scan.nextInt();
            System.out.print("m: ");
            int m = scan.nextInt();
            if (willBoxFit(a, b, c, k, m)) {
                System.out.print("Коробка пройдет через дверь.");
            } else {
                System.out.print("Коробка не пройдет через дверь.");
            }
        } catch (Exception e) {
            System.out.print(e);
        }
    }
}
