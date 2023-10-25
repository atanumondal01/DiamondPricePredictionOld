#it helps us to create our application as a package that
#can be downloaded as a package
from setuptools import find_packages,setup#to set the version or the author
from typing import List

#HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        #if HYPEN_E_DOT in requirements:
            #requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Atanu',
    author_email='atanum390@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)