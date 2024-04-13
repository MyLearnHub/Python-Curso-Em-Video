package labs;

import java.util.Scanner;

public class Exer01 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Entre com um número:");
        int num1 = scan.nextInt();

        System.out.println("Entre com outro número:");
        int num2 = scan.nextInt();

        if (num1 > num2) {
            System.out.println("O maior número é o: " + num1);
        } else {
            System.out.println("O maior número é o: " + num2);
        }
    }
}
