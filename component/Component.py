from abc import ABC


class Component(ABC):
    def save_state(self):
        return vars(self).copy()  # getting a copy of all the attributes

    def __update_attr__(self, dict):  # update all attributes using a dict
        self.__dict__.update(dict)
