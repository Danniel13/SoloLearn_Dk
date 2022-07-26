package Java;
//Imprimir N veces una palabra
import java.util.Scanner;

public class for1 {
  public static void main(String[] args) {
    // Impresión de palabra segun la cantida de veces que el usuario digita
Scanner scanner = new Scanner(System.in);
System.out.println("Ingrese el número de veces que desea imprimir la palabra: ");
int n = scanner.nextInt();  

Scanner scanner2 = new Scanner(System.in);
System.out.println("Ingrese la palabra que quiere repetir: ");
String word = scanner.next();
System.out.println("La palabra " + word + " se repetirá " + n + " veces a continuación: " );
for(Integer x=1;x <=n; x++) 
System.out.println(word);
scanner.close();
scanner2.close();
  }
}
