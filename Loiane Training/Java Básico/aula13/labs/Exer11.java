package labs;

import java.util.Scanner;

public class Exer11 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite um valor inteiro:");
        int num1 = scan.nextInt();

        System.out.println("Digite outro valor inteiro:");
        int num2 = scan.nextInt();

        System.out.println("Digite um valor real:");
        double num3 = scan.nextDouble();

        double produto = num1 * 2 + num2 / 2;
        double soma = num1 * 3 + num3;
        double cubo = Math.pow(num3, 3);

        System.out.println("Produto do dobro do primeiro com metade do segundo: " + produto);
        System.out.println("Soma do triplo do primeiro com o terceiro: " + soma);
        System.out.println("Terceiro elevado ao cubo: " + cubo);
    }
}
