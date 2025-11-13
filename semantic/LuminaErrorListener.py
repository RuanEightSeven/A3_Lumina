from antlr4.error.ErrorListener import ErrorListener

class LuminaErrorListener(ErrorListener):
    def __init__(self):
        super(LuminaErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Linha {line}:{column} — {msg}")

    def has_errors(self):
        return len(self.errors) > 0

    def report(self):
        print("\n❌ Erros sintáticos encontrados:")
        for err in self.errors:
            print(f" - {err}")
