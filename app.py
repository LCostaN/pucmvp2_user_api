from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Game, List
from logger import logger
from schemas import *
from flask_cors import CORS

from datetime import datetime, timedelta

info = Info(title="Dog Care API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
list_tag = Tag(name="Lista de Jogo", description="Adição, visualização e remoção de Lista de Jogos à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi/swagger')


@app.post('/product', tags=[list_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(body: ProdutoSchema):
    """Adiciona um novo Jogo à base de dados
    """
    produto = Game(
        name=body.name,
        category=body.category,
        description=body.description,
        src=body.src,
        quantity=body.quantity,
    )
    logger.debug(f"Adicionando produto de nome: '{produto.name}'")
    try:
        session = Session()
        session.add(produto)
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.name}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        error_msg = "Jogo de mesmo nome já salvo na base"
        logger.warning(f"Erro ao adicionar produto '{produto.name}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item"
        logger.warning(f"Erro ao adicionar produto '{produto.name}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/products', tags=[list_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os Produtos cadastrados.

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos ")
    session = Session()
    produtos = session.query(Game).all()

    if not produtos:
        return {"products": []}, 200
    else:
        logger.debug(f"%d produtos encontrados" % len(produtos))
        print(produtos)
        return apresenta_produtos(produtos), 200


@app.get('/product', tags=[list_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
    """Faz a busca por um Jogo a partir do id do produto.

    Retorna uma representação dos produtos.
    """
    produto_id = query.id
    logger.debug(f"Coletando dados sobre produto #{produto_id}")
    session = Session()
    produto = session.query(Game).filter(Game.id == produto_id).first()

    if not produto:
        error_msg = "Jogo não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{produto_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Jogo encontrado: '{produto.name}'")
        return apresenta_produto(produto), 200


@app.delete('/product', tags=[list_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoDelBuscaSchema):
    """Deleta um Jogo a partir do nome de produto informado

    Retorna uma mensagem de confirmação da remoção.
    """
    produto_nome = unquote(unquote(query.name))
    print(produto_nome)
    logger.debug(f"Deletando dados sobre produto #{produto_nome}")
    session = Session()
    count = session.query(Game).filter(Game.name == produto_nome).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado produto #{produto_nome}")
        return {"message": "Jogo removido", "id": produto_nome}
    else:
        error_msg = "Jogo não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{produto_nome}', {error_msg}")
        return {"message": error_msg}, 404


@app.post('/schedule', tags=[list_tag],
          responses={"200": ScheduleViewSchema, "404": ErrorSchema})
def add_schedule(body: ScheduleSchema):
    """Adiciona um novo agendamento

    Retorna uma representação do agendamento.
    """
    date = datetime.strptime(body.date, "%d/%m/%Y %H:%M")
    schedule = List(
        name=body.name,
        date=date,
        src=body.src,
    )
    logger.debug(f"Adicionando agendamento de '{schedule.name}' no dia e horário '{schedule.date}'")
    try:
        session = Session()
        session.add(schedule)
        session.commit()
        logger.debug(f"Adicionado agendamento '{schedule.id}'")
        return apresenta_agendamento(schedule), 200

    except IntegrityError as e:
        error_msg = "Horário de agendamento não disponível"
        logger.warning(f"Erro ao adicionar agendamento '{schedule}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item"
        logger.error(f"Erro ao adicionar agendamento', {e}")
        return {"message": error_msg}, 400


@app.get('/schedules', tags=[list_tag],
         responses={"200": ScheduleListSchema, "404": ErrorSchema})
def get_schedules(query: ScheduleListSearchSchema):
    """Faz a busca pelos Agendamentos cadastrados a partir da data informada até os próximos 7 dias.

    Retorna uma representação da listagem de agendamentos.
    """
    try:
        initialDate = datetime.strptime(query.date, "%d/%m/%Y")
        finalDate = initialDate + timedelta(days = 8)
        logger.debug(f"Coletando agendamentos ")
        session = Session()
        schedules = session.query(List).filter(List.date >= initialDate,List.date < finalDate).all()

        if not schedules:
            return {"schedules": []}, 200
        else:
            logger.debug(f"%d agendamentos encontrados" % len(schedules))
            return apresenta_agendamentos(schedules), 200
    
    except Exception as e:
        logger.error(e)
        error_msg = f"Não foi possível buscar os agendamentos a partir de {query.date}"
        return {"message": error_msg}, 400