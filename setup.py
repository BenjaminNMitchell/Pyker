import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyker",
    author="Benjamin Mitchell",
    author_email="benjamin.neil.mitchell@gmail.com",
    version="0.0.1",
    packages=setuptools.find_packages(where="poker"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenjaminNMitchell/Pyker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
