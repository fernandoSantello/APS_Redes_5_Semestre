/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ClassesExec;

import Enum.ComandoEnum;
import java.io.Serializable;

/**
 *
 * @author Fer-san
 */
public class Comando implements Serializable {
    private ComandoEnum comando;
    private InformacoesCliente informacoesCliente;
    
    public Comando(ComandoEnum comando, InformacoesCliente informacoesCliente) {
        this.comando = comando;
        this.informacoesCliente = informacoesCliente;
        if (informacoesCliente != null)
            this.informacoesCliente.setOut(null);
    }
    
    public ComandoEnum getComando() {
        return comando;
    }
    
    public InformacoesCliente getInformacoesCliente() {
        return informacoesCliente;
    }
}
