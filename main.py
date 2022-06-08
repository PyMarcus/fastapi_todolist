from fastapi import FastAPI 
from typing import Any
from pydantic import BaseModel

app = FastAPI()  # instânicia de fastapi contém tudo que é necessário e os decorators


class ModelOfItem(BaseModel):
    """Permite criar os schemas nas docs"""
    id: int
    title: str 
    status: str = '' # status pode vir vazio




# to - do list
todo_list: list[dict[str, Any]]  = [
    {   
        "id":1,
        "title": "Estudar fastapi basicona",
        "descrição": "Afim de entender melhor api e a fastapi",
        "status": "Em progresso"
    },
     {   
        "id":2,
        "title": "Trabalhar",
        "descrição": "Afim de aprender e ganhar dinheiro",
        "status": "daqui a pouco"
    },
]


@app.get("/")  # get para o endpoint raiz
def main():   # para executar uvicorn main:app --reload (gera servidor de desenvolvimento e o reload monitora o arquivo)
    """
    Mainzao que informa hello, world! (ISSO VAI APARECER NA DOC)
    ele renderiza no browser o json abaixo
    """
    return {"hello": "world!"}


@app.get("/tarefas", response_model=list[ModelOfItem])
def todo() -> list[dict[str, Any]]:
    """
    View que exibe coisas a fazer
    """
    return todo_list