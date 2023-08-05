

from fqllang.sql_stage.components.basic_components import SqlField, SqlForeignKeyField
from fqllang.sql_stage.components.create_table import CreateTable
from fqllang.sql_stage.components.datatypes import SqlIntegerDatatype, SqlVarcharDatatype


class TestCreateTable:
    def test_generate(self):
        field1 = SqlField("name", SqlVarcharDatatype)
        field2 = SqlField("age", SqlIntegerDatatype)
        table = CreateTable("Project", field1, field2)
        assert table.generate() == "create table Project(name varchar(511),age integer);"
        
    def test_generate_with_foreignkey(self):
        field1 = SqlField("name", SqlVarcharDatatype)
        field2 = SqlField("Project", SqlIntegerDatatype)
        foreignkey = SqlForeignKeyField("Project", "Projects", "FQL_ID")
        table = CreateTable("Person", field1, field2, foreignkey)
        assert table.generate() == "create table Person(name varchar(511),Project integer,foreign key(Project) references Projects(FQL_ID));"
