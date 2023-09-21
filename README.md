# Projeto API MVP1

Esse projeto executa a API para ser consumida no projeto front-end de [MVP 1 - Puc RJ - Lucas Nantes da Costa](https://github.com/LCostaN/puc2023mvp_front)

## Descrição

O projeto MVP consiste em um agendamento de banho para cães.
Também permite visualizar a lista de produtos em estoque para os clientes que vão visitar o pet shop.
Não permite compra online, no entanto.

## Como executar

Para executar o projeto devemos:

1. Configurar um ambiente virtual, a fim de evitar que os pacotes deste projeto sejam instalados globalmente.
2. Instalar as dependências do projeto que se encontram no arquivo requirements.txt
3. Executar o arquivo app.py que é o ponto de partida do programa

### 1. Configurando o ambiente virtual

Para ativar o ambiente virtual, utilizamos o comando

```bash
./env/Scripts/activate
```

Em Linux ou MacOS o comando pode divergir, portanto siga as instruções [neste link](https://virtualenv.pypa.io/en/latest/user_guide.html) caso precise ativar em outra plataforma.

**Atenção:** Caso o seu ambiente virtual não tenha sido devidamente ativado, a instalação das dependências pode entrar em conflito com algum outro projeto e falhar. Recomenda-se fortemente que utilize o ambiente virtual para isolar as dependências deste projeto para somente este projeto.

### 2. Instalando as dependências

O requirements.txt contém todas as dependências do projeto já listadas. Para instalá-las, basta utilizar o comando

```bash
pip install -r requirements.txt
```

### 3. Executando o projeto

Execute o comando

```bash
flask run --host 0.0.0.0 --port 5000
```

para iniciar o servidor e acesse <http://localhost:5000> no browser de sua escolha.
Se o servidor foi iniciado corretamente, você será redirecionado para a página de documentação Swagger do projeto.

*Observação: 5000 é a porta padrão utilizada neste projeto. Caso a porta esteja ocupada, ele tentará iniciar o projeto em outra porta. Você pode verificar a porta utilizada nas mensagens que aparecem após execução do comando. Se for caso o projeto deve ser acessado em **localhost:< porta >***

## Rotas

As rodas são divididas para Produto (product, products) e Agendamento (schedule).
A documentação pode ser acessada após rodar o projeto para uma explicação mais detalhada de cada rota.

### /product

* GET
* POST
* DELETE

### /products

* GET

### /schedule

* GET
* POST
