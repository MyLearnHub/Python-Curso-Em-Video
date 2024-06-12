package programacaoOrientadaObjeto;

import programacaoOrientadaObjeto.Animais.Cachorro;
import programacaoOrientadaObjeto.Animais.Gato;
import programacaoOrientadaObjeto.Animais.Passaro;

public class Main {
    public static void main(String[] args) {
        Cachorro cachorro1 = new Cachorro("Rex", "Branco", 10, 10.5, 5, "nada");
        Gato gato1 = new Gato("Felix", "Preto", 4.5);
        Passaro passaro1 = new Passaro("Frajola", "Azul", 0.5);

        cachorro1.soar();
        gato1.soar();
        passaro1.soar();
    }
}
