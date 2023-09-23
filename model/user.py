from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from  model import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, username:str, password:str):
        """
        Usuário do sistema

        Arguments:
            username: Login de acesso e visualização
            password: Senha de acesso
        """
        
        self.username = username
        self.password = password

    def __str__(self):
        return '{ id: ' + (self.id or 'null') + ', username: ' + self.username + ' }'