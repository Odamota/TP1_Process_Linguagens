#!/usr/bin/python3
#Author: Artur Mendes @ LESI PL 14870

#from csvReader import csvReader
from my_lib import slurp
import ply.lex as plex

#Contents  = csvReader()


tokens = ("DESCRIPTIONLINE", "COMMENT", "CONTENT", "COUNTRYNAME", "CAPITAL", "CURRENCY", "OFFICIALLANGUAGE", "HEADOFGOVERNMENT")
global mycolcounter

def t_DESCRIPTIONLINE(t):
    r"""Country [A-Z].*\n"""
    print(f"Apanha 1ª linha:-> {t.value}\n")
    pass

def t_COMMENT(t):
    r"""\#[a-z]|[A-Z]"""
    #this indicates that the line should not be counted or saved
    #following # there must be always a letter
    pass

def t_CONTENT(t):
    r"""[A-Z][a-z]+.*\,"""
    global mycolcounter
    mycolcounter = mycolcounter+1

    print(f"Catching line 1 -{mycolcounter}->{t.value}\n")
    pass

def t_COUNTRYNAME(t):
    r"""([A-Z][a-z]+),"""
    #([A-Z][a-z]+(( )?)(([A-Z])?[a-z]*)?),
    #Inicia por maiusculas, contem letras e 
    #da currencies e capital + contry name
    print(f"Nome do Pais->{t.value}\n")
    pass

def t_HEADOFGOVERNMENT(t):
    r"""(,[A-Z][a-z]+.*)\n"""
    print(f"Nome presidente->{t.value}\n")
    pass
    

def t_error(t):
    print(f"Token inesasperado - erro: {t.value}\n")
    exit(1)


lexer = plex.lex()
lexer.input(slurp("sampleFile.txt"))
lexer.token()
##print(csvReader.Top())
print("teste1") 