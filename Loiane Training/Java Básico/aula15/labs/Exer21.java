package labs;

import java.util.Scanner;

public class Exer21 {
    public static void main(String[] args) {
        Scanner scan  = new Scanner(System.in);

        System.out.println("Entre com a qtd de litros vendidos:");
        int litros = scan.nextInt();

        System.out.println("Entre com o tipo de combustível");
        String tipo = scan.next();

        double precoGas = 2.5;
        double precoAlc = 1.9;
        int precoDesconto = 0;
        double total = 0;
        double totalDesc = 0;

        if(tipo.equalsIgnoreCase("A")) {
            if (litros <= 20) {
                precoDesconto = 3;
            } else {
                precoDesconto = 5;
            }

            total = litros * precoAlc;
        } else if (tipo.equalsIgnoreCase("G")){
            if (litros <= 20) {
                precoDesconto = 4;
            } else {
                precoDesconto = 6;
            }

            total = litros * precoGas;
        }

        totalDesc = (total / 100) * precoDesconto;

        double precoAPagar = total - totalDesc;

        System.out.println("Valor a ser pago: " + precoAPagar);
    }
}
