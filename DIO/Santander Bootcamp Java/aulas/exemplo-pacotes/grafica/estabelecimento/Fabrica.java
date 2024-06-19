package grafica.estabelecimento;

import grafica.equipamentos.copiadora.Copiadora;
import grafica.equipamentos.digitalizadora.Digitalizadora;
import grafica.equipamentos.impressora.Deskjet;
import grafica.equipamentos.impressora.Impressora;
import grafica.equipamentos.multifuncional.EquipamentoMultifuncional;

public class Fabrica {
    public static void main(String[] args) {
        EquipamentoMultifuncional em = new EquipamentoMultifuncional();

        Deskjet deskjet = new Deskjet();

        Impressora impressora = em;
        Digitalizadora digitalizadora = em;
        Copiadora copiadora = em;

        impressora.imprimir();
        digitalizadora.digitalizar();
        copiadora.copiar();
    }
}
