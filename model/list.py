from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base

class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    src = Column(String(255))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, date:DateTime, name:str,  src:Union[str, None] = None):
        """
        Cria um agendamento

        Arguments:
            date: Data e Hora do agendamento.
            name: Nome do pet
            src: URL da imagem do pet. Opcional
        """
        
        self.date = date
        self.name = name
        self.src = src

    def __str__(self):
        return '{ id: ' + (self.id or 'null') + ', name: ' + self.name + ', date: ' + self.date.strftime("%d/%m/%Y %H:%M") + ', src: ' + self.src + ' }'