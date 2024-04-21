import java.util.Scanner;
public class practice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("첫 번째 숫자를 입력하세요: ");
        int a = scanner.nextInt();

        System.out.print("두 번째 숫자를 입력하세요: ");
        int b = scanner.nextInt();

        int sum = a + b;
        System.out.println("두 숫자의 합은: " + sum);
    }
}