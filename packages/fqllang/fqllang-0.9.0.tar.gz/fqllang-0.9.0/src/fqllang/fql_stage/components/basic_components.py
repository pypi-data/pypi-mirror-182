
import fqllang.fql_stage.components.create_form as create
from fqllang.fql_stage.components.datatypes import FqlNumberDatatype
from fqllang.fql_stage.components.refcardinalities import FqlManyRefcardinality, FqlOneRefcardinality
from fqllang.sql_stage.components.basic_components import SqlField, SqlForeignKeyField
from fqllang.sql_stage.components.datatypes import SqlIntegerDatatype


class Fql:
    pass


class FqlField:
    def __init__(self, name, datatype, *dataconstraints) -> None:
        self.name = name
        self.datatype = datatype
        self.dataconstraints = dataconstraints

    def sql_code(self):
        return self.to_sql_field().generate()
    
    def to_sql_field(self):
        dataconstraints = [
            dataconstraint.__sql__ for dataconstraint in self.dataconstraints]
        datatype = self.datatype.__sql__
        return SqlField(self.name, datatype, *dataconstraints)


class FqlReference:
    # def __init__(self, dataName, refCardinality, refPath, refConstraint) -> None:
    def __init__(self, dataName, refCardinality, refPath) -> None:
        self.dataName = dataName
        self.refCardinality = refCardinality
        self.refPath = refPath
        # self.refConstraint = refConstraint        

    def get_fields(self):
        def create_fields():
            key = FqlField(self.dataName, FqlNumberDatatype)
            foreignKey = FqlForeignKey(self.dataName, self.refPath)
            return [key, foreignKey]
        return [] if self.refCardinality.__type__=='many' else create_fields()

    def get_extracomponent(self, baseName):
        def create_form(baseName):
            name = f"{baseName}_{self.refPath}"
            basename_field = FqlField(f"fk_{baseName}", FqlNumberDatatype)
            fk_basename = FqlForeignKey(f"fk_{baseName}", baseName)
            refpath_field = FqlField(f"fk_{self.refPath}", FqlNumberDatatype)
            fk_refpath = FqlForeignKey(f"fk_{self.refPath}", self.refPath)
            return create.Form(name, basename_field, fk_basename, refpath_field, fk_refpath)
        if self.refCardinality.__type__=='many': return create_form(baseName)
    
class FqlForeignKey:
    def __init__(self, key, refpath) -> None:
        self.key = key
        self.refpath = refpath
        
    def sql_code(self):
        return self.to_sql_reference().generate()
    
    def to_sql_reference(self):
        return SqlForeignKeyField(self.key, self.refpath, "FQL_ID")


class RefCardinality:
    def __init__(self, cardinality1=None, cardinality2=None) -> None:
        self.cardinality1 = cardinality1
        self.cardinality2 = cardinality2


class RefConstraint:
    def __init__(self, constraint) -> None:
        self.constraint = constraint


class SimpleId:
    def __init__(self, id) -> None:
        self.id = id
        
    def sql_code(self):
        return str(self.id)
    
    def __str__(self) -> str:
        return self.sql_code()


class DataPath:
    def __init__(self, *dataPath) -> None:
        self.path = dataPath

    def __iter__(self):
        for data in self.path:
            yield data


class DataLabelList:
    def __init__(self, *dataLabels) -> None:
        self.dataLabels = dataLabels


class DataLabel(SimpleId):
    def __init__(self, id) -> None:
        super().__init__(id)


class All:
    def __init__(self, all) -> None:
        self.star = all
