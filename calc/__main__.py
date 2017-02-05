
from interpreter import Interpreter
from lexer import Lexer

while True:
    try:
        text = input('calc> ')
    except EOFError:
        break
    if not text:
        continue
    lexer = Lexer(text)
    interpreter = Interpreter(lexer)
    result = interpreter.expr()
    print(result)
