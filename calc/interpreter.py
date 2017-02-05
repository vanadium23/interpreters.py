# coding: utf-8

from tokens import INTEGER, PLUS, MINUS, MULTIPLY, DIVISION, LPAR, RPAR


# lexer for this abstract grammar
# expr = term((PLUS|MINUS)term)*
# term = factor((MULTIPLY|DIVISION)factor)*
# factor = INTEGER


class Interpreter(object):

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()

    def error(self):
        raise Exception('Syntax error')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        try:
            self.eat(INTEGER)
            return token.value
        except Exception:
            self.eat(LPAR)
            value = self.expr()
            self.eat(RPAR)
            return value

    def term(self):
        left = self.factor()

        result = left

        while self.current_token.type in (MULTIPLY, DIVISION):
            # No need because only one op
            op = self.current_token
            self.eat(op.type)

            right = self.factor()

            if op.type == MULTIPLY:
                result = result * right
            elif op.type == DIVISION:
                result = result // right

        return result

    def expr(self):
        left = self.term()

        result = left

        while self.current_token.type in (PLUS, MINUS):
            # No need because only one op
            op = self.current_token
            self.eat(op.type)

            right = self.term()

            if op.type == PLUS:
                result = result + right
            elif op.type == MINUS:
                result = result - right

        return result
