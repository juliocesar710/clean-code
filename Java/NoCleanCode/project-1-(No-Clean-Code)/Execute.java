import java.util.Scanner;

public class Execute {

    public static int add(int a, int b) {
        return a + b;
    }

    public static int subtract(int a, int b) {
        return a - b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }

    public static double divide(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Division by zero is not allowed.");
        }
        return (double) a / b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o primeiro número:");
        int num1 = scanner.nextInt();
        System.out.println("Digite o segundo número:");
        int num2 = scanner.nextInt();
        scanner.close();
        System.out.println("A soma do número " + num1 + " com o número " + num2 + " é: " + add(num1, num2));
        System.out.println(
                "A subtração do número " + num1 + " com o número " + num2 + " é: " + subtract(num1, num2));
        System.out.println("A multiplicação do número " + num1 + " com o número " + num2 + " é: "
                + multiply(num1, num2));
        try {
            System.out.println(
                    "A divisão do número " + num1 + " com o número " + num2 + " é: " + divide(num1, num2));
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }

    }
}
