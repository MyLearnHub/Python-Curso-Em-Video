package labs;

import java.util.Scanner;

public class Exer14 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com a primeira nota:");
        double nota1 = scan.nextDouble();

        System.out.println("Entre com a segunda nota:");
        double nota2 = scan.nextDouble();

        double media = (nota1 + nota2) / 2;

        String aproveitamento;

        if (media >= 9) {
            aproveitamento = "A";
        } else if (media >= 7.5) {
            aproveitamento = "B";
        } else if (media >= 6) {
            aproveitamento = "C";
        } else if (media >= 4) {
            aproveitamento = "D";
        } else {
            aproveitamento = "E";
        }

        System.out.println("Nota 1: " + nota1);
        System.out.println("Nota 2: " + nota2);
        System.out.println("Média: " + media);
        System.out.println("Conceito: " + aproveitamento);

        switch (aproveitamento) {
            case "A":
            case "B":
            case "C":
                System.out.println("APROVADO");
                break;
            default:
                System.out.println("REPROVADO");
        }
    }
}
