from component.Component import Component


class HpComponent(Component):
    def __init__(self, hp_value: int = 50):
        self._hp_value = hp_value

    def get_hp(self) -> int:
        return self._hp_value

    def set_hp(self, hp_value: int):
        self._hp_value = hp_value

    def decrease_hp(self, hp_diff: int):
        self._hp_value -= hp_diff

    def increase_hp(self, hp_diff: int):
        self._hp_value += hp_diff
