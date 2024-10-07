# calculator/basic.py

from typing import Optional, Union
from .utils import round_result

class Calculator:
    """
    기본적인 산술 연산을 제공하는 계산기 클래스.
    덧셈, 뺄셈, 곱셈, 나눗셈 연산을 제공하며,
    계산 결과에 대해 소수점 자릿수 지정(precision) 및
    결과를 항상 float로 반환할지 여부(return_float)를 조절할 수 있습니다.
    """

    def add(self, *nums: Union[int, float], precision: Optional[int] = None) -> Union[int, float]:
        """
        덧셈 연산을 수행하는 메서드.

        Args:
            *nums (Union[int, float]): 여러 개의 숫자를 가변 인자로 받습니다.
            precision (Optional[int], optional): 소수점 자릿수를 지정할 수 있는 옵션. 기본값은 None.

        Returns:
            Union[int, float]: 덧셈 결과. precision에 따라 소수점 자릿수가 반영될 수 있으며, 
                               가능한 경우 int로 반환됩니다.
        """
        result = sum(nums)  # 입력된 숫자들의 합을 계산
        return round_result(result, precision)  # precision에 맞춰 결과를 반올림하여 반환

    def subtract(self, *nums: Union[int, float], precision: Optional[int] = None) -> Union[int, float]:
        """
        뺄셈 연산을 수행하는 메서드.

        Args:
            *nums (Union[int, float]): 첫 번째 인자에서 나머지 인자들을 차례대로 뺍니다.
            precision (Optional[int], optional): 소수점 자릿수를 지정할 수 있는 옵션. 기본값은 None.

        Returns:
            Union[int, float]: 뺄셈 결과. precision에 따라 소수점 자릿수가 반영될 수 있으며,
                               가능한 경우 int로 반환됩니다.
        """
        result = nums[0]  # 첫 번째 숫자를 기준으로
        for num in nums[1:]:
            result -= num  # 차례대로 뺄셈 연산
        return round_result(result, precision)  # precision에 맞춰 결과를 반올림하여 반환

    def multiply(self, *nums: Union[int, float], precision: Optional[int] = None) -> Union[int, float]:
        """
        곱셈 연산을 수행하는 메서드.

        Args:
            *nums (Union[int, float]): 곱셈할 여러 개의 숫자를 가변 인자로 받습니다.
            precision (Optional[int], optional): 소수점 자릿수를 지정할 수 있는 옵션. 기본값은 None.

        Returns:
            Union[int, float]: 곱셈 결과. precision에 따라 소수점 자릿수가 반영될 수 있으며,
                               가능한 경우 int로 반환됩니다.
        """
        result = nums[0]  # 첫 번째 숫자를 기준으로
        for num in nums[1:]:
            result *= num  # 차례대로 곱셈 연산
        return round_result(result, precision)  # precision에 맞춰 결과를 반올림하여 반환

    def divide(self, *nums: Union[int, float], precision: Optional[int] = None) -> Union[int, float, str]:
        """
        나눗셈 연산을 수행하는 메서드. 0으로 나누는 경우 적절히 예외 처리합니다.

        Args:
            *nums (Union[int, float]): 첫 번째 인자를 기준으로 차례대로 나눕니다.
            precision (Optional[int], optional): 소수점 자릿수를 지정할 수 있는 옵션. 기본값은 None.

        Returns:
            Union[int, float, str]: 나눗셈 결과. precision에 따라 소수점 자릿수가 반영될 수 있으며,
                                    가능한 경우 int로 반환됩니다. 0으로 나누는 경우 에러 메시지를 반환합니다.
        """
        try:
            result = nums[0]  # 첫 번째 숫자를 기준으로
            for num in nums[1:]:
                result /= num  # 차례대로 나눗셈 연산
            return round_result(result, precision)  # precision에 맞춰 결과를 반올림하여 반환
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."  # 0으로 나누는 경우 에러 메시지 반환
