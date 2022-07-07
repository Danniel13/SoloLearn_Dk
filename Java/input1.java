package Java;

import java.util.Scanner; //Importacion libreria scanner para INPUT

public class input1 {
  public static void main(String[] args) {
    System.out.print("Ingrese la entrada: ");  //Definición texto inicial para input
    Scanner myVar = new Scanner(System.in); //Definición cariable como input
   
    System.out.println("El input es: " + myVar.nextLine()); //Impresión de input
    
    
  }
}
