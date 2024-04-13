package labs;

import java.util.Scanner;

public class Exer12 {
    public static void main(String[] args) {
        Scanner scan  = new Scanner(System.in);

        System.out.println("Entre com o valor/hora:");
        double valor = scan.nextDouble();

        System.out.println("Entre com as horas trabalhadas no mês:");
        double horas = scan.nextDouble();

        double salarioBruto = valor * horas;

        double ir = 0;
        if (salarioBruto > 2500) {
            ir = salarioBruto * 0.20;
        } else if (salarioBruto > 1500) {
            ir = salarioBruto * 0.10;
        } else if (salarioBruto > 900) {
            ir = salarioBruto * 0.05;
        }

        double sindicato = salarioBruto * 0.03;
        double fgts = salarioBruto * 0.11;
        double desconto = ir + sindicato + fgts;
        double salarioLiquido = salarioBruto - desconto;

        System.out.println("Salário Bruto: R$" + salarioBruto);
        System.out.println("( - ) IR: R$" + ir);
        System.out.println("FGTS: R$" + fgts);
        System.out.println("Descontos: R$" + desconto);
        System.out.println("Salário Líquido: R$" + salarioLiquido);
    }
}
