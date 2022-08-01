import java.util.*;

class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("정수를 입력하시오: ");
		int n = sc.nextInt();
		
		long fact = 1;
		int i = 1;
		
		do{
			fact *= i;
			i += 1;
		}while(i <= n);
		
		System.out.printf("%d!은 %d이다", n, fact);
		
	}
}
