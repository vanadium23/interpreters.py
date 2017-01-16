# coding: utf-8

from token import Token, EOF, INTEGER, PLUS, MINUS


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
        result = ''

        # skip whitespaces
        while char == ' ':
            self.pos += 1
            if self.pos > len(self.text) - 1:
                return Token(EOF, None)
            char = self.text[self.pos]

        # parsing digits until next token or text
        while char.isdigit():
            result += char
            if self.pos + len(result) > len(self.text) - 1:
                break
            char = self.text[self.pos + len(result)]

        if result:
            self.pos += len(result)
            token = Token(INTEGER, int(result))
            return token

        if char == '+':
            token = Token(PLUS, '+')
            self.pos += 1
            return token
        elif char == '-':
            token = Token(MINUS, '-')
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
        op = self.current_token
        self.eat(op.type)

        right = self.current_token
        self.eat(INTEGER)

        if op.type == PLUS:
            result = left.value + right.value
        elif op.type == MINUS:
            result = left.value - right.value
        return result
