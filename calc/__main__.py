
from interpreter import Interpreter

while True:
    try:
        text = input('calc> ')
    except EOFError:
        break
    if not text:
        continue
    interpreter = Interpreter(text)
    result = interpreter.expr()
    print(result)
