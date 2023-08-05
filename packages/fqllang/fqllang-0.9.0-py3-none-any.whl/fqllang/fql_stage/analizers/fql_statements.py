

from fqllang.fql_stage.analizers.base import Analizer
from fqllang.fql_stage.analizers.create_form import CreateFormAnalizer
from fqllang.fql_stage.utils import getClassName


class ModelAnalizer(Analizer):
    def make_copy(self):
        className = getClassName(self.model)
        analizerDict = self.modelDict
        return analizerDict[className](self.model).make_copy()

    @property
    def modelDict(self):
        return {
            "CreateForm": CreateFormAnalizer
        }
