
from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="kartingpros",
    version="0.2.3",
    include_package_data=True,
    author="Vishvak Seenichamy, Kevin Kosta, Wesley Boyd, Carson Hamel",
    author_email="vishvak@vishvak.com",
    packages=['kartingpros'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kosta2456/Karting-Pros',
    description="A 2D racing game",
    install_requires=[
        'pygame==1.9.6',
        'numpy==1.18.4',
    ],
    entry_points={
        "console_scripts": [
            "KartingPros=kartingpros.__main__:main"
        ]
    },
)
# echo y | pip uninstall kartingpros && python setup.py install && KartingPros
# echo y | pip3 uninstall kartingpros && python3 setup.py install && KartingPros
# python setup.py bdist_wheel --universal
# sudo python3 setup.py bdist_wheel
# twine upload dist/*
