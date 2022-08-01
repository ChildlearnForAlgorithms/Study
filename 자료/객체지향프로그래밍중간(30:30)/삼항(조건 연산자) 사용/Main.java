public class Main {

	public static void main(String[] args) {
		
		int[] num = { 66, 80, 84, 75, 86, 50, 90, 79, 89 };
		
		int max=0;
		// 여기에 삼항(조건) 연산자를 사용하여 실행화면과 같이 출력되도록 프로그래밍 하시오
		
		for(int i=0; i<num.length;i++){
			max=max<num[i]?num[i]:max;
		}//max보다 num[i]가 크면 num[i]를 반환, 작으면 max 반환
		
		System.out.println("값 중에서 가장 큰 값은 " + max + " 입니다.");
	}

}