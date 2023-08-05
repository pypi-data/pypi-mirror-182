
from fqllang.fql_stage.ast_builders import FqlAstBuilder
from fqllang.sql_stage.code_transpilers.postgreTranspiler import FqlAstPostgreSqlTranspiler

def getSqlCode(fqlCode):
    fqlAstBuilder = FqlAstBuilder.fqlAstFromCode(fqlCode)
    model = fqlAstBuilder.model
    postgreTanspiler = FqlAstPostgreSqlTranspiler(model)
    return postgreTanspiler.generate()
class TestFqlAstPostgreSqlTranspiler:
    def test_fqlStatementTranspiler_createForm(self):
        fqlCode = "create form Person(name TEXT, age NUMBER, project references Projects)"
        result = getSqlCode(fqlCode).lower()
        assert result == "CREATE TABLE Person(FQL_ID SERIAL PRIMARY KEY,name VARCHAR(511),age INTEGER,project INTEGER,FOREIGN KEY(project) REFERENCES Projects(FQL_ID));\n".lower()

    def test_fqlStatementTranspiler_getCase(self):
        fqlCode = "get Person"
        result = getSqlCode(fqlCode).lower()
        assert result == "SELECT * FROM Person;".lower()

    def test_fqlStatementTranspiler_getCaseWithConditions(self):
        fqlCode = "get Person with name='Leandro' and age=20"
        result = getSqlCode(fqlCode).lower()
        assert result == "SELECT * FROM Person WHERE name='Leandro' and age=20;".lower()
        
    def test_fqlStatementTranspiler_createNew(self):
        fqlCode = "create Person (name='Leandro', age=23)"
        result = getSqlCode(fqlCode).lower()
        assert result == "INSERT INTO Person (name,age) VALUES ('Leandro',23);".lower()
