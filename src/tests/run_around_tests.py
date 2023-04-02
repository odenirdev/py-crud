import pytest

from src.database.mock_data import subscribers


@pytest.fixture(autouse=True)
def run_around_tests():
    subscribers = [
        {
            "id": "49780c27-b5e4-4eb9-af36-afe180517fa0",
            "name": "Valentina Teresinha Maria Melo",
            "email": "valentina_melo@mls.com.br",
            "occupation": "Médica",
            "date_of_birth": "1994-01-23",
            "description": "Eu sempre quis levar minha mensagem de conscientização sobre saúde para o maior número de pessoas possível, e o BBB24 parece ser a plataforma perfeita para alcançar esse objetivo. Participar do programa seria uma oportunidade única para inspirar outros a cuidarem melhor de si mesmos e a entenderem a importância de uma vida saudável. Mal posso esperar para fazer parte desse desafio e dividir minhas experiências com o público!"
        }
    ]
    yield
