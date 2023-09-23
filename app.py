from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from utils import tokenize
from model import Session, User
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="User API - MVP2", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
user_tag = Tag(name="Usuário", description="Autenticação e criação de usuário")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi/swagger, tela de documentação do Swagger
    """
    return redirect('/openapi/swagger')


@app.post('/', tags=[user_tag], responses={
    "200": SuccessSchema, 
    "401": ErrorSchema, 
    "422": ErrorSchema, 
    "500": ErrorSchema
})
def login(body: UserSchema):
    """Autentica os dados informados
    """
    try:
        user = User(username=body.username, password=body.password)
        logger.debug(f"Autenticando usuário: '{user.username}'")
        session = Session()
        exists = session.query(User).filter(User.username == user.username, User.password == user.password).first()
        
        if not exists:
            error_msg = "Usuário ou senha não encontrados"
            return {"message": error_msg}, 401

        logger.debug("Autenticação OK")

        token = tokenize(user.username)

        return {"token": token}, 200
    except IntegrityError as e:
        error_msg = "Usuário ou senha não encontrados"
        return {"message": error_msg}, 422
    
    except Exception as e:
        error_msg = "Não foi possível autenticar no momento"
        return {"message": error_msg}, 500


@app.post('/new', tags=[user_tag], responses={"200": SuccessSchema, "422": ErrorSchema, "500": ErrorSchema})
def register(body: UserSchema):
    """Cria um novo usuário no sistema
    """
    user = User(username=body.username, password=body.password)

    try:
        session = Session()
        session.add(user)
        session.commit()
        logger.debug(f"Adicionado usuário '{user.id}'")

        token = tokenize(user.username)

        return {"token": token} ,200

    except IntegrityError as e:
        error_msg = "Nome de usuário não disponível"
        return {"message": error_msg}, 422

    except Exception as e:
        error_msg = "Não foi possível criar o usuário"
        logger.error(f"Register Error: ', {e}")
        return {"message": error_msg}, 500