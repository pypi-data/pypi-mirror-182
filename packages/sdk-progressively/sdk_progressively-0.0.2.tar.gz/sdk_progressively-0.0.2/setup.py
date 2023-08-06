from setuptools import find_packages, setup

setup(
    name='sdk_progressively',
    packages=find_packages(include=['sdk']),
    version='0.0.2',
    description='Python SDK for Progressively',
    author='Marvin Frachet <marvin.frachet@gmail.com>',
    license='MIT',
    install_requires=["requests"]
)
