import os

def getGrammar():
    path = os.path.realpath(os.path.dirname(__file__))
    with open(f"{path}/grammar/fqlgrammar.tx") as f:
        return f.read()

def getGrammarPath():
    path = os.path.realpath(os.path.dirname(__file__))
    return f"{path}/grammar/fqlgrammar.tx"

def getClassName(object):
    return object.__class__.__name__


