# ExamFinalScripting
## Who made this project ?
### Group : 
    - Augustin Marie
    - Aya Najare
    - Remi Staelen

## Want to use this project ?
1. Fork / Clone
2. Create and activate a virtual environment **without poetry** 
#### Install venv 
```sh
$ py -m pip install --user virtualenv
```
#### Creating virtual env 
```sh
$ py -m venv env
```
#### Activating virtual env
```sh
$ .\env\Scripts\activate
```
3. Install requirements 
```sh
$  pip install -r requirements.txt
```
4. Install poetry 
```sh
$  pipx install poetry
```
5. Install poetry dependencies 
```sh
$  poetry install 
```
6. Activate virtual env **using poetry** 
```sh
$  poetry shell 
```


## Run the tests with poetry:
### Unit tests
Unit tests are made with the unittest, to launch them manually, run : 
```sh
$ poetry run python -m unittest discover
```

### Functional tests
Functional tests are made with behave, to launch them manually, run : 
```sh
$ poetry run behave
```

## CI made with
To manually run linters with poetry, you can use the following commands : 
### flake8
```sh
$ poetry run flake8 .
```
### Isort 
```sh
$ poetry run isort .
```
### Bandit 
```sh
$ poetry run bandit -r .
```
## Build & Publish with poetry
### Authentication 
```sh
$ poetry config http-basic.pypi <username> <password>
```
### Build & Publish 
```sh
$ poetry publish --build
```

