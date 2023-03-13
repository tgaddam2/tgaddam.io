import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from styles import *

from pages.robotics import roboticsInfo

route = "education"
title = "Education"

archeryText = """I shoot compeition recurve, and have been doing it for 3 years now"""

offset = 23

def page():
    return pc.box(
        pc.box(
            pc.vstack(
                TopNavbar(),
                pc.heading(
                    "Education",
                    font_size="400%",
                    padding="10px",
                    style=h1Color,
                ),
                pc.heading(
                    "Academics",
                    font_size="275%",
                    padding="10px",
                    style=h1Color,
                ),
                pc.spacer(padding="0.1%"),
                pc.box(
                    pc.unordered_list(
                        pc.list_item("Orlando Science High School"),
                        pc.list_item("John Hopkins"),
                        pc.unordered_list(
                            pc.list_item("Explore Engineering Innovation"),
                            padding_left=f"{2.5}%",
                        ),
                        pc.list_item("Stanford"),
                        pc.unordered_list(
                            pc.list_item("ENGR 40M - An Introduction to Making: What is EE"),
                            pc.list_item("PHYSICS 16 - The Origin and Development of the Cosmos"),
                            padding_left=f"{2.5}%",
                        ),
                        color="#B0B0B0",
                        font_weight = "bold",
                    ),
                ),
                pc.box(
                    pc.heading(
                        "Extracurriculars",
                        font_size="275%",
                        padding="10px",
                        style=h1Color,
                    ),
                ),   
                pc.spacer(padding="0.1%"),
                pc.box(
                    pc.center(
                        pc.markdown("""<span style="color: #B0B0B0;">**Archery**</span>"""),
                    ),
                    pc.center(
                        pc.markdown("""<span style="color: #B0B0B0;">**FIRST Robotics**</span>"""),
                    ),
                    width=["80%", "90%", "90%", "50%"],
                ),
                pc.spacer(padding="10px",),
                pc.divider(color="#B0B0B0"),
                pc.box(
                    pc.heading(
                        "Archery",
                        font_size="200%",
                        padding="10px",                   
                        style=subHColor,
                    ),
                ),
                pc.box(
                    pc.center(
                        pc.text(
                            archeryText,
                            color="#B0B0B0",
                        ),
                    ),
                    width=["95%", "95%", "90%", "50%"],
                ),
                roboticsInfo(),
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