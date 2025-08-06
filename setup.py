from setuptools import setup, find_packages

setup(
    name="kelid",
    version="2.7.4",
    author="Ali jafari",
    author_email="thealiapi@gmail.com",
    description="Simple Python code locker using marshal + base64",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iTs-GoJo/Kelid",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "kelid-encode=kelid.cli:main",
            "kelid-run=kelid.cli:main",
        ],
    },
)
