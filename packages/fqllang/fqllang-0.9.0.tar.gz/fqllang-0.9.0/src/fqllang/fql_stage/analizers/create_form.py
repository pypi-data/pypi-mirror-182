

from fqllang.fql_stage.analizers.base import Analizer
from fqllang.fql_stage.components.create_form import Form
from fqllang.fql_stage.components.dataconstraints import FqlNotnullDataConstraint, FqlUniqueDataConstraint
from fqllang.fql_stage.components.datatypes import FqlBooleanDatatype, FqlNumberDatatype, FqlTextDatatype
from fqllang.fql_stage.components.refcardinalities import FqlManyRefcardinality, FqlOneRefcardinality
from fqllang.fql_stage.utils import getClassName
from fqllang.fql_stage.components.basic_components import FqlField, FqlReference, RefCardinality, RefConstraint, SimpleId, DataPath, All, DataLabelList, DataLabel



class CreateFormAnalizer(Analizer):
    def make_copy(self):
        return Form(self.form_name, *self.data_specs)

    @property
    def data_specs(self):
        return DataSpecListAnalizer(self.model.dataSpecList).make_copy()

    @property
    def form_name(self):
        return self.model.formName


class DataSpecListAnalizer(Analizer):
    def make_copy(self):
        return self.data_specs

    @property
    def data_specs(self):
        return [self._analize_dataSpec(dataSpec) for dataSpec in self]

    def _analize_dataSpec(self, dataSpec):
        return DataSpecAnalizer(dataSpec).make_copy()

    def __iter__(self):
        yield from self.model


class DataSpecAnalizer(Analizer):
    def make_copy(self):
        className = getClassName(self.model)
        analizer = self.dataSpecDict
        return analizer[className](self.model).make_copy()

    @property
    def dataSpecDict(self):
        return {
            "DataDefinition": DataDefinitionAnalizer,
            "DataReference": DataReferenceAnalizer
        }


class DataDefinitionAnalizer(Analizer):
    def make_copy(self):
        return FqlField(self.data_name, self.data_type, *self.dataconstraints)

    @property
    def data_name(self):
        return self.model.dataName

    @property
    def data_type(self):
        def avaliable_datatypes():
            return {
                "NUMBER": FqlNumberDatatype,
                "TEXT": FqlTextDatatype,
                "BOOLEAN":FqlBooleanDatatype
            }
        datatype = self.model.dataType
        return avaliable_datatypes()[datatype]
    
    @property
    def dataconstraints(self):
        dataconstraints = []
        if self.not_null: dataconstraints.append(FqlNotnullDataConstraint)
        if self.unique: dataconstraints.append(FqlUniqueDataConstraint)
        return dataconstraints

    @property
    def not_null(self):
        return self.model.notNull

    @property
    def unique(self):
        return self.model.unique


class DataReferenceAnalizer(Analizer):
    def make_copy(self):
        # return FqlReference(self.data_name, self.ref_cardinality, self.ref_path, self.ref_constraint)
        return FqlReference(self.data_name, self.ref_cardinality, self.ref_path)

    @property
    def data_name(self):
        return self.model.dataName

    @property
    def ref_cardinality(self):
        return RefCardinalityAnalizer(self.model.refCardinality).make_copy()

    @property
    def ref_path(self):
        return RefPathAnalizer(self.model.refPath).make_copy()

    # @property
    # def ref_constraint(self):
    #     return RefConstraintAnalizer(self.model.refConstraint).make_copy()


class RefCardinalityAnalizer(Analizer):

    def make_copy(self):
        if self.model is None: return FqlOneRefcardinality
        if self.card2 is None: return FqlOneRefcardinality
        if self.card2 == "many": return FqlManyRefcardinality
        return FqlOneRefcardinality

    @property
    def card1(self):
        return self.model.cardinality1

    @property
    def card2(self):
        return self.model.cardinality2


class RefPathAnalizer(Analizer):
    def make_copy(self):
        className = getClassName(self.model)
        analizer = self.refPathDict
        return analizer[className](self.model).make_copy()

    @property
    def refPathDict(self):
        return {
            # "IdDotDataPath": IdDotDataPathAnalizer,
            "str": SimpleIdAnalizer
        }


class SimpleIdAnalizer(Analizer):
    def make_copy(self):
        return SimpleId(self.model)


# class IdDotDataPathAnalizer(Analizer):
#     def make_copy(self):
#         return DataPath(*self.full_datapath)

#     @property
#     def full_datapath(self):
#         return [*self]

#     @property
#     def id(self):
#         return self.model.id

#     @property
#     def data_path(self):
#         return DataPathAnalizer(self.model.dataPath).make_copy()

#     def __iter__(self):
#         yield self.id
#         data_path = self.data_path
#         if isinstance(data_path, list):
#             yield from data_path
#         else:
#             yield data_path


# class DataPathAnalizer(Analizer):
#     def make_copy(self):
#         className = getClassName(self.model)
#         analizer = self.dataPathDict
#         return analizer[className](self.model).make_copy()

#     @property
#     def dataPathDict(self):
#         return {
#             "IdDotDataPath": IdDotDataPathAnalizer,
#             "DataLabelList": DataLabelListAnalizer,
#             "All": StarAnalizer,
#             "str": SimpleIdAnalizer
#         }


# class DataLabelListAnalizer(Analizer):
#     def make_copy(self):
#         return DataLabelList(*self.data_labels)

#     @property
#     def data_labels(self):
#         return [self._analize_dataLabel(dataLabel) for dataLabel in self]

#     def __iter__(self):
#         yield from self.model.dataLabelList

#     def _analize_dataLabel(self, dataLabel):
#         return DataLabelAnalizer(dataLabel).make_copy()


# class DataLabelAnalizer(Analizer):
#     def make_copy(self):
#         return DataLabel(self.model)


# class StarAnalizer(Analizer):
#     def make_copy(self):
#         return All(self.model)


# class RefConstraintAnalizer(Analizer):
#     def make_copy(self):
#         return RefConstraint(self.model)
