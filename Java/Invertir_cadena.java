package Java;

import java.util.Scanner;

public class Invertir_cadena {
  public static void main(String[] args) {
    
    Scanner scanner = new Scanner(System.in);
		String text = scanner.nextLine();
		char[] arr = text.toCharArray();
		int longi= arr.length;
		//your code goes here
		// for(int i = 0; i < longi; i++){
      StringBuilder dest = new StringBuilder();
      for (int i = (longi - 1); i >= 0; i--){
        dest.append(text.charAt(i));
      }
      System.out.println(dest);  
    
  }

  
}
