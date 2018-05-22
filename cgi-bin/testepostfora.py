import json
import requests

CEP = "http://api.postmon.com.br:80/v1/cep/04633010"

r = requests.get(CEP)

print(r.content)

#print("logradouro: " + jsonparsed['logradouro'])
##print 'complemento: ' + jsonparsed['complemento']
##print 'cep: ' + jsonparsed['cep']
##print 'bairro: ' + jsonparsed['bairro']

##print 'cidade: ' + jsonparsed['cidade']
##print 'cidade info:'
##print '+--- area_km2: ' + jsonparsed['cidade_info']['area_km2']
##print '+--- codigo_ibge: ' + jsonparsed['cidade_info']['codigo_ibge']

##print 'estado: ' + jsonparsed['estado']
##print 'estado info:'
##print '+--- area_km2: ' + jsonparsed['cidade_info']['area_km2']
##print '+--- codigo_ibge: ' + jsonparsed['cidade_info']['codigo_ibge']
