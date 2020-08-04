from fitsnap3.io.sections.sections import Section
from fitsnap3.parallel_tools import pt


class Extras(Section):

    def __init__(self, name, config, args):
        super().__init__(name, config, args)
        self.knn = self.get_value("EXTRAS", "knn", "0", "bool")
        self.neighbors = self.get_value("EXTRAS", "neighbors", "2", "int")
        self.knnstyle = self.get_value("EXTRAS", "knnstyle", "balltree", "str")
        self.knnbins = self.get_value("EXTRAS", "knnbins", "100", "int")
        self.delete()
