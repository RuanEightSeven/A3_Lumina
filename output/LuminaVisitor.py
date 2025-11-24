# Generated from Lumina.g4 by ANTLR 4.13.2
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


    # Visit a parse tree produced by LuminaParser#varDecl.
    def visitVarDecl(self, ctx:LuminaParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#assign.
    def visitAssign(self, ctx:LuminaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#reflectStat.
    def visitReflectStat(self, ctx:LuminaParser.ReflectStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#inputStat.
    def visitInputStat(self, ctx:LuminaParser.InputStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#chooseStat.
    def visitChooseStat(self, ctx:LuminaParser.ChooseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#repeatStat.
    def visitRepeatStat(self, ctx:LuminaParser.RepeatStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#whilethinkStat.
    def visitWhilethinkStat(self, ctx:LuminaParser.WhilethinkStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#block.
    def visitBlock(self, ctx:LuminaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#expr.
    def visitExpr(self, ctx:LuminaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#logicOrExpr.
    def visitLogicOrExpr(self, ctx:LuminaParser.LogicOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#logicAndExpr.
    def visitLogicAndExpr(self, ctx:LuminaParser.LogicAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#equalityExpr.
    def visitEqualityExpr(self, ctx:LuminaParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#relationalExpr.
    def visitRelationalExpr(self, ctx:LuminaParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:LuminaParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:LuminaParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#unaryExpr.
    def visitUnaryExpr(self, ctx:LuminaParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:LuminaParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuminaParser#type.
    def visitType(self, ctx:LuminaParser.TypeContext):
        return self.visitChildren(ctx)



del LuminaParser