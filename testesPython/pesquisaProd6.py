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
	##print("div1{width:800px;height:350;border:solid 1px;box-shadow:10px 10px 10px 5px gray;border-radius:10px;"})
    ##print("Ftable {width:900px;height:100%;padding:0px;border-spacing: 0px;;background-color: white;border:solid 1px white;padding: 0px;}")
    ##print("Ftable {width:800px;height:100%;padding:0px;border-spacing:0px;border:solid 1px;border-radius:10px;}")
	##print("""<link rel="stylesheet" type="text/css" href="folha.css">""")
	##print("table.steelBlueCols {border: 1px solid blue; background-color: #ffffff;    text-align: left;  border-collapse: collapse;}")
    ##print("table.steelBlueCols tbody td {border: 1px solid gray; font-size: 12px;  font-weight: bold;  color:#808080;}")
    print("</style>")
    print("<script> function preenche(){if (formu.id.value=='') {formu.id.value=0};} </script>")
    print("</head>")
    print("<body style='font-size:small;'>")
## funcão que imprime o rodapé do HTML
    
def printFooter():
    print("</body></html>")

##Função que printa a cabeça de uma tabela
def printTabela():
    print("<table style='padding: 4px;border-spacing: 0px; background-color: white;'>")
    print("<tr>")

def printTabela1():
    print("<table style='padding: 0px;border-spacing: 0px; background-color: white;'>")
    print("<tr>")

## chama a função de impressão de cabeçalho
printHeader()

# Imprime um titulo no orpo da pagina
print("<center><div style='width:200px;height:40;border:solid 1px;box-shadow:10px 10px 10px 5px gray;border-radius:10px;'> <b><p>Pesquisa de Produtos </div></center>")

## Chama função que printa a cabeça de uma tabela
printTabela()

# recebe os dados do formulário html
form = cgi.FieldStorage()

#cria um form html e seus campos dentro da tabela e fecha a tabela
print("<form method='post' action='pesquisaProd6.py' name=formu>")
print("<td style='background-color: #fffFff;  width: 204px;box-shadow:4px 4px 4px 4px gray'>Código:	 <input type='text' name='id' style='border:0px'/></td>")
print("</tr></table>")

#Verifica se o formulário foi submetido e coloca valor passado no campo que servira de indice para o loop que monta o resultado ou seta zero neste campo
if len(form) > 0:
    print("<input type=hidden name='numReg' value="+form["numReg"].value+">")
else:
     print("<input type=hidden name='numReg' value=0>")

## cria um campo vazio chamado botao , para saber se a paginação está para frente ou para trás
print("<input type=hidden name='botao' value='0'/>")

## cria o botão de pesquisar que ao ser clicado chama a função javascript preenche que preenche o valor do campo de pesquisa, caso não tenha nada(para trazer o grid do início)
print("<br><input type='submit' style='background-color: #fffFff;  width: 100px;box-shadow:4px 4px 4px 4px gray' value='Pesquisar' ; onclick='formu.botao.value=1;preenche();formu.numReg.value=0'; />")
print("<p></p><br>")

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

print("<div style='width:900px;height:290;border:solid 1px;box-shadow:10px 10px 10px 5px gray;border-radius:10px';")
print("</div>")
## printa cabeçalho da tabela
print("<br>")
printTabela()

#cria variável de controle do listrado da tabela e cria contador para gerenciar o listrado
back="#ffffff"
contador=1

## pronta as informações de titulo do retorno
print("<tr>")
print("<td style='border: 1pt solid lightgray;width:30px;'><b>Código</td>")
print("<td style='border: 1pt solid lightgray;width:700px;'	><b>Nome</td>")
print("<td style='border: 1pt solid lightgray;width:140px;'><b>Cod Seguradora	</td>")
print("<td style='border: 1pt solid lightgray;width:190px;'><b>Num Max Parcela</td>")
print("</tr>")
## Verifica se o código é zero, se for traz o grid caso contrario traz só registro do Id enviado na pesquisa
if str(codigo)=="0" :

## faz o loop para o grid
    for indice in range(x,y):
        ##print(x)
        selecionado=retorno[indice]
        print("<tr>")
        print("<td style='border: 1pt solid lightgray; width:50px; background-color:"+back+"'>" + str((selecionado.get("produto_id"))) + "</td>")
        print("<td style='border: 1pt solid lightgray;width:800px; background-color:"+back+"'>" + str((selecionado.get("nome"))).capitalize() + "</td>")
        print("<td style='border: 1pt solid lightgray; width:140px; background-color:"+back+"'>" + str((selecionado.get("seguradora_cod_susep"))) + "</td>")
        print("<td style='border: 1pt solid lightgray; width:190px; background-color:"+back+"'>" + str((selecionado.get("num_max_parcela"))) + "</td>")
        print("</tr>")
#define a cor do listrado
        contador=contador+1
        resto = contador % 2
        if resto==0:
            back="#E8E8E8"
        else:
            back="#ffffff"
##traz só registro do Id enviado na pesquisa
else:    
    print("<tr width:800px>")
    print("<td style='border: 1pt solid lightgray;'>" + str((retorno.get("produto_id"))) + "</td>")
    print("<td style='border: 1pt solid lightgray;width:500px''>" + str((retorno.get("nome"))) + "</td>")
    print("<td style='border: 1pt solid lightgray;  width: 140px'>" + str((retorno.get("seguradora_cod_susep"))) + "</td>")
    print("<td style='border: 1pt solid lightgray;'>" + str((retorno.get("num_max_parcela"))) + "</td>")
    print("</tr>")
	
## fecha tabela do grid
print("</tr>")
print("</table><p>")
print("</div ><p>")

## cria os botõses de vai e volta da paginação e passa valores de identificação dele
##print("<div style='align:center;width:217px;height:20px;border:solid 1px;box-shadow:10px 10px 10px 5px gray;border-radius:10px;position:absolute;top:75%;left:20%;margin-top:-50px;margin-left:-50px;';")
##print("</div >")
print("<div align=center>")
print("<input type='submit' style='background-color: #ffffff;  width: 100px;box-shadow:10px 10px 10px 5px gray' value='<<<<<' ;  onclick='formu.id.value=0;formu.botao.value=1'; />&nbsp;&nbsp;")
print("<input type='submit' style='background-color: #ffffff;  width: 100px;box-shadow:10px 10px 10px 5px gray'' value='>>>>>' ;  onclick='formu.id.value=0;formu.botao.value=2'; />")
print("</div>")

print("<p onclick='abre()'> Abre Observação</p> <p onclick='fecha()'> fecha Observação</p>")
#verifica se está no grid ou registro pesquisado
if len(form) > 0 and str(form["id"].value) == "0" :

##  Se está no grid ,verifica qual botão de paginação foi clicado e seta valores para a próxima página (+ ou - 10)
    if botao=="2":
        print("""<script>document.querySelector("[name='numReg']").value = parseInt(document.querySelector("[name='numReg']").value)+10;</script>""")
    else:
        print("""<script>document.querySelector("[name='numReg']").value = parseInt(document.querySelector("[name='numReg']").value)-10;</script>""")
else:
    print("""<script>document.querySelector("[name='numReg']").value = 0</script>""")

print("""<script> function abre() {document.getElementById("obs").style.display = "block";}</script>""")
print("""<script> function fecha() {document.getElementById("obs").style.display = "none";}</script>""")
#printa o rodape do html

print("<div id='obs' style='width:1100;height:160px;border:solid 1px;box-shadow:10px 10px 10px 5px gray;border-radius:10px;display:none;'> ")
print("<br>Trata-se de uma aplicação feita em Python  ,que é acessada via web , que processa tudo no servidor e devolve o codigo para ser executado no cliente(no caso Html, javascript e css)<br>Esta plicação chama uma aplicação Java que é uma api rest que retona um json e esta rodando no apache na porta 8080 utilizando o Maven e tem banco de dados prório , ou seja ; um micro(bem micro mesmo) serviço que é consumido via url .<br>Basta que seja feita a requisiçõ para o serviço ser consumido.<br>Esta api rest é dividida em controller, service e Dao, acessando base de dados Sql ou Oracle(em breve)<br>Basicamente funciona assim :<br>O cliente chama uma rotina Python que consulta um serviço Java , que acessa uma base Sql ou oracle , que pega o retorno em json desta consulta, peocessa no servidor e devolve os dados tratados no código web cliente.<br>")
print("</div>")
printFooter() 
 
   
    
    
