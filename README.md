# Pyker


## Overview
Pyker is made to help players to extract statistics and insights from poker games.

## Supported Formats
- [Pokernow](https://www.pokernow.club/)

## Usage

### Install the library
```bash
pip install "git+https://github.com/BenjaminNMitchell/Pyker#egg=pyker"
```

## Dev

### Setup
To setup the project you need a couple of prerequisites

- Python 3.8 installed on your local machine [pyenv](https://realpython.com/intro-to-pyenv/#installing-pyenv) can help install and manage python distributions
- pipenv installed on your local machine (you can run `pip install pipenv`)


```bash
# Clone the repository
git clone https://github.com/BenjaminNMitchell/Pyker.git

# Enter repo
cd Pyker

# Install dev dependencies from lock file
pipenv install --deploy --dev

# Run static checks
make static-checks
```
