public class Kata {

	public static void main(String[] args) {

	int firstNumber = 10;

	int secondNumber = 2;


	int evenAndOdd = subtract(firstNumber , secondNumber);
	System.out.print(subtract(firstNumber , secondNumber));

	}
		public static int evenOddCalculator (int userNumber) {

			if (userNumber % 2 == 0) {
	            		System.out.println("This is an even number");
			}
	    	  	    else {
	            		System.out.println("This is an odd number");
			    }
				return userNumber;
	    	  	    
		}
		public static boolean primeNumberCheck (int userNumber) {
		
			int counter = 0;
		
			for(int i = 1; i <= userNumber; i++) {
				if (userNumber % i == 0) {
					counter += 1;
				}
			
			}		

				if (counter == 2) {
					return true;
				}  
		
					else  {
					return false;
					}
		}
		public static int subtract(int firstNumber , int secondNumber) {

		int answer = firstNumber - secondNumber;

		return answer;
		}
		

}