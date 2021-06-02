package ClassesExec;

import Enum.ComandoEnum;
import java.io.Serializable;

/**
 *
 * @author Fer-sama
 * @author Isa-chan
 * @author Perigo-kun
 * @author Lucas-san
 * @author Japa-kouhai
 * 
 */

public class FileArray extends Comando implements Serializable{
    String[] nomeArquivos;

    public FileArray(ComandoEnum comando, InformacoesCliente informacoesCliente, String[] nomeArquivos) {
        super(comando, informacoesCliente);
        this.nomeArquivos = nomeArquivos;
    }

    public String[] getNomeArquivos() {
        return nomeArquivos;
    }

}
