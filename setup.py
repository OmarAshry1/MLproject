from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(path:str)->List[str]:
    '''Return list of requirements'''
    requirements=[]
    with open(path) as file_obj:
        requirements=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Omar',
    author_email='omar.ashry.kl@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)