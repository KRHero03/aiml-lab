
import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiml_lab",
    version="0.1",
    author="KRHero",
    author_email="krunalrank0609@gmail.com",
    description="A utility package for AIML Lab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KRHero03/aiml_lab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
