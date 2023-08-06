from setuptools import setup

with open('README.md') as f:
    long_description = '\n' + f.read()

setup(
    name='snaketest',
    version='0.0.4',    
    description='A small package to help test and prototype snakemake rules',
    url='https://github.com/aLahat/snaketest',
    author='Albert',
    license='MIT License',
    packages=['snaketest'],
    install_requires=[],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.5',
    ],
)