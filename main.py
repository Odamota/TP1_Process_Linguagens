#Authored by Artur Mendes nº14870

import ply.lex as plex
from ply.lex import TOKEN
from my_lib import slurp
#from htmlreport import htmlreport


tokens = ( "VALUES", "NEWLINE")


t_ANY_ignore = ""

global linecounter

linecounter =0 


headings = []
values = []


def t_VALUES(t):
    r"""(,||^)([^",\n\r]+|"(?:[^"]|"")*")"""
    global linecounter
    Value = t.value.replace(",", "")
    if(linecounter < 1):
        headings.append(Value)
    else:
        values.append(Value)
    return t


def t_NEWLINE(t):
    r"\n"
    global linecounter
    linecounter = linecounter +1
    t.lexer.begin("INITIAL")


def t_ANY_error(t):
    print(f"Unexpected Token Error ->{t.value}")
    return t

#lexer initialization
lexer = plex.lex()
#lexer.input(slurp("sample.txt"))
readingfile = input("Escolha o ficheiro que pretende analisar: \n(sample.txt existe no diretório para testes)\n")
lexer.input(slurp(readingfile))


while True:
    tok = lexer.token()
    if not tok:
        break #no more input
    print(tok)



global table_content
global table_header

text = '''
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>
'''

heading = '<h2>Relatório de Dados do ficheiro </h2>'
table_content_heading = '<table>  <tr>'



print(headings)
print(values)
print(f"\nforam processadas cerca de {linecounter} linhas.\n")

#lexer.input(numer of lines to report)

print(f"1-{linecounter}")
linestoReport = input("Escolha o nº de linhas que pretende adicionar ao relatório : \n")
#lexer.input(slurp(linestoReport))

file = open("report.html","w+")
file.write(text)
file.write(heading)
file.write(table_content_heading)

for heading in headings:
   table_header = '<th>'+heading+'</th>'
   file.write(table_header)

table_closing_heading = '  </tr>'
file.write(table_closing_heading)
#contents
table_content_open = '<tr> '
file.write(table_content_open)
table_content_close = '  </tr>'
counter = 0


for value in values:
        if(counter < int(linestoReport)):    
            table_content =  '<td>'+value+'</td>'
            counter = counter +1 
            if(counter <= len(headings)):
                    file.write(table_content)
            else:
                
                    file.write(table_content_close)
                    file.write(table_content_open)
                    file.write(table_content)
                    counter = 1


file.write(table_content_close)
table_close = '</table>'
file.write(table_close)
html_close= '</body> </html>'
file.write(html_close)
file.close()



print(f"\nComprimento de colunas {len(headings)} .\n")