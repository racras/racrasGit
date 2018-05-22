import requests
URL = "http://localhost:8080/servico/produto/"
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'produto_id':716}
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
print("batata")
dado = r.json()
x=0
y=10

#indice=0
for indice in range(10,20):
    retorno = dado[indice]
    print(retorno.get("produto_id")) 
    print(retorno.get("nome"))

      #


#retorno = data['produto_id'][0]['geometry']['location']['lat']
#print (retorno)
