import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from styles import *

route = "about"
title = "About"

aboutIntroText = "Hey there! My name is Tarang Gaddam\n"
aboutText = """I live in Orlando, Florida in the US, speak English, some Telugu and can fully understand both languages.
When I game It's generally League of Legends on my PC, Eternal Evolution on my phone, and Titanfall 2 on my Xbox."""

hobbiesOffset = 10

def page():
    return pc.box(
        pc.box(
            pc.vstack(
                TopNavbar(),
                # about me
                pc.box(
                    pc.heading(
                        "About Me",
                        font_size="400%",
                        padding="10px",
                        style=h1Color,
                    ),
                ),
                pc.box(
                    pc.center(
                        pc.text(
                            aboutIntroText,
                            font_size="120%",
                            color="#B0B0B0",
                            as_="b",
                        ),
                    ),
                    width=["95%", "95%", "90%", "auto"],
                ),                
                pc.spacer(),
                pc.box(
                    pc.vstack(
                        pc.box(
                            pc.text(
                                pc.wrap(aboutText),
                                color="#B0B0B0",                        
                            ),
                            width=["80%", "90%", "90%", "50%"],
                        ),
                        pc.spacer(padding="0.1%"),
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
                                    padding_left=f"{2.5}%",
                                ),
                                padding_left=f"{2.5}%",
                            ),
                            padding_right=f"{hobbiesOffset}%",
                            color="#B0B0B0",
                            font_weight = "bold",
                        ),
                    )
                ),
                # quick info
                pc.box(
                    pc.heading(
                        "Quick Info",
                        font_size="350%",
                        padding="5px",
                        style=h1Color,
                    ),
                ),             
                pc.spacer(),
                pc.box(
                    pc.vstack(
                        pc.center(                            
                            pc.hstack(
                                pc.text(
                                    "My current time:",
                                    color="#B0B0B0",
                                ),
                                # https://www.timeanddate.com/clocks/free.html
                                pc.html("""<iframe src="https://free.timeanddate.com/clock/i8rdca8k/n867/fs17/fcb0b0b0/tct/pct/th2/ts1/ta1" frameborder="0" width="102" height="22" allowtransparency="true"></iframe>"""),
                            ),
                        ),
                        pc.text(
                            "My birthday: October 30, 2005",
                            color="#B0B0B0",
                        ),
                    ),
                    width=["80%", "90%", "90%", "50%"],
                ),
                # website info
                pc.box(
                    pc.heading(
                        "Website Info",
                        font_size="350%",
                        padding="5px",
                        style=h1Color,
                    ),
                ),             
                pc.spacer(),
                pc.box(
                    pc.vstack(                        
                        pc.hstack(
                            pc.text(
                                "Built with:",
                                color="#B0B0B0",
                            ),
                            pc.link(
                                pc.text(
                                    "Pynecone",
                                    color="#B0B0B0",
                                ),
                                href="https://pynecone.io",
                                is_external=True,
                            )
                        ),
                    ),
                    width=["80%", "90%", "90%", "50%"],
                ),
                
            ),
            height="95%",
        ),
        pc.center(
            BotNavbar(),
        ),
        style=background,
    )