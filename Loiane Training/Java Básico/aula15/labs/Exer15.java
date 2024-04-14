package labs;

import java.util.Scanner;

public class Exer15 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com o lado 1:");
        double lado1 = scan.nextDouble();

        System.out.println("Entre com o lado 2:");
        double lado2 = scan.nextDouble();

        System.out.println("Entre com o lado 3:");
        double lado3 = scan.nextDouble();

        if (lado1 + lado2 > lado3 && lado1 + lado3 > lado2 && lado2 + lado3 > lado1) {
            if (lado1 == lado2 && lado1 == lado3) {
                System.out.println("Triângulo Equilátero");
            } else if (lado1 != lado2 && lado1 != lado3 && lado2 != lado3) {
                System.out.println("Triângulo Escaleno");
            } else {
                System.out.println("Triângulo   Isósceles");
            }
        } else {
            System.out.println("Não forma um triângulo");
        }
    }
}
