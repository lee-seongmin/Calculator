import pytest
from calculator import Calculator, EngineeringCalculator, ComplexCalculator

# 기본 계산기 덧셈 테스트
def test_basic_add():
    """
    테스트 설명:
    - 기본 계산기(Calculator)의 덧셈 기능을 테스트합니다.
    - 1과 2를 더했을 때 3이 반환되는지 확인합니다.
    """
    calc = Calculator()  # Calculator 클래스 인스턴스 생성
    assert calc.add(1, 2) == 3  # add(1, 2)의 결과가 3인지 확인

# 공학용 계산기 사인 함수 테스트
def test_engineering_sin():
    """
    테스트 설명:
    - 공학용 계산기(EngineeringCalculator)의 사인 계산 기능을 테스트합니다.
    - 90도의 사인값이 약 1.0에 근접하는지 확인합니다.
    - pytest.approx()를 사용하여 부동 소수점 비교 시 오차를 허용합니다.
    """
    eng_calc = EngineeringCalculator()  # EngineeringCalculator 클래스 인스턴스 생성
    assert eng_calc.sin(90, unit='degree') == pytest.approx(1.0, 0.01)  # sin(90)의 결과가 1.0에 근접하는지 확인 (오차 허용 0.01)

# 공학용 계산기 제곱근 함수 테스트
def test_engineering_square_root():
    """
    테스트 설명:
    - 공학용 계산기(EngineeringCalculator)의 제곱근 계산 기능을 테스트합니다.
    - 16의 제곱근이 4.0인지 확인합니다.
    """
    eng_calc = EngineeringCalculator()  # EngineeringCalculator 클래스 인스턴스 생성
    assert eng_calc.square_root(16) == 4.0  # square_root(16)의 결과가 4.0인지 확인

# 복소수 계산기 덧셈 테스트
def test_complex_add():
    """
    테스트 설명:
    - 복소수 계산기(ComplexCalculator)의 복소수 덧셈 기능을 테스트합니다.
    - 복소수 (1 + 2i)와 (3 + 4i)를 더했을 때 (4 + 6i)가 반환되는지 확인합니다.
    """
    complex_calc = ComplexCalculator()  # ComplexCalculator 클래스 인스턴스 생성
    assert complex_calc.add(complex(1, 2), complex(3, 4)) == complex(4, 6)  # (1+2i) + (3+4i)의 결과가 (4+6i)인지 확인

# 복소수 계산기 크기(절대값) 계산 테스트
def test_complex_magnitude():
    """
    테스트 설명:
    - 복소수 계산기(ComplexCalculator)의 크기(절대값) 계산 기능을 테스트합니다.
    - 복소수 (3 + 4i)의 크기(절대값)가 5.0인지 확인합니다.
    - 절대값 계산은 피타고라스 정리에 기반합니다.
    """
    complex_calc = ComplexCalculator()  # ComplexCalculator 클래스 인스턴스 생성
    assert complex_calc.magnitude(complex(3, 4)) == 5.0  # 복소수 (3+4i)의 절대값이 5.0인지 확인
