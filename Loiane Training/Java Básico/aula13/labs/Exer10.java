package labs;

import java.util.Scanner;

public class Exer10 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Diga a temperatura em Cº:");
        double celsius = scan.nextDouble();

        double fahrenheit = (celsius * 9 / 5) + 32;

        System.out.println("A temperatura em Fº é: " + fahrenheit);
    }
}
