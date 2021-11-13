#!/usr/bin/python3
#Author: Artur Mendes @ LESI PL 14870
import ply.lex as plex
from ply.lex import TOKEN
from my_lib import slurp

class csvReader:
    "A stack based Reader for CSV files such as SampleFile.txt"

    

    @staticmethod
    def builder(**kwargs):
        obj = csvReader()
        obj.lexer = plex.lex(module=obj, **kwargs)
        return obj

    def parse(self, filename):
        contents = slurp(filename)
        self.lexer.input(contents)
        for token in iter(self.lexer.token, None):
            pass
        return self.count

csvReader = csvReader.builder()
#listaPaises = csvReader.Lista("sample_test.txt")
#pp = PrettyPrinter(indent=4, width=10)
# pp.pprint(listaPaises) 
#

#list/stack for CountryName, Capital, Currency, Official Language and Head of Government


