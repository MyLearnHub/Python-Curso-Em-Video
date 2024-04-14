import java.util.Scanner;

public class Exer01 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        boolean notaValida = false;

        do {
            System.out.println("Entre com uma nota (0 - 10):");
            int nota = scan.nextInt();

            if (nota >= 0 && nota <= 10) {
                System.out.println("Você Digitou: " + nota);
                notaValida = true;
            } else {
                System.out.println("Nota inválida, digite novamente.");
            }
        } while (!notaValida);
    }
}
