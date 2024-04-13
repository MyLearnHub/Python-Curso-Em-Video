package labs;

import java.util.Scanner;

public class Exer18 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Informe o tamanho do arquivo em MB:");
        double tamanhoDoArquivo = scan.nextDouble();

        System.out.println("Velocidade da internet em Mbps:");
        double velocidadeInternet = scan.nextDouble();

        double velocidadeMBps = velocidadeInternet / 8;

        // Calculando o tempo de download em segundos
        double tempoDownloadSegundos = tamanhoDoArquivo / velocidadeMBps;

        // Convertendo o tempo de download para minutos
        double tempoDownloadMinutos = tempoDownloadSegundos / 60;

        System.out.println("Tempo aproximado de download: " + tempoDownloadMinutos + " minutos");


    }
}
