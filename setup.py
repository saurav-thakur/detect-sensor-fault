from typing import List
from setuptools import find_packages,setup

from typing import List

def get_requirements()->List[str]:
    requirement_list = []

    with open('requirements.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            requirement_list.append(line.strip())
            
    return requirement_list



setup (

    name="sensor",
    version="0.0.1",
    author="Saurav",
    author_email="sauravthakur1341@gmail.com",
    packages=find_packages(),
    install_requires=[],
)