from setuptools import setup, find_packages
# setuptools 설치가 필요하므로, pip install setuptools 해준다.
# pip install wheel
# pip install twine

setup(
    # name: 패키지 이름(그리고 PYPI에 어떻게 나열될지를 지정)
    # version: 적절한 의존성 관리를 유지하는 데 중요합니다.
    # description : 설명
    # long_description : 보다 상세한 설명을 위해 별도의 README 파일을 열어서 본다.
    name='metahuman',
    version='0.1',
    description='project-metahuman-lib',
    # long_description=open('README.md').read(),

    license='MIT',

    # url: 패키지 URL. 일반적으로 깃허브(GitHub) 또는 readthedocs URL에 해당합니다.
    # download_url : 해당 라이브러리의 실행 바이너리 다운 받는 주소. 오픈소소의 경우 대부분 깃헙의 archive주소를 설정한다.
    url='https://github.com/Rarero/metahuman',
    download_url='https://github.com/Rarero/metahuman/archive/0.0.tar.gz',

    # 작성자 정보, 이름과 이메일
    author='Rarero',
    author_email='station7755@naver.com',

    # packages: 패키지에 포함해야 할 서브 패키지 목록. 이때 find_packages()가 활용됩니다.
    packages=find_packages(),

    # zip_safe: 위의 package_data 설정을 하였으면 zip_safe 설정도 해주어야 하며 False로 설정해주어야 한다.
    zip_safe=False,

    # 서포트 하는 파이썬 버전 설정, 정확한 3.6 버전을 필요로 할 경우 '=3.6'
    # 3 버전 이상에서 모두 실행 가능할 경우 '>=3' 으로 적으면 됩니다.
    python_requires='>=3.5.5',

    # 해당 라이브러리를 사용하기 위해서 인스톨 되야하는 dependency들. 해당 라이브러리를 pip을 통해 인스톨 할때 이곳에 나열된 라이브러리들을 같이 인스톨 한다.
    #      install_requires=["opencv-python>=4.5", "numpy>=1.14.0", "pandas>=0.23.4", "tqdm>=4.30.0", "gdown>=3.10.1", "Pillow>=5.2.0", "opencv-python>=3.4.4", "tensorflow>=1.9.0", "keras>=2.2.0", "Flask>=1.1.2", "mtcnn>=0.1.0", "retina-face>=0.0.1"]
    install_requires=["opencv-python", "deepface"]

    # classifiers: PYPI에 등록될 메타 데이터 설정이다. 예를 들어 서포트 하는 python 버젼 정보를 명시할수 있다. 하지만 이건 PYPI에 등록될 메타 데이터일 뿐이고 실제 빌드에는 영향을 주지 않는다. 이점 주의하자
)