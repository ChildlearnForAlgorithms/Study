import java.util.Scanner;
class Hufs {
	
	private String nameUniv;
	private int studentID;

	// 1) 프로그래밍 할 곳
  // setXXX(), getXXX() 메소드를 작성
	public void setNameUniv(String nameUniv){
		this.nameUniv=nameUniv;
	}//nameUniv setter
	public void setStudentID(int studentID){
		this.studentID=studentID;
	}//studentID setter
	
	public String getNameUniv(){
		return this.nameUniv;
	}//nameUniv getter
		
	public int getStudentID(){
		return this.studentID;
	}//studentID getter
	
}


public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		Hufs hufs = new Hufs(); //Hufs 객체 생성
		
		System.out.print("학교 이름을 입력하시오: ");
		String nameUniv=scanner.nextLine();
		System.out.print("학번을 입력하시오: ");
		int studentID=scanner.nextInt();
		//nameUniv와 studentID를 입력받음
		
		hufs.setNameUniv(nameUniv);
		hufs.setStudentID(studentID);
		//hufs의 nameUniv와 studentID를 setter메소드로 각각 저장
		
		
		System.out.println();
		System.out.println("학교 이름은 "+hufs.getNameUniv()+", 학번은 "+hufs.getStudentID()+"입니다.");
		//출력
		
	// 2) 프로그래밍 할 곳
  // 실행화면과 같이 키보드를 통해서 학교 이름을 입력 받아 namUniv 에 저장하고 (setter 메소드)
	// 학번을 입력받아서 studentID에 저장하고 (setter 메소드)
	// 입력된 값(nameUniv, studentID)들을 getter 메소드를 사용해서 실행화면과 같이
	// 출력하는 프로그램을 완성하시오
		
	}
}