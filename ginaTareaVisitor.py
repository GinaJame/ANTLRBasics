# Generated from c:\Users\gina1\Documents\Tec\Compiladores\ANTLRBasics\ginaTarea.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ginaTareaParser import ginaTareaParser
else:
    from ginaTareaParser import ginaTareaParser

# This class defines a complete generic visitor for a parse tree produced by ginaTareaParser.

class ginaTareaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ginaTareaParser#program.
    def visitProgram(self, ctx:ginaTareaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#AsignExpression.
    def visitAsignExpression(self, ctx:ginaTareaParser.AsignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#Asign.
    def visitAsign(self, ctx:ginaTareaParser.AsignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#ifElse.
    def visitIfElse(self, ctx:ginaTareaParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#if.
    def visitIf(self, ctx:ginaTareaParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#declaracion.
    def visitDeclaracion(self, ctx:ginaTareaParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#Print.
    def visitPrint(self, ctx:ginaTareaParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#PrintString.
    def visitPrintString(self, ctx:ginaTareaParser.PrintStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#Atomo.
    def visitAtomo(self, ctx:ginaTareaParser.AtomoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#Aritmetica.
    def visitAritmetica(self, ctx:ginaTareaParser.AritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#Parentesis.
    def visitParentesis(self, ctx:ginaTareaParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ginaTareaParser#Logica.
    def visitLogica(self, ctx:ginaTareaParser.LogicaContext):
        return self.visitChildren(ctx)



del ginaTareaParser