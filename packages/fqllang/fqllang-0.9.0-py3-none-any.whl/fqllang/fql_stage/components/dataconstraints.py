from fqllang.sql_stage.components.dataconstraints import SqlDataconstraint, SqlNotnullDataconstraint, SqlPrimarykeyDataconstraint, SqlUniqueDataconstraint


class FqlDataconstraint:
    __type__ = "default"
    __sql__ = SqlDataconstraint


class FqlNotnullDataConstraint(FqlDataconstraint):
    __type__ = "not null"
    __sql__ = SqlNotnullDataconstraint


class FqlUniqueDataConstraint(FqlDataconstraint):
    __type__ = "unique"
    __sql__ = SqlUniqueDataconstraint


class FqlPrimarykeyDataConstraint(FqlDataconstraint):
    __type__ = "primary key"
    __sql__ = SqlPrimarykeyDataconstraint
