import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from comps.constants import *

route = "about"
title = "About"

aboutIntroText = "Hey there! My name is Tarang Gaddam\n"
aboutText = """I live in Orlando, Florida in the US, speak English, some Telugu and can fully understand both languages.
When I game It's generally League of Legends on my PC, Eternal Evolution on my phone, and Titanfall 2 on my Xbox."""

def page():
    return pc.box(
        pc.box(
            pc.vstack(
                TopNavbar(),
                pc.box(
                    pc.heading(
                        "About Me",
                        font_size="400%",
                        padding="35px",
                        style=heading,
                    ),
                ),
                pc.box(
                    pc.center(
                        pc.text(
                            aboutIntroText,
                            font_size="130%",
                            color="#B0B0B0",
                            as_="b",
                        ),
                    ),
                    width=["95%", "95%", "90%", "auto"],
                ),                
                pc.spacer(),
                pc.box(
                    pc.center(
                        pc.text(
                            pc.wrap(aboutText),
                            font_size="110%",
                            color="#B0B0B0",
                        ),  
                    ),
                    pc.spacer(padding="0.2%"),
                    pc.center(
                        pc.vstack(
                            pc.unordered_list(
                                pc.list_item("Physics"),
                                pc.list_item("Cars"),
                                pc.list_item("Everything Tech"),
                                pc.unordered_list(
                                    pc.list_item("Computers"),
                                    pc.list_item("Smartphones"),
                                    pc.list_item("Coding"),
                                    pc.unordered_list(
                                        pc.list_item("Python"),
                                        padding_left="10%",
                                    ),
                                    padding_left="10%",
                                ),
                                color="#B0B0B0"
                            ),
                            font_weight = "bold",
                        ),
                        border_radius="15px",
                        border_color="#BABABA",
                        border_width="2px",
                    ),
                    width=["80%", "90%", "90%", "40%"],
                    border_radius="15px",
                    border_color="#BABABA",
                    border_width="2px",
                ),
            ),
            height="95%",
        ),
        pc.center(
            BotNavbar(),
        ),
        style=background,
    )