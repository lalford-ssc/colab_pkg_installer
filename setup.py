from setuptools import setup, find_packages

setup(
    name='colab_pkg_installer',
    version='1.0.0',
    packages=find_packages(include=['colab_pkg_installer','colab_pkg_installer.*']),
    description='a Python package that can aid in properly installing custom python packages hosted in github into a Google Colab environment.',
    author='latoya a',
    author_email='',
    url='https://github.com/lalford-ssc/colab_pkg_installer',
    python_requires='>=3.10',
    install_requires=[]  
)