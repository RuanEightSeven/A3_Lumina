# Generated from Lumina.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LuminaParser import LuminaParser
else:
    from LuminaParser import LuminaParser

# This class defines a complete listener for a parse tree produced by LuminaParser.
class LuminaListener(ParseTreeListener):

    # Enter a parse tree produced by LuminaParser#prog.
    def enterProg(self, ctx:LuminaParser.ProgContext):
        pass

    # Exit a parse tree produced by LuminaParser#prog.
    def exitProg(self, ctx:LuminaParser.ProgContext):
        pass


    # Enter a parse tree produced by LuminaParser#stat.
    def enterStat(self, ctx:LuminaParser.StatContext):
        pass

    # Exit a parse tree produced by LuminaParser#stat.
    def exitStat(self, ctx:LuminaParser.StatContext):
        pass


    # Enter a parse tree produced by LuminaParser#assign.
    def enterAssign(self, ctx:LuminaParser.AssignContext):
        pass

    # Exit a parse tree produced by LuminaParser#assign.
    def exitAssign(self, ctx:LuminaParser.AssignContext):
        pass


    # Enter a parse tree produced by LuminaParser#expr.
    def enterExpr(self, ctx:LuminaParser.ExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#expr.
    def exitExpr(self, ctx:LuminaParser.ExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#orExpr.
    def enterOrExpr(self, ctx:LuminaParser.OrExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#orExpr.
    def exitOrExpr(self, ctx:LuminaParser.OrExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#andExpr.
    def enterAndExpr(self, ctx:LuminaParser.AndExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#andExpr.
    def exitAndExpr(self, ctx:LuminaParser.AndExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#eqExpr.
    def enterEqExpr(self, ctx:LuminaParser.EqExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#eqExpr.
    def exitEqExpr(self, ctx:LuminaParser.EqExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#relExpr.
    def enterRelExpr(self, ctx:LuminaParser.RelExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#relExpr.
    def exitRelExpr(self, ctx:LuminaParser.RelExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#somaExpr.
    def enterSomaExpr(self, ctx:LuminaParser.SomaExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#somaExpr.
    def exitSomaExpr(self, ctx:LuminaParser.SomaExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#termo.
    def enterTermo(self, ctx:LuminaParser.TermoContext):
        pass

    # Exit a parse tree produced by LuminaParser#termo.
    def exitTermo(self, ctx:LuminaParser.TermoContext):
        pass


    # Enter a parse tree produced by LuminaParser#fator.
    def enterFator(self, ctx:LuminaParser.FatorContext):
        pass

    # Exit a parse tree produced by LuminaParser#fator.
    def exitFator(self, ctx:LuminaParser.FatorContext):
        pass


    # Enter a parse tree produced by LuminaParser#decl.
    def enterDecl(self, ctx:LuminaParser.DeclContext):
        pass

    # Exit a parse tree produced by LuminaParser#decl.
    def exitDecl(self, ctx:LuminaParser.DeclContext):
        pass


    # Enter a parse tree produced by LuminaParser#tipo.
    def enterTipo(self, ctx:LuminaParser.TipoContext):
        pass

    # Exit a parse tree produced by LuminaParser#tipo.
    def exitTipo(self, ctx:LuminaParser.TipoContext):
        pass


    # Enter a parse tree produced by LuminaParser#ifStat.
    def enterIfStat(self, ctx:LuminaParser.IfStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#ifStat.
    def exitIfStat(self, ctx:LuminaParser.IfStatContext):
        pass


    # Enter a parse tree produced by LuminaParser#whileStat.
    def enterWhileStat(self, ctx:LuminaParser.WhileStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#whileStat.
    def exitWhileStat(self, ctx:LuminaParser.WhileStatContext):
        pass


    # Enter a parse tree produced by LuminaParser#forStat.
    def enterForStat(self, ctx:LuminaParser.ForStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#forStat.
    def exitForStat(self, ctx:LuminaParser.ForStatContext):
        pass


    # Enter a parse tree produced by LuminaParser#block.
    def enterBlock(self, ctx:LuminaParser.BlockContext):
        pass

    # Exit a parse tree produced by LuminaParser#block.
    def exitBlock(self, ctx:LuminaParser.BlockContext):
        pass


    # Enter a parse tree produced by LuminaParser#printStat.
    def enterPrintStat(self, ctx:LuminaParser.PrintStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#printStat.
    def exitPrintStat(self, ctx:LuminaParser.PrintStatContext):
        pass


    # Enter a parse tree produced by LuminaParser#readStat.
    def enterReadStat(self, ctx:LuminaParser.ReadStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#readStat.
    def exitReadStat(self, ctx:LuminaParser.ReadStatContext):
        pass



del LuminaParser