from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    """ Define como um usuário deve ser criado
    """
    username: str = Field(title="Usuário", description="Usuário")
    password: str = Field(title="Senha", description="Senha do usuário")

class SuccessSchema(BaseModel):
    """ Define o retorno de autenticação ou registro bem sucedido
    """
    token: str = Field(title="Token", description="JWT Token de autenticação")