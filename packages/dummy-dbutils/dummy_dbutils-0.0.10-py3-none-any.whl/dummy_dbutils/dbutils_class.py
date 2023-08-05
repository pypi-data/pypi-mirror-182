from collections import namedtuple

class DBUtilsSecrets:

    def get(self, **kwargs):
        # print("calling DBUtilsSecrets.get func from dummy dbutils package, and no operation performed.")
        pass

class DBUtilsWidgets:



    def __init__(self):
        self._format = namedtuple('format', 
                                    [
                                        'input_name',
                                        'input_value',
                                        'input_desc'
                                    ]
                                 )
        
        self._notebook_inputs = {}

    def removeAll(self):
        # print("calling DBUtilsWidgets.removeAll func from dummy dbutils package, and no operation performed.")
        self._notebook_inputs = {}
        pass

    def text(self, *args):
        curr_inputs = self._format(*args)
        self._notebook_inputs[curr_inputs.input_name] = curr_inputs
        # print("calling DBUtilsWidgets.text func from dummy dbutils package, and no operation performed.")
        pass

    def get(self, key):
        return self._notebook_inputs.get(key).input_value
        # print("calling DBUtilsWidgets.get func from dummy dbutils package, and no operation performed.")


class DButilsFunctions:

    def ls(self, dir: str):
        # print("calling DButilsFunctions.ls func from dummy dbutils package, and no operation performed.")
        pass

    def mkdirs(self, dir: str):
        # print("calling DButilsFunctions.mkdirs func from dummy dbutils package, and no operation performed.")
        pass

    def mv(self, src: str, tgt: str):
        # print("calling DButilsFunctions.mv func from dummy dbutils package, and no operation performed.")
        pass

    def mounts(self):
        return []

    def mount(self, **kwargs):
        pass 

class DBUtils:

    def __init__(self):
        self.fs = DButilsFunctions()
        self.widgets = DBUtilsWidgets()
        self.secrets = DBUtilsSecrets()

dbutils = DBUtils()
