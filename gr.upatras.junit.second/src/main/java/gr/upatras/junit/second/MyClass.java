package gr.upatras.junit.second;

public class MyClass {
	
	public String sub2num(int x, int y) {
		
		int result = 0;
		
		result = x - y;
		
		if (x == y) {
			return "ZERO";
		}
		
		if (result > 0) {
			return "POSITIVE";
		}
		
		return "NEGATIVE";
	}
	
	public static void main(String[] args) {
		MyClass m = new MyClass();
		String result = m.sub2num(0, 5);
		System.out.println("The result is " + result);
	}
}

