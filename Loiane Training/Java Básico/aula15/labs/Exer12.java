package labs;

import java.util.Scanner;

public class Exer12 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com o valor/hora:");
        double valorHora = scan.nextDouble();

        System.out.println("Entre com as horas trabalhadas no mês:");
        double qtdHoras = scan.nextDouble();

        double salarioBruto = valorHora * qtdHoras;

        double percentualIR = 0;
        if (salarioBruto > 2500) {
            percentualIR = 0.20;
        } else if (salarioBruto > 1500) {
            percentualIR = 0.10;
        } else if (salarioBruto > 900) {
            percentualIR = 0.05;
        }

        double ir = salarioBruto * percentualIR;
        double inss = salarioBruto * 0.10;
        double fgts = salarioBruto * 0.11;
        double totalDescontos = ir + inss;
        double salarioLiquido = salarioBruto - totalDescontos;

        System.out.println("Salário Bruto: (" + valorHora + " * " + qtdHoras + "): " + salarioBruto);
        System.out.println("( - ) IR (" + percentualIR + "%): " + ir);
        System.out.println("( - ) INSS (10%): " + inss);
        System.out.println("FGTS (11%): " + fgts);
        System.out.println("Total de Descontos: " + totalDescontos);
        System.out.println("Salário Líquido: " + salarioLiquido);
    }
}
