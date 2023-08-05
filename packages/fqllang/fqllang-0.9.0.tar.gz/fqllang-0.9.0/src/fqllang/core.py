from fqllang.fql_stage.ast_builders import FqlAstBuilder
from fqllang.fql_stage.utils import getGrammar
from fqllang.sql_stage.code_transpilers.postgreTranspiler import FqlAstPostgreSqlTranspiler

GRAMMAR = getGrammar()


def getPostgreCodeFromFqlCode(fqlCode):
    try:
        fqlAstBuilder = FqlAstBuilder.fqlAstFromCode(fqlCode)
        postgreCode = FqlAstPostgreSqlTranspiler(fqlAstBuilder.model)
        return str(postgreCode).strip()
    except:
        raise Exception("Bad Fql Code")


if __name__ == "__main__":
    postgreCode = getPostgreCodeFromFqlCode("get Person with age=5 and name='Leandro'")
    print(postgreCode)
    postgreCode = getPostgreCodeFromFqlCode("get Person with age=5")
    print(postgreCode)
    postgreCode = getPostgreCodeFromFqlCode("get Person")
    print(postgreCode)
    postgreCode = getPostgreCodeFromFqlCode("create form Projects(title TEXT not null)")
    print(postgreCode)
    postgreCode = getPostgreCodeFromFqlCode("create form Employees(name TEXT, Project references 1..many Projects)")
    print(postgreCode)
    postgreCode = getPostgreCodeFromFqlCode("create form Person(name TEXT, Project references Projects)")
    print(postgreCode)
    postgreCode = getPostgreCodeFromFqlCode("create form Person(name TEXT, Project references 1 Projects)")
    print(postgreCode)
    postgreCode = getPostgreCodeFromFqlCode("create form Person(name TEXT, Project references 0..1 Projects)")
    print(postgreCode)
    postgreCode = getPostgreCodeFromFqlCode("create Project (name='Leandro', age=25)")
    print(postgreCode)
    
