package designPattern.builder.solucao;

import designPattern.builder.Pessoa;

import java.time.LocalDate;

public class TestePessoaComBuilder {
    public static void main(String[] args) {
        Pessoa pessoa =
                new Pessoa.PessoaBuilder()
                .nome("Anderson")
                .sobreNome("Piotto")
                .documento("35461845569")
                .email("piottok10@gmail.com")
                .apelido("careca")
                .dataNascimento(LocalDate.of(1985, 3, 12))
                .build();

        System.out.println(pessoa);

        StringBuilder sb = new StringBuilder().append("palavra 1").append("palavra 2");
        System.out.println(sb);
    }
}
