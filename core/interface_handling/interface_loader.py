import importlib
import inspect
import csv


class InterfaceLoader:
    def __init__(self, root_dir, interface_root):
        self.root_dir = root_dir
        self.interface_root = interface_root

    def write_interface_data(self):     # TODO csv write func
        pass

    def get_interface_data(self):
        interface_data = list()

        with open(self.root_dir + "/game_interfaces.csv") as csv_file:
            reader = csv.reader(csv_file)

            for i, row in enumerate(reader):
                if i == 0:
                    continue
                interface_data.append(row)
        return interface_data

    def load(self):
        if_instances = dict()
        if_data = self.get_interface_data()

        for interface in if_data:   # interface = [name/dir,file]
            class_obj = None
            imported = importlib.import_module(self.interface_root + "." + interface[0] + "." + interface[1])

            for ckey, cval in inspect.getmembers(imported, inspect.isclass):
                for fkey, fval in inspect.getmembers(cval, inspect.isfunction):

                    if ckey != "RepoHandler" and fkey == "_load_games":     # just checking for one function thats unlikly to exist in dependency
                        class_obj = cval
                        break

            if class_obj is not None:
                instance = class_obj(interface[0])
                if_instances.update({interface[0]: instance})

        return if_instances
