package labs;

import java.util.Scanner;

public class Exer04 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite a primeira nota:");
        double nota = scan.nextDouble();

        System.out.println("Digite a segunda nota:");
        double nota2 = scan.nextDouble();

        System.out.println("Digite a terceira nota:");
        double nota3 = scan.nextDouble();

        System.out.println("Digite a quarta nota:");
        double nota4 = scan.nextDouble();

        double media = (nota + nota2 + nota3 + nota4) / 4;
        System.out.println("A média é: " + media);
    }
}
