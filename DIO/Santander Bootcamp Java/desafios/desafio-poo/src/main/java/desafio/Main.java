package desafio;

public class Main {
    public static void main(String[] args) {
        Iphone meuIphone = new Iphone();

        System.out.println("Teste do Aparelho Telefonico:");
        meuIphone.ligar("123456789");
        meuIphone.atender();
        meuIphone.iniciarCorreioVoz();

        System.out.println("\nTeste do Navegador Internet:");
        meuIphone.exibirPagina("www.exemplo.com");
        meuIphone.adicionarNovaAba();
        meuIphone.atualizarPagina();

        System.out.println("\nTeste do Reprodutor Musical:");
        meuIphone.selecionarMusica("Minha Música Favorita");
        meuIphone.tocar();
        meuIphone.pausar();
    }
}
