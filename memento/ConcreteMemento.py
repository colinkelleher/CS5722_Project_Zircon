from datetime import datetime

from engine import Engine
from memento.Memento import Memento


class ConcreteMemento(Memento):
    def __init__(self, engine: Engine):
        self.global_state = {}
        for entity in engine.entities:
            print(entity)
            component_dic = {}
            for component in entity.components:
                state = component.save_state(component)
                component_dic[component.__class__] = state
            self.global_state[entity.__class__] = component_dic

        self._date = str(datetime.now())[:19]

    def get_state(self) -> {}:
        return self.global_state

    def get_name(self) -> str:
        return str(self._date)

    def get_date(self) -> str:
        return self._date
