from fqllang.sql_stage.components.datatypes import SqlBooleanDatatype, SqlDatatype, SqlIntegerDatatype, SqlSerialDatatype, SqlVarcharDatatype


class FqlDatatype:
    __type__ = "default"
    __sql__ = SqlDatatype


class FqlNumberDatatype(FqlDatatype):
    __type__ = "number"
    __sql__ = SqlIntegerDatatype


class FqlTextDatatype(FqlDatatype):
    __type__ = "text"
    __sql__ = SqlVarcharDatatype


class FqlSerialDatatype(FqlDatatype):
    __type__ = "serial"
    __sql__ = SqlSerialDatatype


class FqlBooleanDatatype(FqlDatatype):
    __type__ = "boolean"
    __sql__ = SqlBooleanDatatype
