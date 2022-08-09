// //Month 1
// Payment: 10% of 20000 = 2000
// Remaining amount: 18000
// Month 2
// Payment: 10% of 18000 = 1800
// Remaining amount: 16200
// Month 3:
// Payment: 10% of 16200 = 1620
// Remaining amount: 14580

package Java;


import java.util.Scanner;


public class LoanCalculator {

  public static void main(String[] args) {
    
 
  // Scanner scanner = new Scanner(System.in);
	// 	int amount = scanner.nextInt();{
	// 	//your code goes here
  //       Integer result= 0;
        
  //   Integer x = 1;
		//  do {
    //     // System.out.println(x);
    //   result += amount*100 /10;
    //   x=+1;
    // } while(x <= 3);
    // System.out.println(result);

    Scanner scanner = new Scanner(System.in);
		int amount = scanner.nextInt();{
		//your code goes here
    int b=0;
    int x = 1;

    while(x<=3){
      x++;
      b= amount *10/100;
      amount -=b;
    }
System.out.println(amount);
     
  }
}
}