# calculator/__init__.py

# calculator 패키지에서 사용될 클래스 및 함수들을 정의하고 외부로 노출하는 초기화 파일입니다.

# 각 모듈에서 필요한 클래스와 함수들을 import하여 패키지 사용자들이 쉽게 접근할 수 있도록 설정합니다.

from .basic import Calculator
# basic 모듈에서 Calculator 클래스를 가져옵니다.
# 이 클래스는 기본적인 산술 연산을 수행하는 계산기 기능을 제공합니다.

from .engineering import EngineeringCalculator
# engineering 모듈에서 EngineeringCalculator 클래스를 가져옵니다.
# 이 클래스는 Calculator 클래스를 상속받아 추가적인 공학 계산 기능(삼각함수, 로그 등)을 제공합니다.

from .complex_cal import ComplexCalculator
# complex_cal 모듈에서 ComplexCalculator 클래스를 가져옵니다.
# 이 클래스는 복소수 연산을 처리하는 기능을 제공합니다.

from .utils import round_result, convert_to_radians
# utils 모듈에서 round_result 함수와 convert_to_radians 함수를 가져옵니다.
# round_result 함수는 계산 결과를 지정된 소수점 자릿수로 반올림하는 기능을 제공하며,
# convert_to_radians 함수는 각도를 라디안으로 변환하는 유틸리티 함수입니다.

# __all__ 변수를 정의하여 패키지 외부에서 import * 를 사용할 때 노출될 이름들을 명시합니다.
# 즉, 사용자가 `from calculator import *` 구문을 사용할 때 아래에 정의된 클래스와 함수들만 노출됩니다.

__all__ = [
    'Calculator',  # 기본적인 계산기 클래스
    'EngineeringCalculator',  # 공학용 계산기 클래스
    'ComplexCalculator',  # 복소수 계산기 클래스
    'round_result',  # 계산 결과를 반올림하는 유틸리티 함수
    'convert_to_radians'  # 각도를 라디안으로 변환하는 유틸리티 함수
]
