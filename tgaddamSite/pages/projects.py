from datetime import datetime

import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from styles import *

route = "projects"
title = "Projects"

projectText = "[Projects]"

start = datetime.strptime("15/9/2022", "%d/%m/%Y")
current = datetime.strptime(datetime.now().strftime("%d/%m/%Y"), "%d/%m/%Y")

delta = current - start

diffyWorkTime = f"""Time Spent: {delta.days} days"""

diffyinfo = """A differential swerve drive consists of multiple drive modules each driven by two motors. By 
controlling the speed and direction of each motor, the wheel can simultaneously rotate and move 
in any direction. This allows for incredible manuverability, which enables any robot designed around 
it to be very capable"""

def page():
    return pc.box(
        pc.box(
            pc.vstack(
                TopNavbar(),
                pc.spacer(padding=f"{startPad}"),
                pc.box(
                    pc.heading(
                        "Projects",
                        font_size="400%",
                        padding="10px",
                        style=h1Color,
                    ),
                ),
                pc.heading(
                    "This Website",
                    font_size="275%",
                    padding="10px",
                    style=h1Color,
                ),
                pc.box(
                    pc.center(
                            pc.link(
                            pc.text(
                                "Source Code",
                                color="#B0B0B0",
                            ),
                            href="https://github.com/tgaddam2/tgaddam.io",
                            is_external=True,
                        ),
                    ),
                    width=["80%", "90%", "90%", "50%"],
                ),
                pc.heading(
                    "Differential Swerve Drive",
                    font_size="275%",
                    padding="10px",
                    style=h1Color,
                ),
                pc.box(
                    pc.center(
                        pc.text(
                            pc.wrap(diffyinfo),
                            color="#B0B0B0",
                        ),
                    ),
                    width=["95%", "95%", "90%", "50%"],
                ),
                pc.box(
                    pc.center(
                        pc.text(
                            "\n" + diffyWorkTime,
                            color="#B0B0B0",
                        ),
                    ),
                    width=["95%", "95%", "90%", "50%"],
                ),
            ),
            height="95%",
        ),
        pc.center(
            BotNavbar(),
        ),
        style=background,
    )