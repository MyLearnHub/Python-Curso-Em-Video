public class Professor extends Pessoa {
    private double Salario;
    private String nomeCurso;

    public double getSalario() {
        return Salario;
    }

    public void setSalario(double salario) {
        Salario = salario;
    }

    public String getNomeCurso() {
        return nomeCurso;
    }

    public void setNomeCurso(String nomeCurso) {
        this.nomeCurso = nomeCurso;
    }

    public double calcularSalarioLiquido() {
        return 0;
    }

    public String obterEtiquetaEndereco() {
        String s = "Endereço do Professor: ";
        s += this.getEndereco();

        return s;
    }
}
