from setuptools import find_packeges, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path):
    '''
    This function will return the list of requirements
    mentioned in the requirements.txt file
    '''
    with open(file_path) as f:
        requir = f.readlines()
        requir = [x.replace('\n', '') for x in requir]
        if HYPEN_E_DOT in requir:
            requir.remove(HYPEN_E_DOT)
    return requir


setup(
    name='Diabetes_Prediction',
    version='0.0.1',
    author='Soham Pande',
    author_email='sohampande58@gmail.com',
    packages=find_packeges(),
    install_requires=get_requirements('requirements.txt')
)