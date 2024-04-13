package labs;

import java.util.Scanner;

public class Exer13 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com o valor/hora:");
        double valorHora = scan.nextDouble();

        System.out.println("Entre com a quantidade de horas trabalhadas no mês:");
        int horas = scan.nextInt();

        double salarioBruto = valorHora * horas;
        double inss = salarioBruto * 0.08;
        double sindicato = salarioBruto * 0.05;
        double ir = salarioBruto * 0.11;
        double totalDescontos = inss + sindicato + ir;
        double salarioLiquido = salarioBruto - totalDescontos;

        System.out.println("Salário bruto é: " + salarioBruto);
        System.out.println("INSS: " + inss);
        System.out.println("Sindicato: " + sindicato);
        System.out.println("IR: " + ir);
        System.out.println("Total descontos: " + totalDescontos);
        System.out.println("Salário líquido: " + salarioLiquido);
    }
}
