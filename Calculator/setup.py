from setuptools import setup, find_packages

# setup() 함수는 패키지의 메타데이터와 패키지 설치를 위한 정보를 설정하는 함수입니다.
# 여기서는 calculator 패키지의 기본 정보와 의존성 등을 정의합니다.

setup(
    # 패키지의 이름을 지정합니다. 
    # 이 이름은 패키지를 설치할 때 사용됩니다. (예: pip install calculator)
    name='calculator',

    # 패키지의 버전을 설정합니다. 
    # 주기적으로 패키지를 업데이트할 때 이 버전을 업데이트하여 관리할 수 있습니다.
    version='1.0',

    # 패키지에 대한 간단한 설명을 작성합니다.
    # 이 설명은 패키지를 설치할 때 또는 PyPI(파이썬 패키지 인덱스) 같은 곳에 등록할 때 사용됩니다.
    description='A basic and engineering calculator with complex number operations',

    # 패키지의 저자를 명시합니다.
    # 저자의 이름을 작성하며, 이 정보는 패키지의 소유자 또는 관리자에게 해당됩니다.
    author='Seongmin Lee',

    # find_packages() 함수는 현재 디렉토리에서 패키지로 정의된 모든 서브 디렉토리를 찾아줍니다.
    # 이를 통해 패키지 내의 모든 모듈을 자동으로 인식하고 포함시킵니다.
    packages=find_packages(),

    # 설치 시 필요한 의존 패키지를 명시합니다.
    # 설치 과정에서 해당 라이브러리들을 자동으로 설치합니다.
    # 'math'와 'cmath'는 파이썬 내장 모듈이므로, 외부 패키지가 필요한 경우에만 명시합니다.
    # 잘못된 부분: math와 cmath는 내장 모듈로 install_requires에 명시할 필요가 없습니다.
    
    install_requires=[
        # 'math'와 'cmath'는 내장 모듈로 install_requires에 명시할 필요가 없습니다.
    ]
)
