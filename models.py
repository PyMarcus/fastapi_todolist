from pydantic import BaseModel
from data import StatusOptions


class ModelOfItem(BaseModel):
    """Permite criar os schemas nas docs"""
    id: int
    title: str
    status: StatusOptions # status pode vir vazio
