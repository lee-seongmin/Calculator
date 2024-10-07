import math
from typing import Union, Optional
from .utils import round_result  # round_result를 가져옴

class Calculator:
    '''
    기본적인 산술 연산을 제공하는 클래스.
    *args는 여러 개의 인자를 받기 위한 매개변수.
    **kwargs는 precision(소수점 자릿수)과 return_float(결과를 float로 반환할지 여부)을 지정할 수 있는 옵션.

    Methods:
        - add(*num, **kwargs): 여러 개의 숫자를 더하는 함수.
        - subtract(*num, **kwargs): 여러 개의 숫자를 차례대로 빼는 함수.
        - multiply(*num, **kwargs): 여러 개의 숫자를 차례대로 곱하는 함수.
        - divide(*num, **kwargs): 여러 개의 숫자를 차례대로 나누는 함수.
    '''

    def add(self, *num: Union[int, float], **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        덧셈 연산을 수행하는 함수입니다.

        Args:
            *num (Union[int, float]): 여러 개의 정수 또는 실수.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 결과 값.
        '''
        result = sum(num)
        return round_result(result, **kwargs)

    def subtract(self, *num: Union[int, float], **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        뺄셈 연산을 수행하는 함수입니다.

        Args:
            *num (Union[int, float]): 첫 번째 값을 기준으로 나머지를 차례대로 뺌.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 결과 값.
        '''
        result = num[0]
        for n in num[1:]:
            result -= n
        return round_result(result, **kwargs)

    def multiply(self, *num: Union[int, float], **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        곱셈 연산을 수행하는 함수입니다.

        Args:
            *num (Union[int, float]): 곱셈을 수행할 여러 개의 값.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 결과 값.
        '''
        result = num[0]
        for n in num[1:]:
            result *= n
        return round_result(result, **kwargs)

    def divide(self, *num: Union[int, float], **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        나눗셈 연산을 수행하는 함수입니다. 0으로 나누는 경우 예외 처리를 포함.

        Args:
            *num (Union[int, float]): 나눗셈을 수행할 값들.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 결과 값 또는 에러 메시지.
        '''
        try:
            result = num[0]
            for n in num[1:]:
                result /= n
            return round_result(result, **kwargs)
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."


class EngineeringCalculator(Calculator):
    '''
    Calculator 클래스를 상속받아 추가적인 공학 계산 기능을 제공하는 클래스.

    Methods:
        - square_root(x, **kwargs): 제곱근을 계산하는 함수.
        - power(x, y, **kwargs): 거듭제곱을 계산하는 함수.
        - log(x, base=10, **kwargs): 로그를 계산하는 함수.
        - ln(x, **kwargs): 자연로그를 계산하는 함수.
        - sin(x, angle_unit='radian', **kwargs): 사인 값을 계산하는 함수.
        - cos(x, angle_unit='radian', **kwargs): 코사인 값을 계산하는 함수.
        - tan(x, angle_unit='radian', **kwargs): 탄젠트 값을 계산하는 함수.
    '''

    def square_root(self, x: Union[int, float], **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        주어진 숫자의 제곱근을 계산하는 함수.

        Args:
            x (Union[int, float]): 제곱근을 구할 값.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 제곱근 값.
        '''
        result = x ** 0.5
        return round_result(result, **kwargs)

    def power(self, x: Union[int, float], y: Union[int, float], **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        주어진 값을 거듭제곱하는 함수.

        Args:
            x (Union[int, float]): 밑값.
            y (Union[int, float]): 지수값.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 거듭제곱 값.
        '''
        result = x ** y
        return round_result(result, **kwargs)

    def log(self, x: Union[int, float], base: int = 10, **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        주어진 값의 로그를 계산하는 함수. 기본 밑은 10(상용로그).

        Args:
            x (Union[int, float]): 로그를 구할 값.
            base (int, optional): 로그의 밑값. 기본값은 10.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 로그 값.
        '''
        result = math.log(x, base)
        return round_result(result, **kwargs)

    def ln(self, x: Union[int, float], **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        주어진 값의 자연로그(밑이 e)를 계산하는 함수.

        Args:
            x (Union[int, float]): 자연로그를 구할 값.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 자연로그 값.
        '''
        result = math.log(x)
        return round_result(result, **kwargs)

    def sin(self, x: Union[int, float], angle_unit: str = 'radian', **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        주어진 각도의 사인 값을 계산하는 함수.

        Args:
            x (Union[int, float]): 각도 값.
            angle_unit (str, optional): 각도 단위 ('radian' 또는 'degree'). 기본값은 'radian'.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 사인 값.
        '''
        if angle_unit == 'degree':
            x = math.radians(x)
        result = math.sin(x)
        return round_result(result, **kwargs)

    def cos(self, x: Union[int, float], angle_unit: str = 'radian', **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        주어진 각도의 코사인 값을 계산하는 함수.

        Args:
            x (Union[int, float]): 각도 값.
            angle_unit (str, optional): 각도 단위 ('radian' 또는 'degree'). 기본값은 'radian'.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 코사인 값.
        '''
        if angle_unit == 'degree':
            x = math.radians(x)
        result = math.cos(x)
        return round_result(result, **kwargs)

    def tan(self, x: Union[int, float], angle_unit: str = 'radian', **kwargs: Optional[dict]) -> Union[int, float, str]:
        '''
        주어진 각도의 탄젠트 값을 계산하는 함수.

        Args:
            x (Union[int, float]): 각도 값.
            angle_unit (str, optional): 각도 단위 ('radian' 또는 'degree'). 기본값은 'radian'.
            **kwargs (Optional[dict]): 추가 옵션으로 precision과 return_float을 포함.

        Returns:
            Union[int, float, str]: 계산된 탄젠트 값.
        '''
        if angle_unit == 'degree':
            x = math.radians(x)
        result = math.tan(x)
        return round_result(result, **kwargs)


# __all__ 변수를 정의하여 외부에서 import * 사용 시 노출될 클래스들 명시
__all__ = ['Calculator', 'EngineeringCalculator']


if __name__ == '__main__':
    '''
    모듈을 직접 실행할 때 간단한 데모를 실행합니다.
    '''
    
    calc = Calculator()
    eng_calc = EngineeringCalculator()
    
    # 기본 계산기 사용 예시
    print("기본 계산기 사용 예시")
    print(f"더하기: {calc.add(1, 2, 3)}")
    print(f"곱하기: {calc.multiply(2, 4, 6)}")
    print(f"반올림 자릿수를 지정한 나누기: {calc.divide(100, 2, 5, precision=3)}")

    # 공학용 계산기 사용 예시
    print("\n공학용 계산기 사용 예시")
    print(f"제곱근: {eng_calc.square_root(16)}")
    print(f"n의 몇승: {eng_calc.power(6, 3)}")
    print(f"상용로그: {eng_calc.log(100)}")
    print(f"삼각함수-사인: {eng_calc.sin(30, angle_unit='degree')}")
