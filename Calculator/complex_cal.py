import cmath
from typing import Union

class ComplexCalculator:
    """
    복소수 연산을 위한 계산기 클래스.
    복소수의 덧셈, 뺄셈, 곱셈, 나눗셈, 절대값, 편각, 극좌표 변환, 직교좌표 변환 기능을 제공.
    """

    def add(self, a: complex, b: complex) -> complex:
        """
        두 복소수의 덧셈을 수행합니다.

        Args:
            a (complex): 첫 번째 복소수.
            b (complex): 두 번째 복소수.

        Returns:
            complex: 두 복소수의 합.
        """
        return a + b

    def subtract(self, a: complex, b: complex) -> complex:
        """
        두 복소수의 뺄셈을 수행합니다.

        Args:
            a (complex): 첫 번째 복소수.
            b (complex): 두 번째 복소수.

        Returns:
            complex: 첫 번째 복소수에서 두 번째 복소수를 뺀 값.
        """
        return a - b

    def multiply(self, a: complex, b: complex) -> complex:
        """
        두 복소수의 곱셈을 수행합니다.

        Args:
            a (complex): 첫 번째 복소수.
            b (complex): 두 번째 복소수.

        Returns:
            complex: 두 복소수의 곱.
        """
        return a * b

    def divide(self, a: complex, b: complex) -> Union[complex, str]:
        """
        두 복소수의 나눗셈을 수행합니다. 0으로 나누는 경우 예외 처리를 합니다.

        Args:
            a (complex): 나눗셈의 피제수.
            b (complex): 나눗셈의 제수.

        Returns:
            Union[complex, str]: 두 복소수의 나눗셈 결과.
            제수가 0일 경우, "Error: Division by zero is not allowed."라는 문자열을 반환.
        """
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    def magnitude(self, a: complex) -> float:
        """
        복소수의 절대값(크기)를 계산합니다.

        Args:
            a (complex): 절대값을 구할 복소수.

        Returns:
            float: 복소수의 크기.
        """
        return abs(a)

    def argument(self, a: complex) -> float:
        """
        복소수의 편각(Argument)를 계산합니다. 편각은 복소수의 극좌표 표현에서의 각도입니다.

        Args:
            a (complex): 편각을 구할 복소수.

        Returns:
            float: 복소수의 편각(라디안 값).
        """
        return cmath.phase(a)

    def to_polar(self, a: complex) -> tuple[float, float]:
        """
        복소수를 극좌표로 변환합니다.

        Args:
            a (complex): 극좌표로 변환할 복소수.

        Returns:
            tuple[float, float]: 복소수의 극좌표 표현 (크기, 편각).
            크기는 실수, 편각은 라디안 값입니다.
        """
        return cmath.polar(a)

    def to_rectangular(self, r: float, theta: float) -> complex:
        """
        극좌표를 직교 좌표로 변환합니다.

        Args:
            r (float): 극좌표의 크기.
            theta (float): 극좌표의 편각 (라디안 값).

        Returns:
            complex: 변환된 직교 좌표 표현.
        """
        return cmath.rect(r, theta)
