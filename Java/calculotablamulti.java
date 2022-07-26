package Java;

import java.util.Scanner;

public class calculotablamulti {
  public static void main(String[] args) {
    
//multiplos de 3
Scanner scanner = new Scanner(System.in);
System.out.println("Ingrese la tabla a evaluar");
int n = scanner.nextInt();  



for(int x = 1; x <=10; x++) 
System.out.printf("%d * %d = %d %n", x, n,x*n);
  // System.out.println(x  +  n + x*n);
  
scanner.close();

  }
}
