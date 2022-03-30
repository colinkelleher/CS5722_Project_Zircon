import tcod.event

from events import Events
from events.EventManager import InputManager
from events.Events import Event


def handle(event: Event):
    if type(event) not in HANDLERS.keys():
        return
    for handler in HANDLERS[type(event)]:
        handler(event)


def manage_input(event: tcod.event.KeyDown):
    input_manager = InputManager()
    input_manager.handle_input(event)


HANDLERS = {
    tcod.event.KeyDown: [manage_input],
    tcod.event.Undefined: [],
    tcod.event.WindowEvent: [],
}
