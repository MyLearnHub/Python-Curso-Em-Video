package labs;

import java.util.Scanner;

public class Exer10 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite o turno que você estuda:");
        String turno = scan.nextLine();

        switch (turno) {
            case "m":
            case "M":
                System.out.println("Bom Dia!");
                break;
            case "v":
            case "V":
                System.out.println("Boa Tarde!");
                break;
            case "n":
            case "N":
                System.out.println("Boa Noite!");
                break;
            default:
                System.out.println("Valor Inválido!");
        }
    }
}
