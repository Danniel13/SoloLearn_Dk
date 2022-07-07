/*
You need a program to convert days to seconds.
The given code takes the amount of days as input. Complete the code to convert it to seconds and output the result. */
package Java;

import java.util.Scanner;

public class Time_converter {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
		int days = scanner.nextInt();
		Integer hours = days*24;
		Integer minutes = hours * 60;
		Integer seconds = minutes * 60;

		System.out.println(seconds);
  }
}
