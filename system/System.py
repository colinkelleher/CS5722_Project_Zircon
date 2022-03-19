class System:
    def __init__(self, system_id: int):
        self._system_id = system_id

    def __str__(self) -> str:
        return f"System has ID: {self._system_id}"
