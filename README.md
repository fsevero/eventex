# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/fsevero/eventex.svg)](https://travis-ci.org/fsevero/eventex)
[![Code Health](https://landscape.io/github/fsevero/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/fsevero/eventex/master)
[![Code Climate](https://codeclimate.com/github/fsevero/eventex/badges/gpa.svg)](https://codeclimate.com/github/fsevero/eventex)
[![codecov.io](https://codecov.io/github/fsevero/eventex/coverage.svg?branch=master)](https://codecov.io/github/fsevero/eventex?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/e9e56e864b92420fb4ffda3e53f1a6da)](https://www.codacy.com/app/severo-fabricio/eventex)

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com .env
6. Execute os testes

```console
git clone git@github.com:fsevero/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroky config:set DEBUG=False
# configura email
git push heroku master --force
```
