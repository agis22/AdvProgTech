package gr.upatras.junit.second;

import static org.junit.jupiter.api.Assertions.*;
//import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class MyClassTest {

	@Test
	void testSub2num() {
		MyClass tester = new MyClass();
		assertEquals("POSITIVE", tester.sub2num(10, 5), "10 - 5 = 5, is POSITIVE");
		assertEquals("NEGATIVE", tester.sub2num(0, 5), "0 - 5 = -5, is NEGATIVE");
		assertEquals("ZERO", tester.sub2num(5, 5), "5 - 5 = 0, is ZERO");
	}

}
