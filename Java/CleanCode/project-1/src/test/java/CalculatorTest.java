import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {
    @Test
    void testSum() {
        Calculator calc = new Calculator();
        assertEquals(5, calc.sum(2, 3));
    }

    @Test
    void testSubtract() {
        Calculator calc = new Calculator();
        assertEquals(1, calc.subtract(3, 2));
    }

    @Test
    void testMultiply() {
        Calculator calc = new Calculator();
        assertEquals(6, calc.multiply(2, 3));
    }

    @Test
    void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> {
            Calculator calculator = new Calculator();
            calculator.divide(10, 0);
        });
    }


        @Test
        void testDivide() {
            Calculator calc = new Calculator();
            assertEquals(2, calc.divide(10, 5));
        }
}
