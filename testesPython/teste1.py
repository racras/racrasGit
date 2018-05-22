#!/Python34/python
import cgi

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head>")
    print("<title>Cadastrando</title>")
    print ("<style>")
    print("table.steelBlueCols {border: 1px solid blue; background-color: #ffffff;  width: 400px;  text-align: left;  border-collapse: collapse;}")
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
