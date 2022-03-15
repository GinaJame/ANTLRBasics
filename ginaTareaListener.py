# Generated from c:\Users\gina1\Documents\Tec\Compiladores\ANTLRBasics\ginaTarea.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ginaTareaParser import ginaTareaParser
else:
    from ginaTareaParser import ginaTareaParser

# This class defines a complete listener for a parse tree produced by ginaTareaParser.
class ginaTareaListener(ParseTreeListener):

    # Enter a parse tree produced by ginaTareaParser#program.
    def enterProgram(self, ctx:ginaTareaParser.ProgramContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#program.
    def exitProgram(self, ctx:ginaTareaParser.ProgramContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#AsignExpression.
    def enterAsignExpression(self, ctx:ginaTareaParser.AsignExpressionContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#AsignExpression.
    def exitAsignExpression(self, ctx:ginaTareaParser.AsignExpressionContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#Asign.
    def enterAsign(self, ctx:ginaTareaParser.AsignContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#Asign.
    def exitAsign(self, ctx:ginaTareaParser.AsignContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#ifElse.
    def enterIfElse(self, ctx:ginaTareaParser.IfElseContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#ifElse.
    def exitIfElse(self, ctx:ginaTareaParser.IfElseContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#if.
    def enterIf(self, ctx:ginaTareaParser.IfContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#if.
    def exitIf(self, ctx:ginaTareaParser.IfContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#declaracion.
    def enterDeclaracion(self, ctx:ginaTareaParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#declaracion.
    def exitDeclaracion(self, ctx:ginaTareaParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#Print.
    def enterPrint(self, ctx:ginaTareaParser.PrintContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#Print.
    def exitPrint(self, ctx:ginaTareaParser.PrintContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#PrintString.
    def enterPrintString(self, ctx:ginaTareaParser.PrintStringContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#PrintString.
    def exitPrintString(self, ctx:ginaTareaParser.PrintStringContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#Atomo.
    def enterAtomo(self, ctx:ginaTareaParser.AtomoContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#Atomo.
    def exitAtomo(self, ctx:ginaTareaParser.AtomoContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#Aritmetica.
    def enterAritmetica(self, ctx:ginaTareaParser.AritmeticaContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#Aritmetica.
    def exitAritmetica(self, ctx:ginaTareaParser.AritmeticaContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#Parentesis.
    def enterParentesis(self, ctx:ginaTareaParser.ParentesisContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#Parentesis.
    def exitParentesis(self, ctx:ginaTareaParser.ParentesisContext):
        pass


    # Enter a parse tree produced by ginaTareaParser#Logica.
    def enterLogica(self, ctx:ginaTareaParser.LogicaContext):
        pass

    # Exit a parse tree produced by ginaTareaParser#Logica.
    def exitLogica(self, ctx:ginaTareaParser.LogicaContext):
        pass



del ginaTareaParser