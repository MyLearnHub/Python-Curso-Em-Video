package edu.gleyson.segundasemana;

public class MinhaClasse {
    public static void main(String[] args) {
        // System.out.println("Olá turma, sejam bem-vindos");
        // final String BR = "Brasil";
        // BR = "Brazil";

        // String meuNome = "Gleyson";
        // int anoFabricacao = 2022;
        // boolean verdadeira = false;

        String primeiroNome = "Gleyson";
        String segundoNome = "Sampaio";

        String nomeCompleto = nomeCompleto(primeiroNome, segundoNome);

        System.out.println(nomeCompleto);
    }

    public static String nomeCompleto(String primeiroNome, String segundoNome) {
        return "Resultado do método " + primeiroNome.concat(" ").concat(segundoNome);  
    }
}
