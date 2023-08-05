from fqllang.sql_stage.code_generators.main_elements import CreateSql
from fqllang.sql_stage.code_generators.basic_elements import ColumnList, FieldList


class CreatePostgreSql(CreateSql):
    def __init__(self, tableName: str, columns: ColumnList, fields: FieldList) -> None:
        super().__init__(tableName, columns)
        self.fields = fields

    def generate(self):
        result = f"CREATE TABLE {self.tableName}("
        result += f"{self.fields}"
        result += f");"
        return result
