from setuptools import setup, find_packages

setup(
    name='My_LibrarySys',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Library management system',
    url='https://github.com/KingOfOrikid/DATA533_proj_step3',
    author='Yuki Chen and Sylvia Lyu',
    author_email='yuxin.yuki.chen@gmail.com'
)