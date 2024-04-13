package labs;

import java.util.Scanner;

public class Exer15 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Quanto você ganha por hora?");
        double valorHora = scan.nextDouble();

        System.out.println("Quantas horas você trabalha por mês?");
        int horas = scan.nextInt();

        double salarioBruto = valorHora * horas;

        double impostoDeRenda = salarioBruto * 0.11;
        double inss = salarioBruto * 0.8;
        double sindicato = salarioBruto * 0.5;
        double descontos = impostoDeRenda + inss + sindicato;

        double salarioLiquido = salarioBruto - descontos;

        System.out.println("Seu salário bruto é: " + salarioBruto);
        System.out.println("Quanto pagou ao INSS: " + inss);
        System.out.println("Quanto pagou ao sindicato: " + sindicato);
        System.out.println("Seu salário líquido: " + salarioLiquido);
    }
}
