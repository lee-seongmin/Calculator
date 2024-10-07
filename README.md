Calculator 패키지 구조
calculator/ ├── LICENSE ├── init.py ├── basic.py ├── engineering.py ├── complex.py ├── utils.py ├── README.md ├── requirements.txt ├── setup.py └── tests/ └── test_calculator.py

Calculator 패키지
Calculator 패키지는 기본적인 산술 연산뿐만 아니라 공학적 연산과 복소수 연산 기능을 제공하는 Python 패키지입니다. 이 패키지는 Calculator, EngineeringCalculator, ComplexCalculator 클래스를 통해 다양한 계산 기능을 지원합니다.

주요 기능
Calculator 클래스: 기본적인 덧셈, 뺄셈, 곱셈, 나눗셈 기능 제공.
EngineeringCalculator 클래스: 제곱근, 로그, 삼각함수와 같은 공학적 연산 기능 제공.
ComplexCalculator 클래스: 복소수의 덧셈, 뺄셈, 곱셈, 나눗셈, 절대값 계산, 편각 계산 기능 제공.
설치 방법
패키지를 설치하려면, 루트 디렉토리에서 다음 명령어를 실행하세요:

소스 코드에서 직접 설치
git clone https://github.com/lee-seongmin/Calculator cd calculator pip install .

사용법
기본 계산기
from calculator import Calculator

기본 계산기 인스턴스 생성
calc = Calculator()

덧셈
print(calc.add(1, 2, 3)) # 출력: 6

곱셈
print(calc.multiply(2, 4)) # 출력: 8

나눗셈
print(calc.divide(10, 2)) # 출력: 5

공학용 계산기
from calculator import EngineeringCalculator

공학용 계산기 인스턴스 생성
eng_calc = EngineeringCalculator()

제곱근 계산
print(eng_calc.square_root(16)) # 출력: 4.0

로그 계산 (기본 밑: 10)
print(eng_calc.log(100)) # 출력: 2.0

사인 계산 (각도: 30도)
print(eng_calc.sin(30, angle_unit='degree')) # 출력: 0.5

복소수 계산기
from calculator import ComplexCalculator

복소수 계산기 인스턴스 생성
complex_calc = ComplexCalculator()

복소수 덧셈
print(complex_calc.add(complex(1, 2), complex(3, 4))) # 출력: (4+6j)

복소수의 절대값 계산
print(complex_calc.magnitude(complex(3, 4))) # 출력: 5.0

테스트
pip install pytest pytest tests/
