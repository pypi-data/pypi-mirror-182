class SqlDataconstraint:
    __type__="default"
    
class SqlUniqueDataconstraint(SqlDataconstraint):
    __type__="unique"
    
class SqlNotnullDataconstraint(SqlDataconstraint):
    __type__="not null"
    
class SqlPrimarykeyDataconstraint(SqlDataconstraint):
    __type__="primary key"