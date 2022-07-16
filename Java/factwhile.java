package Java;

import java.util.Scanner;

public class factwhile {
  public static void main(String[] args) {
    
System.out.println("Write the number to analyze: ");
Scanner scanner = new Scanner(System.in); 
Integer  number = scanner.nextInt(); //Num factorial



// int  number = scanner.nextInt();
int fact = 1; //Initialization value->final result
Integer x= 1;//Incremental value
while (x <= number)//Cycle Initial condition to scanner number
{
  fact = fact * x; //fact = result between fact and incremental "x"
  ++x;//Incremental x
  
}
System.out.println("Factorial to " + number + " is: " + fact);

  }
}
