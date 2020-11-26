
from setuptools import setup
from setuptools import find_packages

setup(
    name="kartingpros",
    version="0.1.0",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'pygame==1.9.6',
    ],
    entry_points={
        "console_scripts": [
            "KartingPros=src.__main__:main"
        ]
    },
)
# echo y | pip uninstall kartingpros && python setup.py install && KartingPros
# echo y | pip3 uninstall kartingpros && python3 setup.py install && KartingPros