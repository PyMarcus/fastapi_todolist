from fastapi import FastAPI 
from typing import Any
from data import ToDo
from models import ModelOfItem


app = FastAPI()  # instânicia de fastapi contém tudo que é necessário e os decorators


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
    return ToDo().listThis()


@app.post("/tarefas/post", response_model=list[ModelOfItem], status_code=201)  # é possível identificar o status code 201 etc aqui
def insertToDo(insert: ModelOfItem) -> None:
    """
    view que insere item na lista de itens a fazer
    """
    ToDo().insert(insert.dict())


@app.get("/tarefas/{id}", response_model=list[ModelOfItem])
def getItem(id: int) -> list[dict[str, Any]]:
    # retorna um elemento da lista
    todo = ToDo().listThis()
    item = filter(lambda x: x["id"] == id, todo)
    if item:
        return list(item)
    return [{"item": "não encontrado"}]
