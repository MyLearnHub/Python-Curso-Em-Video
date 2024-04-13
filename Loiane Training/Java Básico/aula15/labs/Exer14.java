package labs;

import java.util.Scanner;

public class Exer14 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite a primeira nota:");
        double nota1 = scan.nextDouble();

        System.out.println("Digite a segunda nota:");
        double nota2 = scan.nextDouble();

        double media = (nota1 + nota2) / 2;
        String conceito;

        if (media > 9) {
            conceito = "A";
        } else if (media > 7.5) {
            conceito = "B";
        } else if (media > 6) {
            conceito = "C";
        } else if (media > 4) {
            conceito = "D";
        } else {
            conceito = "E";
        }

        String mensagem = conceito == "D" || conceito == "E" ? "REPROVADO" : "APROVADO";

        System.out.println("Primeira nota: " + nota1);
        System.out.println("Segunda nota: " + nota2);
        System.out.println("Média: " + media);
        System.out.println("Conceito: " + conceito);
        System.out.println("Mensagem: " + mensagem);
    }
}
