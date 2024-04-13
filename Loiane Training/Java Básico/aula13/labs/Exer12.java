package labs;

import java.util.Scanner;

public class Exer12 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite sua altura:");
        double altura = scan.nextDouble();

        double pesoIdeal = 72.2 * altura - 58;

        System.out.println("Seu peso ideal é: " + pesoIdeal);
    }
}
