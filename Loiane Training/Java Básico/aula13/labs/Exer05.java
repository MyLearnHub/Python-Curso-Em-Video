package labs;

import java.util.Scanner;

public class Exer05 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite um valor em metros:");
        double metros = scan.nextDouble();

        double conversao = metros * 100;
        System.out.println(metros + "m em centímetros é: " + conversao + "cm");
    }
}
