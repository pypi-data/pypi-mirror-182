
class FqlRefcardinality:
    __type__="default"
    
class FqlOneRefcardinality(FqlRefcardinality):
    __type__="one"
    
class FqlManyRefcardinality(FqlRefcardinality):
    __type__="many"