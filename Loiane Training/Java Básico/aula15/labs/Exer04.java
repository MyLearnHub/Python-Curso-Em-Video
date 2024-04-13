package labs;

import java.util.Scanner;

public class Exer04 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite uma letra:");
        String letra = scan.nextLine();

        if (letra.equals("A") || letra.equals("E") || letra.equals("I") || letra.equals("O") || letra.equals("U")) {
            System.out.println("Vogal");
        } else {
            System.out.println("Consoante");
        }
    }
}
