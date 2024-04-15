import java.util.Scanner;

public class Exer31 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int[] vetorA = new int[20];
        int[] vetorB = new int[vetorA.length];

        for (int i = 0; i < vetorA.length; i++) {
            System.out.println("Entre com o valor da posição A - " + i);
            vetorA[i] = scan.nextInt();
        }

        int posB = 0;
        for (int j : vetorA) {
            if (j % 2 == 0) {
                vetorB[posB] = j;
                posB++;
            }
        }

        for (int j : vetorA) {
            if (j % 2 != 0) {
                vetorB[posB] = j;
                posB++;
            }
        }

        System.out.print("Vetor A = ");
        for (int j : vetorA) {
            System.out.print(j + " ");
        }
        System.out.println();

        System.out.print("Vetor B = ");
        for (int i = 0; i < posB; i++) {
            System.out.print(vetorB[i] + " ");
        }
        System.out.println();
    }
}
