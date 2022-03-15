# Generated from c:\Users\gina1\Documents\Tec\Compiladores\ANTLRBasics\ginaTarea.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("U\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\2\7\2\20\n\2\f\2\16\2\23\13\2\5\2\25\n\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\60\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4?")
        buf.write("\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\7\4P\n\4\f\4\16\4S\13\4\3\4\2\3\6\5\2\4\6\2")
        buf.write("\t\3\2\n\13\3\2\f\r\3\2\16\17\3\2\20\21\3\2\22\23\3\2")
        buf.write("\24\25\3\2\26\27\2a\2\24\3\2\2\2\4/\3\2\2\2\6>\3\2\2\2")
        buf.write("\b\n\5\4\3\2\t\b\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f")
        buf.write("\3\2\2\2\f\25\3\2\2\2\r\13\3\2\2\2\16\20\5\6\4\2\17\16")
        buf.write("\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22")
        buf.write("\25\3\2\2\2\23\21\3\2\2\2\24\13\3\2\2\2\24\21\3\2\2\2")
        buf.write("\25\3\3\2\2\2\26\27\7\37\2\2\27\30\7\3\2\2\30\60\5\6\4")
        buf.write("\2\31\32\7\37\2\2\32\33\7\4\2\2\33\34\7 \2\2\34\60\7\5")
        buf.write("\2\2\35\36\7\6\2\2\36\37\5\6\4\2\37 \7\7\2\2 !\5\6\4\2")
        buf.write("!\"\7\b\2\2\"#\5\6\4\2#$\7\t\2\2$\60\3\2\2\2%&\7\6\2\2")
        buf.write("&\'\5\6\4\2\'(\7\7\2\2()\5\6\4\2)*\7\t\2\2*\60\3\2\2\2")
        buf.write("+,\t\2\2\2,\60\7\37\2\2-.\t\3\2\2.\60\7\37\2\2/\26\3\2")
        buf.write("\2\2/\31\3\2\2\2/\35\3\2\2\2/%\3\2\2\2/+\3\2\2\2/-\3\2")
        buf.write("\2\2\60\5\3\2\2\2\61\62\b\4\1\2\62?\7\35\2\2\63\64\7\30")
        buf.write("\2\2\64\65\5\6\4\2\65\66\7\31\2\2\66?\3\2\2\2\678\7\32")
        buf.write("\2\289\5\6\4\29:\7\31\2\2:?\3\2\2\2;<\7\33\2\2<=\7 \2")
        buf.write("\2=?\7\34\2\2>\61\3\2\2\2>\63\3\2\2\2>\67\3\2\2\2>;\3")
        buf.write("\2\2\2?Q\3\2\2\2@A\f\13\2\2AB\t\4\2\2BP\5\6\4\fCD\f\n")
        buf.write("\2\2DE\t\5\2\2EP\5\6\4\13FG\f\t\2\2GH\t\6\2\2HP\5\6\4")
        buf.write("\nIJ\f\b\2\2JK\t\7\2\2KP\5\6\4\tLM\f\7\2\2MN\t\b\2\2N")
        buf.write("P\5\6\4\bO@\3\2\2\2OC\3\2\2\2OF\3\2\2\2OI\3\2\2\2OL\3")
        buf.write("\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\7\3\2\2\2SQ\3\2")
        buf.write("\2\2\t\13\21\24/>OQ")
        return buf.getvalue()


class ginaTareaParser ( Parser ):

    grammarFileName = "ginaTarea.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' ='", "' = \"'", "'\"'", "'if ('", "') then {'", 
                     "'} else {'", "'}'", "'int'", "'bool'", "'String'", 
                     "'float'", "'*'", "'/'", "'+'", "'-'", "'>'", "'<'", 
                     "'>='", "'<='", "'&'", "'|'", "'('", "')'", "'print('", 
                     "'print( '", "' )'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "WS", 
                      "ID", "STRING" ]

    RULE_program = 0
    RULE_statem = 1
    RULE_expr = 2

    ruleNames =  [ "program", "statem", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    INT=27
    WS=28
    ID=29
    STRING=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ginaTareaParser.StatemContext)
            else:
                return self.getTypedRuleContext(ginaTareaParser.StatemContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ginaTareaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ginaTareaParser.ExprContext,i)


        def getRuleIndex(self):
            return ginaTareaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ginaTareaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ginaTareaParser.T__3) | (1 << ginaTareaParser.T__7) | (1 << ginaTareaParser.T__8) | (1 << ginaTareaParser.T__9) | (1 << ginaTareaParser.T__10) | (1 << ginaTareaParser.ID))) != 0):
                    self.state = 6
                    self.statem()
                    self.state = 11
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ginaTareaParser.T__21) | (1 << ginaTareaParser.T__23) | (1 << ginaTareaParser.T__24) | (1 << ginaTareaParser.INT))) != 0):
                    self.state = 12
                    self.expr(0)
                    self.state = 17
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ginaTareaParser.RULE_statem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracionContext(StatemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.StatemContext
            super().__init__(parser)
            self.tipo = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ginaTareaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)


    class AsignExpressionContext(StatemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.StatemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ginaTareaParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ginaTareaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignExpression" ):
                listener.enterAsignExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignExpression" ):
                listener.exitAsignExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignExpression" ):
                return visitor.visitAsignExpression(self)
            else:
                return visitor.visitChildren(self)


    class AsignContext(StatemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.StatemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ginaTareaParser.ID, 0)
        def STRING(self):
            return self.getToken(ginaTareaParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsign" ):
                listener.enterAsign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsign" ):
                listener.exitAsign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsign" ):
                return visitor.visitAsign(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(StatemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.StatemContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.instruc = None # ExprContext
            self.instruc2 = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ginaTareaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ginaTareaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.StatemContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.instruc = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ginaTareaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ginaTareaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def statem(self):

        localctx = ginaTareaParser.StatemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statem)
        self._la = 0 # Token type
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = ginaTareaParser.AsignExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(ginaTareaParser.ID)
                self.state = 21
                self.match(ginaTareaParser.T__0)
                self.state = 22
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ginaTareaParser.AsignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(ginaTareaParser.ID)
                self.state = 24
                self.match(ginaTareaParser.T__1)
                self.state = 25
                self.match(ginaTareaParser.STRING)
                self.state = 26
                self.match(ginaTareaParser.T__2)
                pass

            elif la_ == 3:
                localctx = ginaTareaParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(ginaTareaParser.T__3)
                self.state = 28
                localctx.cond = self.expr(0)
                self.state = 29
                self.match(ginaTareaParser.T__4)
                self.state = 30
                localctx.instruc = self.expr(0)
                self.state = 31
                self.match(ginaTareaParser.T__5)
                self.state = 32
                localctx.instruc2 = self.expr(0)
                self.state = 33
                self.match(ginaTareaParser.T__6)
                pass

            elif la_ == 4:
                localctx = ginaTareaParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(ginaTareaParser.T__3)
                self.state = 36
                localctx.cond = self.expr(0)
                self.state = 37
                self.match(ginaTareaParser.T__4)
                self.state = 38
                localctx.instruc = self.expr(0)
                self.state = 39
                self.match(ginaTareaParser.T__6)
                pass

            elif la_ == 5:
                localctx = ginaTareaParser.DeclaracionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                localctx.tipo = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ginaTareaParser.T__7 or _la==ginaTareaParser.T__8):
                    localctx.tipo = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 42
                self.match(ginaTareaParser.ID)
                pass

            elif la_ == 6:
                localctx = ginaTareaParser.DeclaracionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                localctx.tipo = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ginaTareaParser.T__9 or _la==ginaTareaParser.T__10):
                    localctx.tipo = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.match(ginaTareaParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ginaTareaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PrintContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ginaTareaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class PrintStringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ginaTareaParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintString" ):
                listener.enterPrintString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintString" ):
                listener.exitPrintString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintString" ):
                return visitor.visitPrintString(self)
            else:
                return visitor.visitChildren(self)


    class AtomoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ginaTareaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomo" ):
                listener.enterAtomo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomo" ):
                listener.exitAtomo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomo" ):
                return visitor.visitAtomo(self)
            else:
                return visitor.visitChildren(self)


    class AritmeticaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ginaTareaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ginaTareaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAritmetica" ):
                listener.enterAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAritmetica" ):
                listener.exitAritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAritmetica" ):
                return visitor.visitAritmetica(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ginaTareaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class LogicaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ginaTareaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ginaTareaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ginaTareaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogica" ):
                listener.enterLogica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogica" ):
                listener.exitLogica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogica" ):
                return visitor.visitLogica(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ginaTareaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ginaTareaParser.INT]:
                localctx = ginaTareaParser.AtomoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 48
                localctx.atom = self.match(ginaTareaParser.INT)
                pass
            elif token in [ginaTareaParser.T__21]:
                localctx = ginaTareaParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(ginaTareaParser.T__21)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(ginaTareaParser.T__22)
                pass
            elif token in [ginaTareaParser.T__23]:
                localctx = ginaTareaParser.PrintContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(ginaTareaParser.T__23)
                self.state = 54
                self.expr(0)
                self.state = 55
                self.match(ginaTareaParser.T__22)
                pass
            elif token in [ginaTareaParser.T__24]:
                localctx = ginaTareaParser.PrintStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.match(ginaTareaParser.T__24)
                self.state = 58
                self.match(ginaTareaParser.STRING)
                self.state = 59
                self.match(ginaTareaParser.T__25)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ginaTareaParser.AritmeticaContext(self, ginaTareaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 63
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ginaTareaParser.T__11 or _la==ginaTareaParser.T__12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = ginaTareaParser.AritmeticaContext(self, ginaTareaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 66
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ginaTareaParser.T__13 or _la==ginaTareaParser.T__14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ginaTareaParser.LogicaContext(self, ginaTareaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 69
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ginaTareaParser.T__15 or _la==ginaTareaParser.T__16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = ginaTareaParser.LogicaContext(self, ginaTareaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 72
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ginaTareaParser.T__17 or _la==ginaTareaParser.T__18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 73
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = ginaTareaParser.LogicaContext(self, ginaTareaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 75
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ginaTareaParser.T__19 or _la==ginaTareaParser.T__20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 76
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




