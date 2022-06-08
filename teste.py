from starlette.testclient import TestClient 
from main import app


# construção de testes 
client = TestClient(app)  # para executar pytest nome,py

def test_main_status_code() -> None:
    response = client.get('/')
    assert response.status_code == 200


def test_main_response_json() -> None:
    response = client.get('/')
    assert response.json() == {'hello':'world!'}



def test_main_tarefas() -> None:
    response = client.get('/tarefas')
    assert response.json() == [
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
