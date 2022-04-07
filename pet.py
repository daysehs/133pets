import pytest  # motor / engine
import requests   # biblioteca para comunicar APIs

base_url = 'https://petstore.swagger.io/v2'  # endereço da API
headers = {'Content-Type': 'application/json'}  # os dados serão no formato json

def testar_incluir_pet():
    # Configura
  # Dados de entrada: virão do pet1.json
  # Resultado Esperado
    status_code_esperado = 200
    nome_pet_esperado = 'Bruce'
    tag_esperada = 'vacinado'

    # Executa
    resultado_obtido = requests.post(url=base_url + '/pet',
                  data=open('vendors/json/pet1.json', 'br'),
                  headers=headers
                  )
    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()       # extrai o json da response
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    # assert corpo_da_resposta['tags.name'] == tag_esperada <-- assim funcionaria se fosse Java
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada


def testar_consultar_pet():
    # 1 - Configura
    # 1.1 Dados de entrada

    pet_id = '227148'

    # 1.2 Resultados Esperados

    status_code_esperado = 200
    nome_pet_esperado = 'Bruce'
    tag_esperada = 'vacinado'


    # Executa
    resultado_obtido = requests.get(
        url=base_url + '/pet/' + pet_id,
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada


def testar_alterar_pet():
    status_code_esperado = 200
    nome_pet_esperado = 'Bruce'
    status_esperado = 'solded'

    resultado_obtido = requests.put(
        url=f'{base_url}/pet',
        data=open('C:\\Users\\Dayse Souza\\PycharmProjects\\133pets\\vendors\\json\\pet2.json', 'rb'),
        headers=headers
    )

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta["name"] == nome_pet_esperado
    assert corpo_da_resposta['status'] == status_esperado

def testar_excluir_pet():
    pet_id = '227148'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    # oi


    resultado_obtido = requests.delete(
        url=base_url + '/pet/' + pet_id,
        headers=headers
    )

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == pet_id


@pytest.mark.parametrize('pet_id,category_id,categorya-name,name,tags_id,tags_name,status') ler_dados_csv)()
def testar_incluir_pet_json_dinamico(pet_id,category_id,categorya-name,name,tags_id,tags_name,status):
    # 1 - Configura
    # 1.1 - Dados de Entrada
    # Utilizará o arquivo pets.csv

    # 1.2 - Resultado Esperados
    # Utilizará o arquivo pets_positivo.csv

    # 1.3 - Extra - Montar o json dinamicamente a partir do csv

    # 2 - Executa



    # Valida

