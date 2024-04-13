package labs;

import java.util.Scanner;

public class Exer14 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Quantos quilos de peixe?");
        double quilos = scan.nextDouble();

        double excesso = quilos > 50 ? quilos - 50 : 0;
        double multa = excesso * 4;

        System.out.println("Valor do excesso: " + excesso);
        System.out.println("Valor da multa: " + multa);
    }
}
