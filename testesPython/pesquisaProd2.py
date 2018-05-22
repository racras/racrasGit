#!/Python37/python
import datetime
import cgi
import json
import requests
##import requests

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head>")
    print("<title>Pesquisa Produto</title>")
    print ("<style>")
    print("table.steelBlueCols {border: 1px solid blue; background-color: #ffffff;    text-align: left;  border-collapse: collapse;}")
    print("table.steelBlueCols tbody td {border: 1px solid black; font-size: 12px;  font-weight: bold;  color:#808080;}")
    print("</style>")
    print("</head>")
    print("<body>")

def printFooter():
    print("</body></html>")

def printTabela():
    print("<table class = steelBlueCols>")
    print("<tr>")

printHeader()



print("<h2 atyle='font-size=1'>Pesquisa de Produto </h2>")
printTabela()


print("<form method='post' action='pesquisaProd2.py' name=formu>")
print("<td>Código: <input type='text' name='id' /></td>")
print("</tr></table>")
print("<input type=hidden name='botao' value='p'/>")
print("<input type='submit' style='background-color: #E0FFFF;  width: 100px;' value='Pesquisar' ; onclick='formu.botao.value=1'; />")


form = cgi.FieldStorage()

if len(form) > 0  :
    codigo=form["id"].value
    botao=form["botao"].value
    ##print(codigo+"aaaa")
    if codigo!="0":
        ##print("entrou errado")
        resposta=requests.get("http://localhost:8080/servico/produto/"+codigo)
    ##elif codigo=="0":
        ##print("entrou")
        ##resposta=requests.get("http://localhost:8080/servico/produto/"_)
        ##print(resposta.content)
        
    
    ##print(resposta.content)
    ##print("<p>")
    retorno = resposta.json()
    ##print(retorno.get("nome"))
    ##print(retorno.get("produto_id"))
    print("<table class=steelBlueCols>")
    back="#B0E0E6"
    contador=1
    print("<tr>")
    print("<td width= 110  align=center style=background-color:#ffffff>Id</td>")
    print("<td width= 140  align=center style=background-color:#ffffff>Nome</td>")
    print("<td width= 110  align=center style=background-color:#ffffff>Cod Seguradora</td>")
    print("<td width= 110  align=center style=background-color:#ffffff>Num Max Parcela</td>")
    #while row is not None:
    ##for item in retorno:
    print("<tr>")
    print("<td style=background-color:"+back+">" + str((retorno.get("produto_id"))) + "</td>")
    print("<td style=background-color:"+back+">" + str((retorno.get("nome"))) + "</td>")
    print("<td style=background-color:"+back+">" + str((retorno.get("seguradora_cod_susep"))) + "</td>")
    print("<td style=background-color:"+back+">" + str((retorno.get("num_max_parcela"))) + "</td>")
    ##   print("<td>" + str(row[4]) + "</td>")
    #contador=contador+1
    #resto = contador % 2
    #if resto==0:
    #    back="##B0E0E6"
    #else:
    #   back="#F0FFF0"
    print("</tr>")
    print("</table>")
    Lista = json.loads(retorno)
   ##for item in retorno:
             # print(item)





    
 
printFooter()
    
    
