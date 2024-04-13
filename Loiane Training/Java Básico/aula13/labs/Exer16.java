package labs;

import java.util.Scanner;

public class Exer16 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Diga o metro quadrado da área a ser pintada:");
        double metroQuadrado = scan.nextDouble();

        double litrosDeTinta = metroQuadrado / 3;
        double latasNecessarias = litrosDeTinta / 18;
        double valorAPagar = latasNecessarias * 80;

        System.out.println("Total de latas a serem compradas: " + latasNecessarias);
        System.out.println("Valor total: " + valorAPagar);
    }
}
