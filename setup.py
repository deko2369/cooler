import os
from setuptools import setup, find_packages

setup(
    name='cooler',
    version='0.0.1',
    author='Kei Nishiyama',
    author_email='deko2369@gmail.com',
    description='Tempature and IR controller',
    license='MIT',
    keywords='',
    url='http://dkok.net/cooler',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'spidev==3.2'
    ],
    test_suite='tests',
    tests_require=[
        'mock'
    ],
    entry_points={
        'console_scripts': [
            'cooler = cooler:main'
        ]
    },
    long_description='TBD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License'
    ],
)
