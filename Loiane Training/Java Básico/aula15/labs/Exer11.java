package labs;

import java.util.Scanner;

public class Exer11 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com o salário atual:");
        double salarioAtual = scan.nextDouble();

        double aumento;
        String percentual;
        if (salarioAtual >= 1500) {
            aumento = salarioAtual * 0.05;
            percentual = "5%";
        } else if (salarioAtual > 700) {
            aumento = salarioAtual * 0.10;
            percentual = "10%";
        } else if (salarioAtual > 280) {
            aumento = salarioAtual * 0.15;
            percentual = "15%";
        } else {
            aumento = salarioAtual * 0.20;
            percentual = "20%";
        }

        double salarioFinal = salarioAtual + aumento;

        System.out.println("Salário antes do reajuste: " + salarioAtual);
        System.out.println("Percentual de aumento: " + percentual);
        System.out.println("Aumento: " + aumento);
        System.out.println("Salário final: " + salarioFinal);
    }
}
