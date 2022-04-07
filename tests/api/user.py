import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}

def testar_incluir_user():

    # Configura

    # Resultado Esperado
    status_code_esperado = 200 # se a comunicação teve ida e volta
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '377302'



# Executa
    resultado_obtido = requests.post(url=base_url + '/user',
                                     data=open('C:\\Users\\Dayse Souza\\PycharmProjects\\133pets\\vendors\\json\\user1.json', 'br'),
                                     headers=headers

    )

    # Valida

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada


def testar_consultar_user():

    # Configura
    # Dados de Entrada
    code_esperado = 200
    # Resultados Esperados
    status_code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '377302'

    # Executa

    resultado_obtido = requests.post(url=base_url + '/user',
                                     data=open(
                                         'C:\\Users\\Dayse Souza\\PycharmProjects\\133pets\\vendors\\json\\user1.json',
                                         'br'),
                                     headers=headers

                                     )

    # Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada


def testar_alterar_user():

    # Configura

    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '377302'

    # Executa

    resultado_obtido = requests.post(url=base_url + '/user',
                                     data=open(
                                         'C:\\Users\\Dayse Souza\\PycharmProjects\\133pets\\vendors\\json\\user1.json',
                                         'br'),
                                     headers=headers

                                     )

    # Valida
    assert resultado_obtido.status_code == code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada


def testar_excluir_user():

    # Configura

    message_esperada = '377302'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'

    # Executa

    resultado_obtido = requests.post(url=base_url + '/user',
                                     data=open(
                                         'C:\\Users\\Dayse Souza\\PycharmProjects\\133pets\\vendors\\json\\user1.json',
                                         'br'),
                                     headers=headers

                                     )

        # Valida

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada



