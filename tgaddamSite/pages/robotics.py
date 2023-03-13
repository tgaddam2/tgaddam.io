import pynecone as pc
import sys

sys.path.append("Pynecone/")

from styles import *
from comps.imageClusters.cattlebotsCluster import cattleCluster

cattlebotsInfo = """I've been doing robotics for 2 years now. I am my team's captain as well as mechanical and electrical lead, 
and am also the coding co-lead. We've made it to top 4 in our league for both years we've existed as a team, and qualified to 
Florida states this year."""

clockworkinfo = """"""
baconInfo = """"""

offset = 23

def roboticsInfo():
    return pc.box(
        pc.box(
            pc.vstack(                
                pc.box(
                    pc.heading(
                        "FIRST Robotics",
                        font_size="200%",
                        padding="10px",                   
                        style=subHColor,
                    ),
                ),
                pc.box(
                    pc.heading(
                        "FTC 20344 - Cattlebots",
                        font_size="150%",
                        padding="10px",                   
                        style=subHColor,
                    ),
                ),
                pc.box(
                    pc.center(
                        pc.text(
                            pc.wrap(cattlebotsInfo),
                            color="#B0B0B0",
                        ),                        
                    ),
                    width=["95%", "95%", "90%", "50%"],
                ),
                cattleCluster(),
                pc.hstack(
                    pc.unordered_list(
                        pc.list_item("2021 - 2022 Freight Frenzy"),
                        pc.unordered_list(
                            pc.list_item("Tesla League Semifinalists Captain"),
                            pc.list_item("Tesla League Think Award"),
                            padding_left=f"{2.5}%",
                        ),
                        padding_left=f"{2.5}%",
                        color="#B0B0B0",
                    ),
                    pc.unordered_list(
                        pc.list_item("2022 - 2023 Powerplay"),
                        pc.unordered_list(
                            pc.list_item("Orlando Robotics League Finalists Captain"),
                            pc.list_item("Florida State Semifinalists 2nd Pick"),
                            padding_left=f"{2.5}%",
                        ),
                        padding_left=f"{2.5}%",
                        color="#B0B0B0",
                    ),
                ),
                pc.box(
                    pc.heading(
                        "FRC 4013 - Clockwork Mania",
                        font_size="150%",
                        padding="10px",                   
                        style=subHColor,
                    ),
                ),
                pc.box(
                    pc.center(
                        pc.text(
                            pc.wrap(clockworkinfo),
                            color="#B0B0B0",
                        ),
                    ),
                    width=["95%", "95%", "90%", "50%"],
                ),
                pc.box(
                    pc.heading(
                        "FRC 1902 - Exploding Bacon",
                        font_size="150%",
                        padding="10px",                   
                        style=subHColor,
                    ),
                ),
                pc.box(
                    pc.center(
                        pc.text(
                            pc.wrap(baconInfo),
                            color="#B0B0B0",
                        ),
                    ),
                    width=["95%", "95%", "90%", "50%"],
                ),
            ),
        ),
    )