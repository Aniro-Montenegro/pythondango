# pythondango
Curso Python Django


## Instalação de libs com PIP

> Instalando requests
````commandline
pip install requests
````


## Arquivo Requirements
>Verificando Bibliotecas instaladas
````commandline
pip freeze
````
>Criando requirements.txt

````commandline
pip freeze > requirements.txt
````

>Instalando as dependencias pelo arquivo requirements
````commandline
pip install -r requirements.txt
````

## Flake8

>Instalando Flake8
````commandline
pip install flake8
````

>Requirements  dev
 ````commandline
pip install > requirements-dev.txt 
````

> Em ambiente de desenvolvimento
````commandline
pip install -r requirements-dev.txt
````
## Pipenv

````commandline
pip install pipenv
````

````commandline
pipenv install requests
pipenv install flake8 pytest coverage pytest-cov
````

## Pytest
````commandline
pip install pytest
````

>Rodar o teste
````commandline
pytest projeto/tests
````

## Pytest Coverage
````commandline
pip install pytest-cov
````

> Procurando bibliotecas instaladas
````commandline
pip freeze |grep cov
````

````commandline
pytest projeto --cov=projeto
````


## Django

````commandline
pipenv install django
````
> Instalando Flake8 em ambiente de desenvonvimento
````commandline
pipenv install -d flake8
````

