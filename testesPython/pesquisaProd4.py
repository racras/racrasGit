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

form = cgi.FieldStorage()

print("<form method='post' action='pesquisaProd4.py' name=formu>")
print("<td>Código: <input type='text' name='id' /></td>")
print("</tr></table>")

if len(form) > 0:
    print(form["numReg"].value)
    print("<input type=hidden name='numReg' value="+form["numReg"].value+">")
    print("entrou no if")
else:
     print("<input type=hidden name='numReg' value=1>")
     print("entrou no else")


    ##"+form["id"].value+"'>"
print("<input type=hidden name='botao' value='p'/>")
print("<input type='submit' style='background-color: #E0FFFF;  width: 100px;' value='Pesquisar' ; onclick='formu.botao.value=1'; />")
print("<p>")

##form = cgi.FieldStorage()

if len(form) > 0  :
    codigo=form["id"].value
    botao=form["botao"].value
    numReg=form["numReg"].value
else:
    numReg=1
    #if len(numReg)<0
    #numReg=1
    print(numReg)
x=int(numReg)
y=x+10
##    print(str(x)+"aaaa")
##    if codigo!="0":
##        ##print("entrou errado")
resposta=requests.get("http://localhost:8080/servico/produto/")
##    ##elif codigo=="0":
##        ##print("entrou")
##        ##resposta=requests.get("http://localhost:8080/servico/produto/"_)
##        ##print(resposta.content)
##        
##    
##    ##print(resposta.content)
##    ##print("<p>")
retorno = resposta.json()
##    ##print(retorno.get("nome"))
##    ##print(retorno.get("produto_id"))
print("<table class=steelBlueCols>")
back="#F0FFF0"
contador=1
print("<tr>")
print("<td width= 110  align=center style=background-color:#ffffff>Id</td>")
print("<td   align=center style=background-color:#ffffff>Nome</td>")
print("<td width= 110  align=center style=background-color:#ffffff>Cod Seguradora</td>")
print("<td width= 110  align=center style=background-color:#ffffff>Num Max Parcela</td>")
##    #while row is not None:
##    if x<= len(retorno):
##        
for indice in range(x,y):
    selecionado=retorno[indice]
    print("<tr>")
    print("<td style=background-color:"+back+">" + str((selecionado.get("produto_id"))) + "</td>")
    print("<td style=background-color:"+back+">" + str((selecionado.get("nome"))) + "</td>")
    print("<td style=background-color:"+back+">" + str((selecionado.get("seguradora_cod_susep"))) + "</td>")
    print("<td style=background-color:"+back+">" + str((selecionado.get("num_max_parcela"))) + "</td>")
    contador=contador+1
    resto = contador % 2
    if resto==0:
        back="#B0E0E6"
    else:
        back="#F0FFF0"
    ##        #pagina=int(numReg)
    ##        
    ####        xxx=numReg+str(10)
    ####    xx=repr(x)
    ####    #print (pagina)
print("</tr>")
print("</table>")
####    print("<p>")
####    str="<script>formu.numReg.value ="
####    
##    str2="></script>"
##
##    #print (str + x +str2)
print("<script>formu.numReg.value=16;></script>")
#print("""<script>document.querySelector("[name='numReg']").value = 10;</script>""")


print("""<script>document.querySelector("[name='numReg']").value = parseInt(document.querySelector("[name='numReg']").value)+10;</script>""")   

   ## Lista = json.loads(retorno)
   ##for item in retorno:
             # print

printFooter() 
 
   
    
    
