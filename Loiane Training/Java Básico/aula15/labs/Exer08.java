package labs;

import java.util.Scanner;

public class Exer08 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com o primeiro preco:");
        double preco1 = scan.nextDouble();

        System.out.println("Entre com o segundo preco:");
        double preco2 = scan.nextDouble();

        System.out.println("Entre com o terceiro preco:");
        double preco3 = scan.nextDouble();

        if (preco1 <= preco2 && preco1 <= preco3) {
            System.out.println("Compre o produto 1");
        } else if (preco2 <= preco1 && preco2 <= preco3) {
            System.out.println("Compre o produto 2");
        } else {
            System.out.println("Compre o produto 3");
        }
    }
}
