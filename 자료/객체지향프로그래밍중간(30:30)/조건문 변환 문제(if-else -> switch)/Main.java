public class Main {

	public static void main(String[] args) {
		char ch =(char)((int) (Math.random()*4) + 'a');

		/* 아래의 if-else문을 switch문으로 변환하시오
		if(ch == 'a') {
			System.out.println("a 입니다");
		} else if(ch == 'b') {	
			System.out.println("b 입니다");
		} else if(ch == 'c') {
			System.out.println("c 입니다");
		} else {
			System.out.println("d 입니다");
		}
		*/
		switch (ch){
			case 'a':
				System.out.println("a 입니다");
				break;
			case 'b':
				System.out.println("b 입니다");
				break;
			case 'c':
				System.out.println("c 입니다");
				break;
			default:
				System.out.println("d 입니다");
				break;
		}
		
	}
}