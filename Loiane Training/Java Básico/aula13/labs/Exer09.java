package labs;

import java.util.Scanner;

public class Exer09 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Diga a temperatura em Fº:");
        double farenheit = scan.nextDouble();

        double celsius = (farenheit - 32) * 5 / 9;

        System.out.println("A temperatura em graus Cº é: " + celsius);
    }
}
