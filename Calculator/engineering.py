# calculator/engineering.py

import math
from .basic import Calculator
from .utils import round_result, convert_to_radians
from typing import Optional, Union

# 각도 단위를 상수로 정의
RADIAN = 'radian'
DEGREE = 'degree'

class EngineeringCalculator(Calculator):
    """
    공학용 계산기 클래스, 기본 계산기 기능 외에 공학적 연산을 제공하는 클래스.
    Calculator 클래스를 상속받아 제곱근, 로그, 삼각 함수 등의 공학적 계산을 추가로 구현합니다.
    또한 결과를 소수점 자릿수와 원하는 타입(float 또는 int)으로 제어할 수 있습니다.
    """

    def __init__(self, precision: Optional[int] = None, return_float: bool = False):
        """
        클래스 초기화 함수.
        precision: 연산 결과의 소수점 자릿수를 지정하는 옵션 (None일 경우 자릿수 제한 없음).
        return_float: 결과값을 항상 float로 반환할지 여부를 지정하는 옵션 (기본값은 False).

        Args:
            precision (Optional[int]): 결과의 소수점 자릿수 (None이면 반올림하지 않음).
            return_float (bool): True일 경우 항상 float 타입으로 결과를 반환. False일 경우 가능한 경우 int로 반환.
        """
        self._precision = precision  # 소수점 자릿수
        self._return_float = return_float  # float 타입 강제 변환 여부

    # precision 속성에 대한 getter
    @property
    def precision(self):
        return self._precision

    # precision 속성에 대한 setter
    @precision.setter
    def precision(self, value: Optional[int]):
        """
        precision 값을 설정할 때 호출되는 함수. 입력값이 정수이거나 None인지 확인하고, 올바른 값일 경우 설정합니다.

        Args:
            value (Optional[int]): 소수점 자릿수, None일 경우 소수점 자릿수를 제한하지 않음.

        Raises:
            TypeError: value가 정수가 아니거나 None이 아닐 경우 발생.
        """
        if value is not None and not isinstance(value, int):
            raise TypeError("Precision must be an integer or None.")
        self._precision = value

    # return_float 속성에 대한 getter
    @property
    def return_float(self):
        return self._return_float

    # return_float 속성에 대한 setter
    @return_float.setter
    def return_float(self, value: bool):
        """
        return_float 값을 설정할 때 호출되는 함수. 입력값이 boolean인지 확인합니다.

        Args:
            value (bool): 결과를 float로 반환할지 여부 (True 또는 False).

        Raises:
            TypeError: value가 boolean 타입이 아닐 경우 발생.
        """
        if not isinstance(value, bool):
            raise TypeError("Return_float must be a boolean.")
        self._return_float = value

    def square_root(self, x: Union[int, float]) -> Union[int, float]:
        """
        제곱근을 계산하는 함수.

        Args:
            x (Union[int, float]): 제곱근을 구할 값.

        Returns:
            Union[int, float]: 결과값. 소수점 자릿수는 precision에 따라 제한되며, return_float에 따라 float 타입으로 반환될 수 있음.
        """
        result = math.sqrt(x)  # math.sqrt로 제곱근 계산
        return round_result(result, precision=self.precision)  # round_result를 사용하여 precision 적용

    def power(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """
        거듭제곱을 계산하는 함수.

        Args:
            x (Union[int, float]): 밑값.
            y (Union[int, float]): 지수값.

        Returns:
            Union[int, float]: 결과값. 소수점 자릿수는 precision에 따라 제한될 수 있음.
        """
        result = math.pow(x, y)  # math.pow로 거듭제곱 계산
        return round_result(result, precision=self.precision)  # round_result를 사용하여 precision 적용

    def log(self, x: Union[int, float], base: int = 10) -> Union[int, float]:
        """
        로그를 계산하는 함수 (기본값은 상용로그, base=10).

        Args:
            x (Union[int, float]): 로그를 계산할 값.
            base (int, optional): 로그의 밑값 (기본값은 10).

        Returns:
            Union[int, float]: 결과값. 소수점 자릿수는 precision에 따라 제한될 수 있음.
        """
        result = math.log(x, base)  # math.log로 로그 계산
        return round_result(result, precision=self.precision)  # round_result를 사용하여 precision 적용

    def sin(self, angle: Union[int, float], unit: str = RADIAN) -> Union[int, float]:
        """
        사인 값을 계산하는 함수. 기본적으로 라디안 단위로 계산되며, 'degree' 옵션을 사용하면 각도를 degree로 변환하여 계산 가능.

        Args:
            angle (Union[int, float]): 각도 값 (라디안 또는 degree).
            unit (str, optional): 각도의 단위 ('radian' 또는 'degree'). 기본값은 'radian'.

        Returns:
            Union[int, float]: 결과값. 소수점 자릿수는 precision에 따라 제한될 수 있음.
        """
        angle_in_radians = convert_to_radians(angle, unit)  # 각도 단위를 라디안으로 변환
        result = math.sin(angle_in_radians)  # math.sin으로 사인 값 계산
        return round_result(result, precision=self.precision)  # round_result를 사용하여 precision 적용

    def cos(self, angle: Union[int, float], unit: str = RADIAN) -> Union[int, float]:
        """
        코사인 값을 계산하는 함수. 기본적으로 라디안 단위로 계산되며, 'degree' 옵션을 사용하면 각도를 degree로 변환하여 계산 가능.

        Args:
            angle (Union[int, float]): 각도 값 (라디안 또는 degree).
            unit (str, optional): 각도의 단위 ('radian' 또는 'degree'). 기본값은 'radian'.

        Returns:
            Union[int, float]: 결과값. 소수점 자릿수는 precision에 따라 제한될 수 있음.
        """
        angle_in_radians = convert_to_radians(angle, unit)  # 각도 단위를 라디안으로 변환
        result = math.cos(angle_in_radians)  # math.cos으로 코사인 값 계산
        return round_result(result, precision=self.precision)  # round_result를 사용하여 precision 적용

    def tan(self, angle: Union[int, float], unit: str = RADIAN) -> Union[int, float]:
        """
        탄젠트 값을 계산하는 함수. 기본적으로 라디안 단위로 계산되며, 'degree' 옵션을 사용하면 각도를 degree로 변환하여 계산 가능.

        Args:
            angle (Union[int, float]): 각도 값 (라디안 또는 degree).
            unit (str, optional): 각도의 단위 ('radian' 또는 'degree'). 기본값은 'radian'.

        Returns:
            Union[int, float]: 결과값. 소수점 자릿수는 precision에 따라 제한될 수 있음.
        """
        angle_in_radians = convert_to_radians(angle, unit)  # 각도 단위를 라디안으로 변환
        result = math.tan(angle_in_radians)  # math.tan으로 탄젠트 값 계산
        return round_result(result, precision=self.precision)  # round_result를 사용하여 precision 적용
