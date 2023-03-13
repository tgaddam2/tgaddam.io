import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from comps.constants import *

route = "index"
title = "Home"

welcomeText = """Welcome to my personal website! Here, you'll find a collection of my latest projects, 
ideas, and other random stuff I'm working on. I created this website as a way to share my passions 
with others and to connect with like-minded individuals. Whether you're interested in coding, graphic 
design, or just curious about what I'm up to, I hope you find something here that inspires you. I'm 
always looking for feedback and collaboration, so don't hesitate to reach out if you have any 
questions or want to work on a project together. Thank you for visiting and I hope you enjoy 
exploring my site!"""

def page():
    return pc.box(
        pc.box(
            pc.vstack(
                TopNavbar(),
                pc.box(
                    pc.heading(
                        "Welcome",
                        font_size="600%",
                        style=heading,
                    ),
                ),
                pc.box(
                    pc.heading(
                        "This is tgaddam's website, go and explore the place",
                        font_size="200%",
                        color="#B0B0B0",
                    ),
                ),
                pc.spacer(),
                pc.box(
                    pc.text(
                        pc.wrap(welcomeText),
                        color="#B0B0B0",
                    ),
                    border_radius="15px",
                    border_color="#BABABA",
                    border_width="2px",
                    padding=5,
                    width="95%"
                ),
            ),
            height="95%",
        ),
        pc.center(
            BotNavbar(),
        ),
        style=background,
    )