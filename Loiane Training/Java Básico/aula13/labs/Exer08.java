package labs;

import java.util.Scanner;

public class Exer08 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Quanto você ganha por hora?");
        double valorHora = scan.nextDouble();

        System.out.println("Quantas horas você trabalha por mês?");
        int horas = scan.nextInt();

        double salario = valorHora * horas;

        System.out.println("Seu salário é: " + salario);
    }
}
