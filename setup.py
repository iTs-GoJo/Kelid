from setuptools import setup, find_packages

setup(
    name="kelid",
    version="1.9.7",
    description="Kelid is a Python code locker using marshal and base64.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Ali-Jafari",
    author_email="thealiapi@gmail.com",
    url="https://github.com/iTs-GoJo/kelid",  # آدرس گیت‌هابت رو جایگزین کن اگه داری
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "kelid = kelid.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
