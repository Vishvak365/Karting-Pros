  
from setuptools import setup
from setuptools import find_packages

setup(
    name="kartingpros",
    version="0.1.0",
    include_package_data=True,
    # packages=['KartingPros', 'KartingPros.fonts', 'KartingPros.images'],
    packages=find_packages(),
    install_requires=[
        'pygame==1.9.6',
    ],
    entry_points={
        "console_scripts": [
            "KartingPros = src.main:main"
        ]
    },
)