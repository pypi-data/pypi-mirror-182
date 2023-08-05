

from fqllang.fql_stage.components.basic_components import FqlField, FqlReference
from fqllang.fql_stage.components.create_form import Form
from fqllang.fql_stage.components.datatypes import FqlTextDatatype
from fqllang.fql_stage.components.refcardinalities import FqlManyRefcardinality, FqlOneRefcardinality


class TestForm:
    def test_classify_references(self):
        name = "Projects"
        field1 = FqlField("name", FqlTextDatatype)
        reference1 = FqlReference(
            "Employee", FqlManyRefcardinality, "Employees")
        fields, components = Form(
            name, field1, reference1).classify_references([reference1])
        assert len(list(components)) == 1 and len(list(fields)) == 0

    def test_classify_references2(self):
        name = "Projects"
        field1 = FqlField("name", FqlTextDatatype)
        reference1 = FqlReference(
            "Employee", FqlOneRefcardinality, "Employees")
        fields, components = Form(
            name, field1, reference1).classify_references([reference1])
        assert len(list(components)) == 0 and len(list(fields)) == 2

    def test_classify_fields(self):
        name = "Projects"
        field1 = FqlField("name", FqlTextDatatype)
        reference1 = FqlReference(
            "Employee", FqlManyRefcardinality, "Employees")
        fields, components = Form(name, field1, reference1).classify_fields()
        assert len(fields) == 2 and len(components) == 1

    def test_classify_fields2(self):
        name = "Projects"
        field1 = FqlField("name", FqlTextDatatype)
        reference1 = FqlReference(
            "Employee", FqlOneRefcardinality, "Employees")
        fields, components = Form(name, field1, reference1).classify_fields()
        assert len(fields) == 4 and len(components) == 0

    def test_sql_code(self):
        name = "Projects"
        field1 = FqlField("name", FqlTextDatatype)
        reference1 = FqlReference(
            "Employee", FqlOneRefcardinality, "Employees")
        form = Form(name, field1, reference1)
        assert form.sql_code() == "create table Projects(FQL_ID serial primary key,name varchar(511),Employee integer,foreign key(Employee) references Employees(FQL_ID));\n"

    def test_sql_code2(self):
        name = "Projects"
        field1 = FqlField("name", FqlTextDatatype)
        reference1 = FqlReference(
            "Employee", FqlManyRefcardinality, "Employees")
        form = Form(name, field1, reference1)
        code1 = "create table Projects(FQL_ID serial primary key,name varchar(511));"
        code2 = "create table Projects_Employees(FQL_ID serial primary key,fk_Projects integer,foreign key(fk_Projects) references Projects(FQL_ID),fk_Employees integer,foreign key(fk_Employees) references Employees(FQL_ID));"
        assert form.sql_code() == code1 + "\n" + code2
