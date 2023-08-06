from os import path
from setuptools import setup, find_packages

try:
    current_path = path.abspath(path.dirname(__file__))
except NameError:
    current_path = None

try:
    with open(path.join(current_path, 'README.md')) as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='find_oper',
    version='1.1',
    license='MIT License',
    author="nuqo888",
    author_email='vladimirovich.aleksei.ru@gmail.com',
    description='select the operator covering the largest number of regions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'main=find_oper:main',
        ],
    },
)