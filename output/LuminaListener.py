# Generated from Lumina.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by LuminaParser#varDecl.
    def enterVarDecl(self, ctx:LuminaParser.VarDeclContext):
        pass

    # Exit a parse tree produced by LuminaParser#varDecl.
    def exitVarDecl(self, ctx:LuminaParser.VarDeclContext):
        pass


    # Enter a parse tree produced by LuminaParser#assign.
    def enterAssign(self, ctx:LuminaParser.AssignContext):
        pass

    # Exit a parse tree produced by LuminaParser#assign.
    def exitAssign(self, ctx:LuminaParser.AssignContext):
        pass


    # Enter a parse tree produced by LuminaParser#reflectStat.
    def enterReflectStat(self, ctx:LuminaParser.ReflectStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#reflectStat.
    def exitReflectStat(self, ctx:LuminaParser.ReflectStatContext):
        pass


    # Enter a parse tree produced by LuminaParser#inputStat.
    def enterInputStat(self, ctx:LuminaParser.InputStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#inputStat.
    def exitInputStat(self, ctx:LuminaParser.InputStatContext):
        pass


    # Enter a parse tree produced by LuminaParser#chooseStat.
    def enterChooseStat(self, ctx:LuminaParser.ChooseStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#chooseStat.
    def exitChooseStat(self, ctx:LuminaParser.ChooseStatContext):
        pass


    # Enter a parse tree produced by LuminaParser#repeatStat.
    def enterRepeatStat(self, ctx:LuminaParser.RepeatStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#repeatStat.
    def exitRepeatStat(self, ctx:LuminaParser.RepeatStatContext):
        pass


    # Enter a parse tree produced by LuminaParser#whilethinkStat.
    def enterWhilethinkStat(self, ctx:LuminaParser.WhilethinkStatContext):
        pass

    # Exit a parse tree produced by LuminaParser#whilethinkStat.
    def exitWhilethinkStat(self, ctx:LuminaParser.WhilethinkStatContext):
        pass


    # Enter a parse tree produced by LuminaParser#block.
    def enterBlock(self, ctx:LuminaParser.BlockContext):
        pass

    # Exit a parse tree produced by LuminaParser#block.
    def exitBlock(self, ctx:LuminaParser.BlockContext):
        pass


    # Enter a parse tree produced by LuminaParser#expr.
    def enterExpr(self, ctx:LuminaParser.ExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#expr.
    def exitExpr(self, ctx:LuminaParser.ExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#logicOrExpr.
    def enterLogicOrExpr(self, ctx:LuminaParser.LogicOrExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#logicOrExpr.
    def exitLogicOrExpr(self, ctx:LuminaParser.LogicOrExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#logicAndExpr.
    def enterLogicAndExpr(self, ctx:LuminaParser.LogicAndExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#logicAndExpr.
    def exitLogicAndExpr(self, ctx:LuminaParser.LogicAndExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#equalityExpr.
    def enterEqualityExpr(self, ctx:LuminaParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#equalityExpr.
    def exitEqualityExpr(self, ctx:LuminaParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#relationalExpr.
    def enterRelationalExpr(self, ctx:LuminaParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#relationalExpr.
    def exitRelationalExpr(self, ctx:LuminaParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:LuminaParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:LuminaParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:LuminaParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:LuminaParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#unaryExpr.
    def enterUnaryExpr(self, ctx:LuminaParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#unaryExpr.
    def exitUnaryExpr(self, ctx:LuminaParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:LuminaParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by LuminaParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:LuminaParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by LuminaParser#type.
    def enterType(self, ctx:LuminaParser.TypeContext):
        pass

    # Exit a parse tree produced by LuminaParser#type.
    def exitType(self, ctx:LuminaParser.TypeContext):
        pass



del LuminaParser