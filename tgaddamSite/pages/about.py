import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from comps.constants import *

route = "about"

aboutText = """Hey there! My name is Tarang Gaddam and this is my personal website. As you can see I like to code and build 
robots."""

def page():
    return pc.box(
        pc.vstack(
            TopNavbar(),
            pc.center(
                pc.vstack(
                    pc.box(
                        pc.heading(
                            "About Me",
                            style=heading,
                            font_size="5em",
                        ),
                    ),
                    pc.box(
                        pc.text(
                            pc.wrap(aboutText),
                            color="#B0B0B0"
                        )
                    )
                )
            ),
        ),
        style=background,
    )