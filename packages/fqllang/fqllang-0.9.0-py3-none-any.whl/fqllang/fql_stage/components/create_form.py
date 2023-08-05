

from itertools import chain

import fqllang.fql_stage.components.basic_components as components
from fqllang.fql_stage.components.dataconstraints import FqlPrimarykeyDataConstraint
from fqllang.fql_stage.components.datatypes import FqlSerialDatatype
from fqllang.sql_stage.components.create_table import CreateTable


class Form:
    def __init__(self, name, *fields) -> None:
        self.name = name
        hidden_field = components.FqlField("FQL_ID", FqlSerialDatatype, FqlPrimarykeyDataConstraint)
        self.fields = [hidden_field, *fields]

    def sql_code(self):
        subfields, extracomponents = self.classify_fields()
        sqlsubfields = self.to_sql_subfields(subfields)
        result = CreateTable(self.name, *sqlsubfields).generate()
        result += self.generate_extracomponents(extracomponents)
        return result

    def classify_fields(self):
        subfields = filter(lambda field: isinstance(field, components.FqlField), self.fields)
        references = filter(lambda field: isinstance(field, components.FqlReference), self.fields)
        extrasubfields, extracomponents = self.classify_references(list(references))
        subfields = list(chain(subfields,extrasubfields))
        return subfields, extracomponents
    
    def classify_references(self, references):
        subfields = map(lambda reference: reference.get_fields(),references)
        components = map(lambda reference: reference.get_extracomponent(self.name), references)
        subfields = filter(lambda subfield: len(subfield)!=0,subfields)
        components = filter(lambda component: component is not None,components)
        subfields = chain(*subfields)
        return list(subfields), list(components)
    
    def to_sql_subfields(self, subfields):
        result = []
        for subfield in subfields:
            if isinstance(subfield, components.FqlField):
                result.append(subfield.to_sql_field())
            elif isinstance(subfield, components.FqlForeignKey):
                result.append(subfield.to_sql_reference())
        return result

    def generate_extracomponents(self, extracomponents):
        components = []
        for component in extracomponents:
            if isinstance(component, Form):
                subfields = self.to_sql_subfields(component.fields)
                components.append(CreateTable(component.name, *subfields))
        return "\n" + "\n".join(component.generate() for component in components)
