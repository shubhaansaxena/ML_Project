from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
        print(f"Final requirements: {requirements}")
    return requirements

setup(
name = 'ML_Project',
version = '0.0.1',
author = 'Shubhaan',
author_email = 'shubhaan.saxena@gmail.com',
packages = find_packages(),
install_requires = get_requirements('Requirements.txt')
)