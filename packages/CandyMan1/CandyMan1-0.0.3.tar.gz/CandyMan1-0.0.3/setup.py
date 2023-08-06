from setuptools import setup

setup(
    name='CandyMan1',
    version='0.0.3',    
    description='A package for astronomy stuffs',
    url='https://github.com/backyard-Py/candyman',
    author='himangshu147-git',
    author_email='himangshu147@invail.mail',
    license='BSD 2-clause',
    packages=['candyman1'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",        
        'Programming Language :: Python :: 3.10',
    ],
)