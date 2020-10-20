from setuptools import setup
from setuptools import find_packages

setup(
    name="Karting-Pros",
    version="Prototype",
    include_package_data=True,
    # packages=['KartingPros', 'KartingPros.fonts', 'KartingPros.images'],
    packages=find_packages(),
    install_requires=[
        'pygame==1.9.6',
    ],
    entry_points={
        "console_scripts": [
            "KartingPros = KartingPros.__main__:main"
        ]
    },
)
# pip uninstall Karting_Pros-Prototype-py2.py3-none-any.whl && pip install Karting_Pros-Prototype-py2.py3-none-any.whl && KartingPros
# python setup.py bdist_wheel --universal