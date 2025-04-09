# functions go here
def make_statement(statement, decoration):
    """Emphasises heading by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"


# Main Routine goes here
print(make_statement("Instructions", "I"))
