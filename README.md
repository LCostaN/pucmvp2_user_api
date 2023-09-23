# MVP 2 - Usuários API

API de criação e autenticação de usuários

## Descrição

Esta API cuida da autenticação e criação dos usuários do MVP2 - Lucas Nantes.

## Executando o projeto

Para executar o projeto, é necessário usar a ferramenta docker e criar o container. O Dockerfile já está configurado e só é necessário rodar os comandos:

`docker build -t mvp2_user_api .`

`docker run -d --name mvp2_user_api -p 5000:5000 mvp2_user_api`

## Rotas

### /

* POST - Autentica usuário

### /new

* POST - Cria novo usuário
