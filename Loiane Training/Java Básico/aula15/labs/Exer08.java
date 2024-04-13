package labs;

import java.util.Scanner;

public class Exer08 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com o preço do primeiro produto:");
        double produto1 = scan.nextDouble();

        System.out.println("Entre com o preço do segundo produto:");
        double produto2 = scan.nextDouble();

        System.out.println("Entre com o preço do terceiro produto:");
        double produto3 = scan.nextDouble();

        if (produto1 > produto2 && produto1 > produto3){
            System.out.println("Compre o primeiro produto");
        } else if (produto2 > produto1 && produto2 > produto3){
            System.out.println("Compre o segundo produto");
        } else {
            System.out.println("Compre o terceiro produto");
        }
    }
}
