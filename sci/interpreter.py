
from tokens import (
    PLUS, MINUS,
    MULTIPLY, DIVISION,
)


class NodeVisitor(object):
    def __init__(self, parser):
        self.parser = parser

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)


class Interpreter(NodeVisitor):

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIVISION:
            return self.visit(node.left) // self.visit(node.right)

    def visit_Num(self, node):
        return node.value


class RPNInterpreter(NodeVisitor):

    def visit_BinOp(self, node):
        return '{} {} {}'.format(
            self.visit(node.left),
            self.visit(node.right),
            node.op.value,
        )

    def visit_Num(self, node):
        return node.value


class LispInterpreter(NodeVisitor):

    def visit_BinOp(self, node):
        return '({} {} {})'.format(
            node.op.value,
            self.visit(node.left),
            self.visit(node.right),
        )

    def visit_Num(self, node):
        return node.value
