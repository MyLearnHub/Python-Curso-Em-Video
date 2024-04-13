package labs;

import java.util.Scanner;

public class Exer17 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite o tamanho em metros quadrados da área a ser pintada: ");
        double tamanhoArea = scan.nextDouble();

        double quantidadeTinta = tamanhoArea / 6 * 1.1;

        int latas = (int) Math.ceil(quantidadeTinta / 18);

        double precoLatas = latas * 80.0;

        int galoes = (int) Math.ceil(quantidadeTinta / 3.6);

        double precoGaloes = galoes * 25.0;

        int latasRestantes = (int) Math.ceil((quantidadeTinta - galoes * 3.6) / 18);
        double precoMisto = (latas - latasRestantes) * 80.0 + latasRestantes * 80.0;

        System.out.println("Quantidade de tinta necessária: " + quantidadeTinta + " litros");

        System.out.println("Comprando apenas latas de 18 litros:");
        System.out.println("Quantidade de latas: " + latas);
        System.out.println("Preço total: R$ " + precoLatas);

        System.out.println("\nComprando apenas galões de 3,6 litros:");
        System.out.println("Quantidade de galões: " + galoes);
        System.out.println("Preço total: R$ " + precoGaloes);

        System.out.println("\nMisturando latas e galões:");
        System.out.println("Quantidade de latas: " + (latas - latasRestantes));
        System.out.println("Quantidade de galões: " + galoes);
        System.out.println("Preço total: R$ " + precoMisto);
    }
}
