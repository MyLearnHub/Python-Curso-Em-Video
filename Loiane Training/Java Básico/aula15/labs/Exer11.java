package labs;

import java.util.Scanner;

public class Exer11 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite o salário:");
        double salario = scan.nextDouble();

        int percentual;
        if (salario >= 1500) {
            percentual = 5;
        } else if (salario >= 700) {
            percentual = 10;
        } else if (salario > 280) {
            percentual = 15;
        } else {
            percentual = 20;
        }

        double aumento = (salario / 100) * percentual;
        double salarioAjustado = salario + aumento;

        System.out.println("Salário: " + salario);
        System.out.println("Percentual: " + percentual);
        System.out.println("Aumento: " + aumento);
        System.out.println("Salário Ajustado: " + salarioAjustado);
    }
}
