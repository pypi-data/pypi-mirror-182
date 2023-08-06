from setuptools import setup, find_packages

setup(
    name='sudokuPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A sudoku game',
	url='https://github.com/7lu0420/TravisCI-DATA533',
    author='Shveta Sharma & Tia Wang',
    author_email='yingziwang0308@gmail.com'
)