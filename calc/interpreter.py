# coding: utf-8

from token import Token, EOF, INTEGER, PLUS


class Interpreter(object):

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Syntax error')

    def get_next_token(self):

        if self.pos > len(self.text) - 1:
            return Token(EOF, None)

        char = self.text[self.pos]

        if char.isdigit():
            token = Token(INTEGER, int(char))
            self.pos += 1
            return token

        if char == '+':
            token = Token(PLUS, '+')
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        # ???
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        # No need because only one op
        # op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value
        return result
