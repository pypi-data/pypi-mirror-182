
from fqllang.fql_stage.components.basic_components import FqlField, FqlForeignKey, FqlReference
from fqllang.fql_stage.components.create_form import Form
from fqllang.fql_stage.components.dataconstraints import FqlUniqueDataConstraint
from fqllang.fql_stage.components.datatypes import FqlTextDatatype
from fqllang.fql_stage.components.refcardinalities import FqlManyRefcardinality, FqlOneRefcardinality


class TestFqlField:
    def test_sql_code(self):
        name = "name"
        datatype = FqlTextDatatype
        dataconstraint1 = FqlUniqueDataConstraint
        field = FqlField(name, datatype, dataconstraint1)
        assert field.sql_code() == "name varchar(511) unique"
        
class TestFqlForeignKey:
    def test_sql_code(self):
        foreign = FqlForeignKey("Project", "Projects")
        assert foreign.sql_code() == "foreign key(Project) references Projects(FQL_ID)"
        
class TestFqlReference:
        
    def test_get_fields_empty(self):
        name = "Project"
        refcard = FqlManyRefcardinality
        refpath = "Projects"
        reference = FqlReference(name, refcard, refpath)
        assert len(reference.get_fields())==0
        
    def test_get_fields(self):
        name = "Project"
        refcard = FqlOneRefcardinality
        refpath = "Projects"
        reference = FqlReference(name, refcard, refpath)
        assert len(reference.get_fields())==2
        
    def test_get_extracomponent(self):
        name = "Project"
        refcard = FqlManyRefcardinality
        refpath = "Projects"
        component = FqlReference(name, refcard, refpath).get_extracomponent("Employees")
        assert isinstance(component, Form)
