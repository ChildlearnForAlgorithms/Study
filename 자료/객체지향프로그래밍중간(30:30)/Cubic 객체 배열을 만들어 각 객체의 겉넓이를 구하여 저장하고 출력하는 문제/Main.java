class Cubic {
	int line;
	public Cubic(int line){
		this.line=line;
	}//생성자
	public void setLine(int line){
		this.line=line;
	}//line을 설정하는 메소드
	
	public int getLine(){
		return this.line;
	}//line의 값을 받는 메소드
	
	public int getS(){
		return this.line*this.line*6;
	}//면적을 구하는 메소드
	
	// 생성자와 setXXX(), getXXX() 메소드를 구현
	// 정육면체(Cubic) 객체의 겉넓이 = line * line * 6
	
}

public class Main {
	public static void main(String[] args) {
		Cubic[] c = new Cubic[6];
		for(int i=0;i<c.length;i++){
			c[i] = new Cubic(i); //c[i]에 Cubic 객체 생성
			c[i].setLine(c[i].getS()); //c[i]의 line을 getS 메소드의 결과로 저장
			System.out.println("Cubic["+(i+1)+"] 면적은 "+c[i].getLine()); //출력
		}
	// 길이가 0~5인 Cubic 객체 6개를 가지는 배열을 생성
	// 배열에 있는 모든 Cubic 객체의 겉넓이를 구하여 각 객체 배열의 line 필드에 저장
  // 결과 값은 실행화면과 같이 출력
	}
}