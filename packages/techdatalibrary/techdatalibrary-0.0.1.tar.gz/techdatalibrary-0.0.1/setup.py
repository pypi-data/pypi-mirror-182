from setuptools import setup

# Setting up
setup(
    name="techdatalibrary",
    version="0.0.1",
    description="Gathers tech data",
    install_requires=['pandas', 'mplfinance'],
    py_modules=['techdata'],
    package_dir={'': 'src'},
    classifiers=[
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Operating System :: OS Independent",
    ],
)
