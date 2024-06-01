package desafio;

public class Iphone implements AparelhoTelefonico, NavegadorInternet, ReprodutorMusical {

    private String musicaAtual;
    private boolean emChamada;

    @Override
    public void ligar(String numero) {
        emChamada = true;
        System.out.println("Ligando para " + numero + "...");
    }

    @Override
    public void atender() {
        if (emChamada) {
            System.out.println("Atendendo a chamada...");
        } else {
            System.out.println("Não há chamada para atender.");
        }
    }

    @Override
    public void iniciarCorreioVoz() {
        System.out.println("Iniciando o correio de voz...");
    }

    @Override
    public void exibirPagina(String url) {
        System.out.println("Exibindo a página: " + url);
    }

    @Override
    public void adicionarNovaAba() {
        System.out.println("Adicionando uma nova aba...");
    }

    @Override
    public void atualizarPagina() {
        System.out.println("Atualizando a página...");
    }

    @Override
    public void tocar() {
        if (musicaAtual != null) {
            System.out.println("Tocando a música: " + musicaAtual);
        } else {
            System.out.println("Nenhuma música selecionada.");
        }
    }

    @Override
    public void pausar() {
        if (musicaAtual != null) {
            System.out.println("Pausando a música: " + musicaAtual);
        } else {
            System.out.println("Nenhuma música está tocando.");
        }
    }

    @Override
    public void selecionarMusica(String musica) {
        musicaAtual = musica;
        System.out.println("Música selecionada: " + musica);
    }
}