import java.util.Scanner;

public class Main {
     public static void main(String[] args) {
        Calculator calc = new Calculator();
        Scanner scanner = new Scanner(System.in);

        int num1, num2;

        System.out.print("Digite o primeiro número: ");
        num1 = scanner.nextInt();

        System.out.print("Digite o segundo número: ");
        num2 = scanner.nextInt();

        scanner.close();

        int result = calc.sum(num1, num2);
        System.out.println("Resultado da soma de "+ num1 +" e "+ num2 +" é: " + result);

        result = calc.subtract(num1, num2);
        System.out.println("Resultado da subtração de "+ num1 +" e "+ num2 +" é: " + result);

        result = calc.multiply(num1, num2);
        System.out.println("Resultado da multiplicação de "+ num1 +" e "+ num2 +" é: " + result);

        result = calc.divide(num1, num2);
        System.out.println("Resultado da divisão de "+ num1 +" e "+ num2 +" é: " + result);


    }
}
