'''
Bruno C. Zaccariello RA: 1700604
Rodrigo Sena de Oliveira RA: 1701596
'''

'''
a API da climatempo está em https://advisor.climatempo.com.br

faça:
    1) Crie uma conta e consiga uma chave sua para acessar
    2) Teste no postman um exemplo de temperatura atual (veja a documentacao)
    3) Crie uma funcao temp_sao_paulo que retorna o temperatura atual em sao paulo
    4) Crie uma funcao temp_fortaleza que retorna o temperatura atual em fortaleza
    5) Crie uma função pega_id que recebe o nome da cidade e retorna seu id 
    6) Desafio: Crie uma funcao pega_temp que recebe o nome da cidade e retorna 
    a sua temperatura
'''

import requests as req

chave='37f83391e8c5948bb8c3269ae224d0b5'

def tempo_atual(id_cidade):
        url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{}/current?token={}".format(id_cidade, chave)
        retorno = req.get(url).json()
        data = retorno['data']
        print(url)

        dadosCidade = {
            'ID Cidade': id_cidade,
            'Nome':retorno['name'],
            'Temperatura':data['temperature']
            }
        return(dadosCidade)

def temp_sao_paulo():
        url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3477/current?token={}".format(chave)
        retorno = req.get(url).json()
        data = retorno['data']
        print(url)

        dadosCidade = {
            'ID Cidade':retorno['id'],
            'Nome':retorno['name'],
            'Temperatura':data['temperature']
            }
        return(dadosCidade)

def temp_fortaleza():
        url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/8050/current?token={}".format(chave)
        retorno = req.get(url).json()
        data = retorno['data']
        print(url)

        dadosCidade = {
            'ID Cidade':retorno['id'],
            'Nome':retorno['name'],
            'Temperatura':data['temperature']
            }
        return(dadosCidade)

def pega_id(nome_cidade):
        url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={}&token={}".format(nome_cidade, chave)
        retorno = req.get(url).json()
        print(url)
        string = ''
        for i in retorno:
                print('Cidade: {} Estado: {}'.format(i['name'], i['state']))
        if len(retorno) > 1 :
                a = str(input('Selecione o Estado correto da sua cidade: '))
                for i in retorno :
                        if i['state'] == a :
                                item = i
                        else :
                                'id invalido'
        else:
                item = retorno[0]
        return(item['id'])

def pega_temp(nome_cidade):
        url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={}&token={}".format(nome_cidade, chave)
        retorno = req.get(url).json()
        print(url)
        for i in retorno:
                print(i)
        if len(retorno) > 1 :
                a = int(input('Selecione o id correto da sua cidade: '))
                for i in retorno :
                        if i['id'] == a :
                                item = i
                        else :
                                'id invalido'
        else:
                item = retorno[0]
        url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{}/current?token={}".format(item['id'], chave)
        retorno = req.get(url).json()
        data = retorno['data']
        dadosCidade = {
            'ID Cidade':retorno['id'],
            'Nome':retorno['name'],
            'State':retorno['state'],
            'Temperatura':data['temperature'],
            'Condição':data['condition']
                    }

        return(dadosCidade)

temp_fortaleza()
    
