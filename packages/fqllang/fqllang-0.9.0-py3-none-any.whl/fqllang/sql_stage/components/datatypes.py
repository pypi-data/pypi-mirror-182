class SqlDatatype:
    __type__="default"

class SqlIntegerDatatype(SqlDatatype):
    __type__="integer"
    
class SqlVarcharDatatype(SqlDatatype):
    __type__="varchar(511)"
    
class SqlSerialDatatype(SqlDatatype):
    __type__="serial"
    
class SqlBooleanDatatype(SqlDatatype):
    __type__="boolean"
    