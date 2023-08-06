from setuptools import setup, find_packages

setup(
    name='census_data_collection',
    
    version='0.1.0',
    
    license='MIT',
    
    author="Jinyan Xiang",
    
    author_email='jxiang5@vt.edu',
    
    packages=['census_data_collection'],
    
    url='https://github.com/jinyan0425/census_collection',
    
    keywords =['census','american_community_survey'],
    
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
        "Operating System :: OS Independent"],

    install_requires =['pandas','Census'])
