import java.util.Scanner;

public class Exer19 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double[] notas1 = new double[10];
        double[] notas2 = new double[notas1.length];
        double[] resultados = new double[notas1.length];

        for (int i = 0; i < notas1.length; i++) {
            System.out.println("Entre com a nota 1 do aluno " + (i + 1));
            notas1[i] = scan.nextDouble();

            System.out.println("Entre com a nota 2 do aluno " + (i + 1));
            notas2[i] = scan.nextDouble();

            resultados[i] = (notas1[i] + notas2[i]) / 2;
        }

        System.out.print("Notas 1 = ");
        for (double v : notas1) {
            System.out.print(v + " ");
        }
        System.out.println();

        System.out.print("Notas 2 = ");
        for (double v : notas2) {
            System.out.print(v + " ");
        }
        System.out.println();

        System.out.println("Resultados:");
        for (double resultado : resultados) {
            if (resultado >= 7) {
                System.out.println(resultado + " - Aprovado");
            } else {
                System.out.println(resultado + " - Reprovado");
            }
        }
    }
}
