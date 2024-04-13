package labs;

import java.util.Scanner;

public class Exer03 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite uma letra (F ou M):");
        String letra = scan.nextLine();

        if (letra.equals("F")) {
            System.out.println("F - Feminino");
        } else if (letra.equals("M")) {
            System.out.println("M - Masculino");
        } else {
            System.out.println("Sexo inválido");
        }
    }
}
