#!/usr/bin/python3
import sys
from antlr4 import *
from ginaTareaLexer import ginaTareaLexer
from ginaTareaParser import ginaTareaParser
from ginaTareaVisitor import ginaTareaVisitor


class CalcVisitor(ginaTareaVisitor):
    def visitAtomo(self, ctx:ginaTareaParser.AtomoContext):
        return int(ctx.getText())

    def visitParentesis(self, ctx:ginaTareaParser.ParentesisContext):
        return self.visit(ctx.expr())

    def visitAritmetica(self, ctx:ginaTareaParser.AritmeticaContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            if r == 0:
                print('divide by zero!')
                return 0
            return l / r
    
    def visitLogica(self, ctx:ginaTareaParser.LogicaContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        if op == '<':
            return (l < r)
        elif op == '>':
            return (l > r)
        elif op == '<=':
            return (l <= r)
        elif op == '>=':
            return (l >= r)
        elif op == '&':
            return (l & r)
        elif op == '|':
            return (l | r)

    def visitPrint(self, ctx:ginaTareaParser.PrintContext):
        return self.visit(ctx.expr())

    def visitPrintString(self, ctx:ginaTareaParser.PrintStringContext):
        return ctx.STRING()

    def visitAsign(self, ctx:ginaTareaParser.AsignContext):
        text = str(ctx.ID()) + " now has the value of " +  str(ctx.STRING() )
        return text

    def visitAsignExpression(self, ctx:ginaTareaParser.AsignExpressionContext):
        text = str(ctx.ID()) + " now has the value of " + str(self.visit(ctx.expr()))
        return text

    def visitIfElse(self, ctx:ginaTareaParser.IfElseContext):
        if(self.visit(ctx.cond)):
            return self.visit(ctx.instruc)
        return self.visit(ctx.instruc2)
    
    def visitIf(self, ctx:ginaTareaParser.IfContext):
        if(self.visit(ctx.cond)):
            return self.visit(ctx.instruc)
        return "No entró a condición"

    def visitDeclaracion(self, ctx:ginaTareaParser.DeclaracionContext):
        text = str(ctx.ID()) + " fue declarada" 
        return text




def calc(line) -> float:
    input_stream = InputStream(line)

    # lexing
    lexer = ginaTareaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # parsing
    parser = ginaTareaParser(stream)
    tree = parser.program()

    # use customized visitor to traverse AST
    visitor = CalcVisitor()
    return visitor.visit(tree)



if __name__ == '__main__':
    while True:
        print(">>> ", end='')
        line = input()
        print(calc(line))
