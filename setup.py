from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read lines from the line
            lines =file.readlines()
            # process of each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found")
    return requirement_lst

setup(
    Name="Network Security",
    version="0.0.1",
    author="ramsai",
    author_email="ponugotiramsai@gmail.com ",
    packages=find_packages(),
    install_requires=get_requirements()
)
