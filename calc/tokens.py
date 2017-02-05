# coding: utf-8

EOF = 'EOF'
INTEGER, LPAR, RPAR = 'INTEGER', 'LPAR', 'RPAR'
PLUS, MINUS, MULTIPLY, DIVISION = 'PLUS', 'MINUS', 'MULTIPLY', 'DIVISION'


class Token(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type},{self.value})'

    def __repr__(self):
        return self.__str__()
