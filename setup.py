from setuptools import find_packages, setup
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()


__version__="0.0.0"

REPO_NAME = "Text_Summarization_NLP"
AUTHOR_USER_NAME = "Ran-Dhir-Singh"
SRC_REPO = "src"
AUTHOR_EMAIL = "randhirsingh7777777@gmail.com"

def get_requirements(file_path:str)->List[str]:
    """
    returns the list of requirements from the requirements.txt file
    """
    HYPHEN_E_DOT = '-e .'
    requirements =[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python app for text summarization using NLP",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
