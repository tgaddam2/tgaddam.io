import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.state import State
from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from styles import *

route = "entrybox"
title = "Entry box"

class entryState(State):
    textStr: str = "hello"

def page():
    return pc.box(
        pc.vstack(
            TopNavbar(),
            pc.center(
                pc.vstack(
                    pc.text(entryState.textStr),
                    pc.input(placeholder="Enter text",
                            on_blur=entryState.set_textStr),
                )
            )
        ),
        style=background,
    )