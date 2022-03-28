from datetime import datetime

from memento.Memento import Memento


class ConcreteMemento(Memento):
    def __init__(self, entities):
        self._global_state = {}
        for entity in entities:
            entity_id = entity.id
            component_dic = {}
            for component in entity.components.values():
                state = component.save_state()
                component_type = type(component)
                component_dic[component_type] = state
            self._global_state[entity_id] = component_dic

        self._date = str(datetime.now())[:19]

    def get_state(self) -> {}:
        return self._global_state

    def get_name(self) -> str:
        return f"{self._date} / ({self._global_state}...)"

    def get_date(self) -> str:
        return self._date
