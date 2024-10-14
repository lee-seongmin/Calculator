# Calculator

`Calculator` 패키지는 기본적인 산술 연산, 공학적 연산, 복소수 연산을 지원하는 Python 패키지입니다. 이 패키지는 다양한 계산 작업을 수행할 수 있는 `Calculator`, `EngineeringCalculator`, `ComplexCalculator` 클래스를 제공합니다.

## 목차

1. [환경](#환경)
2. [프로젝트 개요](#프로젝트-개요)
3. [디렉토리 구조](#디렉토리-구조)
4. [설치 방법](#설치-방법)
5. [사용법](#사용법)
6. [테스트](#테스트)
7. [라이선스](#라이선스)

## 환경

- Python 3.8 이상

## 프로젝트 개요

이 패키지는 다음과 같은 기능을 제공합니다:

- **기본 산술 연산**: 덧셈, 뺄셈, 곱셈, 나눗셈
- **공학적 연산**: 제곱근, 로그, 삼각함수 계산
- **복소수 연산**: 복소수 덧셈, 뺄셈, 곱셈, 나눗셈, 절대값, 편각 계산

## 디렉토리 구조

```bash
calculator/
├── LICENSE
├── __init__.py
├── basic.py
├── engineering.py
├── complex.py
├── utils.py
├── README.md
├── requirements.txt
├── setup.py
└── tests/
    └── test_calculator.py
```

## 설치 방법

소스 코드를 클론하여 설치할 수 있습니다:

```bash
git clone https://github.com/lee-seongmin/Calculator.git
cd calculator
pip install .
```

## 사용법

### 기본 계산기

```python
from calculator import Calculator

# 기본 계산기 인스턴스 생성
calc = Calculator()

# 덧셈
print(calc.add(1, 2, 3))  # 출력: 6

# 곱셈
print(calc.multiply(2, 4))  # 출력: 8

# 나눗셈
print(calc.divide(10, 2))  # 출력: 5
```

### 공학용 계산기

```python
from calculator import EngineeringCalculator

# 공학용 계산기 인스턴스 생성
eng_calc = EngineeringCalculator()

# 제곱근 계산
print(eng_calc.square_root(16))  # 출력: 4.0

# 로그 계산 (기본 밑: 10)
print(eng_calc.log(100))  # 출력: 2.0

# 사인 계산 (각도: 30도)
print(eng_calc.sin(30, angle_unit='degree'))  # 출력: 0.5
```

### 복소수 계산기

```python
from calculator import ComplexCalculator

# 복소수 계산기 인스턴스 생성
complex_calc = ComplexCalculator()

# 복소수 덧셈
print(complex_calc.add(complex(1, 2), complex(3, 4)))  # 출력: (4+6j)

# 복소수의 절대값 계산
print(complex_calc.magnitude(complex(3, 4)))  # 출력: 5.0
```

## 테스트

테스트를 실행하려면 `pytest`를 설치한 후 다음 명령어를 실행하세요:

```bash
pip install pytest
pytest tests/
```

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE.txt) 파일을 참조하세요.
