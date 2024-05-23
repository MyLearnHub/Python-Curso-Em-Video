public class Operadores {
    public static void main(String[] args) {
        // OPERADORES - PARTE 1
        String nomeCompleto = "LINGUAGEM" + "JAVA";

        System.out.println(nomeCompleto);

        // OPERADORES - PARTE 2
        String concatenacao = "?";

        concatenacao = 1 + 1 + 1 + "1";

        concatenacao = 1 + "1" + 1 + 1;

        concatenacao = 1 + "1" + 1 + "1";

        concatenacao = "1" + 1 + 1 + 1;

        concatenacao = "1" + (1 + 1 + 1);

        // OPERADORES - PARTE 3
        int numero = 5;

        numero = - numero;

        System.out.println(numero);

        numero = + numero;

        System.out.println(numero);

        // OPERADORES PARTE 4

        numero = numero + 1;

        System.out.println(numero);

        numero++;

        System.out.println(numero);

        System.out.println(numero++);

        System.out.println(++numero);

        System.out.println(numero--);

        System.out.println(--numero);

        boolean variavel = true;

        System.out.println(!variavel);

        System.out.println(variavel);

        variavel = false;

        System.out.println(variavel);

        // OPERADORES PARTE 5
        int a, b;

        a = 5;
        b = 6;

        // String resultado = "";
        // if (a == b)
        //     resultado = "verdadeiro";
        // else
        //     resultado = "falso";

        String resultado = a == b ? "verdadeiro" : "falso";

        System.out.println(resultado);

        // OPERADORES PARTE 6
        String nomeUm = "GLEYSON";
        String nomeDois = new String("GLEYSON");

        System.out.println(nomeUm == nomeDois);

        int numero1 = 1;
        int numero2 = 2;

        boolean simNao = numero1 == numero2;

        if (numero1 > numero2) {
            System.out.println("a nossa condição é verdadeira");
        }

        System.out.println("numeroUm é igual a numeroDois?" + simNao);

        simNao = numero1 != numero2;

        System.out.println("numeroUm é diferente a numeroDois" + simNao);

        simNao = numero1 > numero2;

        System.out.println("numeroUm é maior que numeroDois" + simNao);

        // OPERADORES PARTE 7
        boolean condicao1 = true;

        boolean condicao2 = false;

        if (condicao1 && condicao2) {
            System.out.println("as duas condições são verdadeiras");            
        }

        System.out.println("fim");
    }
}
