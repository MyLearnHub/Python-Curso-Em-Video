import java.util.Scanner;

public class Exer10 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        
        int[] vetorA = new int[10];
        int[] vetorB = new int[vetorA.length];
        
        for (int i=0; i<vetorA.length; i++){
            System.out.println("Entre com o valor da posição: " + i);
            vetorA[i] = scan.nextInt();
            vetorB[i] = vetorA[i] % 2;
        }
        
        System.out.print("Vetor A = ");
        for (int j : vetorA) {
            System.out.print(j + " ");
        }
        System.out.println();
        
        System.out.print("Vetor B = ");
        for (int j : vetorB) {
            System.out.print(j + " ");
        }
        System.out.println();
    }    
}
