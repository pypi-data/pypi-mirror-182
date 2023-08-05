from fqllang.sql_stage.code_generators.main_elements import FindByKeySql, SelectSql, SelectWithCriteriaSql, SelectWithMatchSql
from fqllang.sql_stage.code_generators.basic_elements import Where


class SelectPostgreSql(SelectSql):
    def __init__(self, tableName: str, columns=None) -> None:
        super().__init__(tableName, columns)

    def generate(self):
        return f"SELECT {self.columns} FROM {self.tableName};"

    def __str__(self) -> str:
        return self.generate()


class SelectWithCriteriaPostgreSql(SelectWithCriteriaSql):
    def __init__(self, tableName: str, columns, criteria) -> None:
        super().__init__(tableName, columns, criteria)
        self.where = Where(criteria)

    def generate(self):
        return f"SELECT {self.columns} FROM {self.tableName} {self.where};"

    def __str__(self) -> str:
        return self.generate()


class SelectWithMatchPostgreSql(SelectWithMatchSql):
    def __init__(self, tableName: str, columns, pattern: str) -> None:
        super().__init__(tableName, columns, pattern)


class FindByKeyPostgreSql(FindByKeySql):
    def __init__(self, tableName: str, columns, keyColumn: str, keyValue: str):
        super().__init__(tableName, columns, keyColumn, keyValue)
