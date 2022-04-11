class Item:
    _state = None

    def transition_to(self, state):
        if self._state is None:
            print(f"Item creation, state set to {type(state).__name__}")
        else:
            print(f"Item: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def use_action(self, comp):
        self._state.use_item(comp)

    def repair_action(self):
        self._state.repair_item()
