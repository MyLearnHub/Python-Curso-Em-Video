package labs;

import java.util.Scanner;

public class Exer02 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com um valor:");
        int valor = scan.nextInt();

        if (valor > 0) {
            System.out.println("Esse número é positivo");
        } else {
            System.out.println("Esse número é negativo");
        }
    }
}
