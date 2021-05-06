/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package main;

import Telas.inicial;

/**
 *
 * @author Fer-san
 */
public class ChatTcpIp {

    /**
     * @param args the command line arguments
     */
    private static boolean clicou = false;
    public static void main(String[] args) {
        // TODO code application logic here
        inicial login = new inicial(clicou);
        login.setVisible(true);
    }
    
}
