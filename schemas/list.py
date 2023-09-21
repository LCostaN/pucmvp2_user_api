from pydantic import BaseModel, Field
from model.list import Schedule
from typing import Optional, List


class ScheduleSchema(BaseModel):
    """ Define como um novo agendamento a ser inserido deve ser representado
    """
    date: str = Field(title="Vaga", description="Data e Hora do agendamento", default="12/07/2023 08:30")
    name: str = Field(title="Nome Pet", description="Nome do Pet", default="Rex")
    src: Optional[str] = Field(title="Foto Pet", description="Imagem do Pet (URL)", default="https://placehold.co/600x400")

class ScheduleViewSchema(BaseModel):
    """ Define como um agendamento será retornado.
    """
    id: int = Field(title="Id", description="Id do agendamento", default="1")
    date: str = Field(title="Vaga", description="Data e Hora do agendamento", default="12/07/2023 08:30")
    name: str = Field(title="Nome Pet", description="Nome do Pet", default="Rex")
    src: str = Field(title="Foto Pet", description="Imagem do Pet (URL)", default="https://placehold.co/600x400")

    
class ScheduleListSearchSchema(BaseModel):
    """ Define os parâmetros de busca da listagem de agendamentos
    """


class ScheduleListSchema(BaseModel):
    """ Define como uma listagem de agendamentos será retornada.
    """
    data: List[ScheduleSchema]

def apresenta_agendamentos(agendamentos: List[Schedule]):
    """ Retorna uma representação dos agendamentos seguindo o schema definido em
        ScheduleViewSchema.
    """
    result = []
    for agendamento in agendamentos:
        result.append(apresenta_agendamento(agendamento))

    return {"schedules": result}

def apresenta_agendamento(agendamento: Schedule):
    """ Retorna uma representação do agendamento seguindo o schema definido em
        ScheduleViewSchema.
    """
    date = agendamento.date.strftime("%d/%m/%Y %H:%M")
    return {
            "id": agendamento.id,
            "name": agendamento.name,
            "date": date,
            "src": agendamento.src,
        }