from setuptools import find_packages, setup
from typing import List

Hypen = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a text file containing a list of Python package requirements
    and returns a list of these requirements.

    Parameters:
    file_path (str): The path to the text file containing the requirements.

    Returns:
    List[str]: A list of Python package requirements.

    Raises:
    FileNotFoundError: If the specified file does not exist.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace('\n','') for req in requirements]
        if Hypen in requirements:
            requirements.remove(Hypen)
    return requirements

setup(
   name='Ened To End ML Project',
   packages=find_packages(),
   version='0.1.0',
   description='Heart Disease Prediction',
   author='Sajib Hossain',
   author_email='sajibhossain@gmail.com',
   install_requires = get_requirements('requirements.txt')
   )