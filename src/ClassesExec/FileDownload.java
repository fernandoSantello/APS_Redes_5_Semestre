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

public class FileDownload extends Comando implements Serializable {
    private byte[] fileBytes;

    //Método Construtor da classe 
    public FileDownload(ComandoEnum comando, InformacoesCliente informacoesCliente, byte[] fileBytes) {
        super(comando, informacoesCliente);
        this.fileBytes = fileBytes;
    }
    
    //Métodos Set e Get
    public void setFileBytes(byte[] fileBytes) {
        this.fileBytes = fileBytes;
    }
    
    public byte[] getFileBytes(){
        return fileBytes;
    }
}
