# calculator/utils.py

import math
from typing import Union

def round_result(value: Union[int, float], precision: int = None) -> Union[int, float]:
    """
    결과값을 지정된 정밀도로 반올림하는 함수
    """
    if precision is not None:
        return round(value, precision)
    return value

def convert_to_radians(angle: Union[int, float], unit: str = 'radian') -> float:
    """
    각도를 라디안으로 변환하는 함수
    """
    if unit == 'degree':
        return math.radians(angle)
    return angle