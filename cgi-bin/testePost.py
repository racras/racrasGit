import json
import requests
inserir = {'produto_id':'9988','nome': 'produto testeBicca','seguradora_cod_susep': '1685','num_max_parcela': '15'}
url='http://localhost:8080/servico/produto'
headers ={'content-type':'application/json'}
r = requests.put(url,data=json.dumps(inserir),headers=headers)
###############r = requests.post(url,data=json.dumps(inserir),headers=headers)
      
print(r.status_code)
print(r.content)




