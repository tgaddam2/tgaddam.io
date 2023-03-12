import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from comps.constants import *

route = "projects"

projectText = """[Projects Here]"""

def page():
    return pc.box(
        pc.vstack(
            TopNavbar(),
            pc.center(
                pc.vstack(
                    pc.box(
                        pc.heading(
                            "Projects",
                            # pc.spacer(),
                            # style=heading,
                            # font_size="5em",
                        ),
                        pc.spacer(),
                        style=heading,
                        font_size="5em",
                    ),
                    pc.box(
                        pc.text(
                            pc.wrap(projectText),
                            color="#B0B0B0"
                        )
                    )
                )
            ),
        ),
        style=background,
    )