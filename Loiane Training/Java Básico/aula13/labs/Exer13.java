package labs;

import java.util.Scanner;

public class Exer13 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite sua altura:");
        double altura = scan.nextDouble();

        System.out.println("Digite seu sexo [M / F]:");
        String sexo = scan.next();

        double pesoIdeal = sexo == "M" ? 72.7 * altura - 58 : 62.1 * altura - 44.7;

        System.out.println("Diga seu peso atual:");
        double pesoAtual = scan.nextDouble();

        String resultado = pesoIdeal == pesoAtual ? "dentro do peso ideal" : pesoIdeal >= pesoAtual ? "acima do peso" : "abaixo do peso";
        System.out.println("Você está: " + resultado);
    }
}
