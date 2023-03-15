import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.state import State
from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from styles import *

from comps.robotics import roboticsInfo
from comps.academics import academicsInfo

route = "contact"
title = "Contact Me"

archeryText = """I shoot compeition recurve, and have been doing it for 3 years now"""

class contact(State):
    firstName: str = ""
    lastName: str = ""
    email: str = ""
    body: str = ""

def page():
    return pc.box(
        pc.box(
            pc.vstack(
                TopNavbar(),
                pc.spacer(padding=f"{startPad}"),
                pc.heading(
                    "Contact Me",
                    font_size="400%",
                    padding="10px",
                    style=h1Color,
                ),
                
            ),
            height="97%",
        ),
        pc.center(
            BotNavbar(),
        ),
        height="230vh",
        width="99vw",
        style=background,
    )