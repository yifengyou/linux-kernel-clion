from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='linuxkernelclion',
    version='0.9.9',
    description='Generate CMakeLists.txt from a compile_commands.json, just for fun~',
    long_description="linux kernel clion",
    url='https://github.com/yifengyou/linuxkernelclion',
    author='Abigail & yifengyou',
    license='MIT',
    classifiers=[
        'Development Status :: 9 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='linux kernel c cmake development c++',
    packages=find_packages(),
    entry_points={'console_scripts': ['linuxkernelclion=linuxkernelclion:main']},
)
