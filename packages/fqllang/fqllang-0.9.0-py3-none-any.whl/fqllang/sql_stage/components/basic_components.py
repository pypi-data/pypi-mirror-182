class SqlField:
    def __init__(self, name, datatype, *dataconstraints) -> None:
        self.name = name
        self.datatype = datatype.__type__
        self.dataconstraints = [dataconstraint.__type__ for dataconstraint in dataconstraints]
        
    def generate(self):
        datatype = self.datatype
        dataname_datatype = f"{self.name} {datatype}"
        dataconstraints = " ".join(self.dataconstraints)
        return f"{dataname_datatype} {dataconstraints}" if len(self.dataconstraints) else dataname_datatype

    def __str__(self) -> str:
        return self.generate()
    

class SqlForeignKeyField:
    def __init__(self, key, refpath, fieldName) -> None:
        self.key = key
        self.fieldName = fieldName
        self.refpath = refpath
        
    def generate(self):
        return f"foreign key({self.key}) references {self.refpath}({self.fieldName})"