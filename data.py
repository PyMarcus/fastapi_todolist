from typing import Any
from enum import Enum


class StatusOptions(str, Enum):
    """
    Se o status fugir do enum, resulta em 422 que é erro de validação
    """
    todo = 'ToDo'
    making = 'Fazendo'
    made = 'feito'


class ToDo:
    # to - do list
    todo_list: list[dict[str, Any]] = [
        {
            "id": 1,
            "title": "Estudar fastapi basicona",
            "descrição": "Afim de entender melhor api e a fastapi",
            "status": StatusOptions.todo
        },
        {
            "id": 2,
            "title": "Trabalhar",
            "descrição": "Afim de aprender e ganhar dinheiro",
            "status": StatusOptions.made
        },
    ]
    id = 2

    def listThis(self) -> list[dict[str, Any]]:
        return self.todo_list

    def insert(self, value: dict[str, Any]) -> None:
        self.id += 1
        value['id'] = self.id
        self.todo_list.append(value)
