from setuptools import setup

REQUIRES = [
    'requests',
    'structlog',
    'curlify',
    'allure-pytest'
]

setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/isolodukhin/restclient',
    license='MIT',
    author='ilaso',
    author_email='Ilya',
    install_requirements=REQUIRES,
    description='restclient with allure and logger'
)
