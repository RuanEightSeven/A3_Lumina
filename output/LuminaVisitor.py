# Generated from Lumina.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LuminaParser import LuminaParser
else:
    from LuminaParser import LuminaParser

# This class defines a complete generic visitor for a parse tree produced by LuminaParser.

class LuminaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LuminaParser#prog.
    def visitProg(self, ctx:LuminaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#stat.
    def visitStat(self, ctx:LuminaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#assign.
    def visitAssign(self, ctx:LuminaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#expr.
    def visitExpr(self, ctx:LuminaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#orExpr.
    def visitOrExpr(self, ctx:LuminaParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#andExpr.
    def visitAndExpr(self, ctx:LuminaParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#eqExpr.
    def visitEqExpr(self, ctx:LuminaParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#relExpr.
    def visitRelExpr(self, ctx:LuminaParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#somaExpr.
    def visitSomaExpr(self, ctx:LuminaParser.SomaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#termo.
    def visitTermo(self, ctx:LuminaParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#fator.
    def visitFator(self, ctx:LuminaParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#decl.
    def visitDecl(self, ctx:LuminaParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#tipo.
    def visitTipo(self, ctx:LuminaParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#ifStat.
    def visitIfStat(self, ctx:LuminaParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#whileStat.
    def visitWhileStat(self, ctx:LuminaParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#forStat.
    def visitForStat(self, ctx:LuminaParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#block.
    def visitBlock(self, ctx:LuminaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#printStat.
    def visitPrintStat(self, ctx:LuminaParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#readStat.
    def visitReadStat(self, ctx:LuminaParser.ReadStatContext):
        return self.visitChildren(ctx)



del LuminaParser