
from lexer import Lexer
from parser import Parser
from interpreter import (
    Interpreter,
)


def main():
    while True:
        try:
            text = input('spi> ')
        except EOFError:
            break
        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        # interpreter = RPNInterpreter(parser)
        # interpreter = LispInterpreter(parser)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)


if __name__ == '__main__':
    main()
