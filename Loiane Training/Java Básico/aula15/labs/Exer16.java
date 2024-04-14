package labs;

import java.util.Scanner;

public class Exer16 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com o valor de a:");
        double a = scan.nextDouble();

        if (a == 0) {
            System.out.println("Não é equação de segundo grau");
        } else {
            System.out.println("Entre com o valor de b:");
            double b = scan.nextDouble();

            System.out.println("Entre com o valor de c:");
            double c = scan.nextDouble();

            double delta = b * b - 4 * a * c;

            if (delta < 0) {
                System.out.println("Delta Negativo");
            } else {
                System.out.println("Delta: " + delta);

                double x1 = (-b + Math.sqrt(delta)) / (2 * a);
                double x2 = (-b - Math.sqrt(delta)) / (2 * a);

                System.out.println("x1 = " + x1);
                System.out.println("x2 = " + x2);
            }
        }
    }
}
