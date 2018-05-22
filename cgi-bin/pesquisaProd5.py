#!/Python37/python
import datetime
import cgi
import json
import requests
##import requests

## função cria cabeçalho Web e definindo encode. Sem isto o Python chia . Aqui também estão sendo ciasdas as clas do css e tem também uma função javascript
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
    print("<script> function preenche(){if (formu.id.value=='') {formu.id.value=0};} </script>")
    print("</head>")
    print("<body>")
## funcão que imprime o rodapé do HTML
    
def printFooter():
    print("</body></html>")

##Função que printa a cabeça de uma tabela
def printTabela():
    print("<table class = steelBlueCols>")
    print("<tr>")

## chama a função de impressão de cabeçalho
printHeader()

# Imprime um titulo no orpo da pagina
print("<h2 atyle='font-size=1'>Pesquisa de Produto </h2>")

## Chama função que printa a cabeça de uma tabela
printTabela()

# recebe os dados do formulário html
form = cgi.FieldStorage()

#cria um form html e seus campos dentro da tabela e fecha a tabela
print("<form method='post' action='pesquisaProd6.py' name=formu>")
print("<td>Código: <input type='text' name='id' /></td>")
print("</tr></table>")

#Verifica se o formulário foi submetido e coloca valor passado no campo que servira de indice para o loop que monta o resultado ou seta zero neste campo
if len(form) > 0:
    print("<input type=hidden name='numReg' value="+form["numReg"].value+">")
else:
     print("<input type=hidden name='numReg' value=0>")

## cria um campo vazio chamado botao , para saber se a paginação está para frente ou para trás
print("<input type=hidden name='botao' value='0'/>")

## cria o botão de pesquisar que ao ser clicado chama a função javascript preenche que preenche o valor do campo de pesquisa, caso não tenha nada(para trazer o grid do início)
print("<input type='submit' style='background-color: #E0FFFF;  width: 100px;' value='Pesquisar' ; onclick='formu.botao.value=1;preenche();formu.numReg.value=0'; />")
print("<p>")

## verifica se o formulário foi submetido e se há valor no campo de pesquisa (para ser pesquisado) em caso positivo pega osvalores dos campos e joga em variáveis
if len(form) > 0 and form["id"].value != 0 :
    codigo=form["id"].value
    botao=form["botao"].value
    numReg=form["numReg"].value

## caso contrário seta valores default e seta x com número do registro ataual no grid (para paginação) e y com x +10(para o range do grid)
else:
    numReg=1
    codigo=0
x=int(numReg)
y=x+10

## se o código não tiver nada ou for igual a zero , chama o sevico que traz os registros.
if str(codigo)=="0" or  codigo == None:
     resposta=requests.get("http://localhost:8080/servico/produto/")
else :

## caso contrario chama o serviço passando o Id do produto que foi colocado no campo de pesquisa
    resposta=requests.get("http://localhost:8080/servico/produto/"+codigo)

## Dá um Json no retorno 
retorno = resposta.json()

##    ##print(retorno.get("nome"))
##    ##print(retorno.get("produto_id"))
## printa cabeçalho da tabela
printTabela()

#cria variável de controle do listrado da tabela e cria contador para gerenciar o listrado
back="#F0FFF0"
contador=1

## pronta as informações de titulo do retorno
print("<tr>")
print("<td width= 110  align=center style=background-color:#ffffff>Id</td>")
print("<td  width=500  align=center style=background-color:#ffffff>Nome</td>")
print("<td width= 110  align=center style=background-color:#ffffff>Cod Seguradora</td>")
print("<td width= 110  align=center style=background-color:#ffffff>Num Max Parcela</td>")

## Verifica se o código é zero, se for traz o grid caso contrario traz só registro do Id enviado na pesquisa
if str(codigo)=="0" :

## faz o loop para o grid
    for indice in range(x,y):
        print(x)
        selecionado=retorno[indice]
        print("<tr>")
        print("<td style=background-color:"+back+">" + str((selecionado.get("produto_id"))) + "</td>")
        print("<td style=background-color:"+back+">" + str((selecionado.get("nome"))) + "</td>")
        print("<td style=background-color:"+back+">" + str((selecionado.get("seguradora_cod_susep"))) + "</td>")
        print("<td style=background-color:"+back+">" + str((selecionado.get("num_max_parcela"))) + "</td>")

#define a cor do listrado
        contador=contador+1
        resto = contador % 2
        if resto==0:
            back="#B0E0E6"
        else:
            back="#F0FFF0"
##traz só registro do Id enviado na pesquisa
else:    
    print("<tr>")
    print("<td style=background-color:"+back+">" + str((retorno.get("produto_id"))) + "</td>")
    print("<td style=background-color:"+back+">" + str((retorno.get("nome"))) + "</td>")
    print("<td style=background-color:"+back+">" + str((retorno.get("seguradora_cod_susep"))) + "</td>")
    print("<td style=background-color:"+back+">" + str((retorno.get("num_max_parcela"))) + "</td>")

## fecha tabela do grid
print("</tr>")
print("</table><p>")

## cria os botõses de vai e volta da paginação e passa valores de identificação dele
print("<input type='submit' style='background-color: #E0FFFF;  width: 100px;' value='<<<<<' ;  onclick='formu.id.value=0;formu.botao.value=1'; />")
print("<input type='submit' style='background-color: #E0FFFF;  width: 100px;' value='>>>>>' ;  onclick='formu.id.value=0;formu.botao.value=2'; />")

#verifica se está no grid ou registro pesquisado
if len(form) > 0 and str(form["id"].value) == "0" :

##  Se está no grid ,verifica qual botão de paginação foi clicado e seta valores para a próxima página (+ ou - 10)
    if botao=="2":
        print("""<script>document.querySelector("[name='numReg']").value = parseInt(document.querySelector("[name='numReg']").value)+10;</script>""")
    else:
        print("""<script>document.querySelector("[name='numReg']").value = parseInt(document.querySelector("[name='numReg']").value)-10;</script>""")
else:
    print("""<script>document.querySelector("[name='numReg']").value = 0</script>""")

#printa o rodape do html

printFooter() 
 
   
    
    
