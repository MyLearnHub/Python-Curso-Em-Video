package contrutores;

public class SistemaCadastro {
    public static void main(String[] args) {
        Pessoa marcos = new Pessoa("Paulo", "12345678910", "Reginaldo Nilson da Silva");

        marcos.setEndereco("RUA DAS MARIAS");

        System.out.println(marcos.getNome() + "-" + marcos.getCpf());
    }
}
