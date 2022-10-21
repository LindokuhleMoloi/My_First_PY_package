from setuptools import setup, find_packages
setup(
    name='mypackage',
    version='0.1',
    packages= find_packages(exclude= ['tests*']),
    license='MIT',
    description='Py package example',
    long_description= open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/LindokuhleMoloi/mypackage/',
    author="Lindokuhle Moloi",
    author_email="lindokuhlepearlsonmoloi@gmail.com"
)