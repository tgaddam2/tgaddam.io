import pynecone as pc

import sys

sys.path.append("Pynecone/")

from .state import State
from styles import *

def TopNavbar():
    return pc.hstack(        
        pc.link( # navigate home
            pc.hstack(
                pc.image(
                    src="Severum.ico",
                    width="30px",
                    height="auto",
                ),
                pc.button(
                    "tgaddam",
                    color_scheme="white",
                    # width="5em",
                    # font_size="175%",
                    style=navbar
                ),
            ),
            href="/",
        ),
        pc.spacer(),
        pc.hstack(
            pc.link( # navigate to projects page
                pc.button(
                        "Projects",
                        color_scheme="white",
                        # width="4em",
                        # font_size="175%",
                        style=navbar,
                    ),
                href="projects",
                button=True,
            ),
            pc.link( # navigate to about page
                pc.button(
                        "About",
                        color_scheme="white",
                        # font_size="175%",
                        # width="5em",
                        style=navbar,
                    ),
                href="about",
                button=True,
            ),
            pc.link( # navigate to about page
                pc.button(
                        "Education",
                        color_scheme="white",
                        # font_size="175%",
                        # width="5em",
                        style=navbar,
                    ),
                href="education",
                button=True,
            ),
            pc.link( # navigate to gihub
                pc.image(
                        src="github-white.ico",
                        width="30px",
                        height="auto",
                    ),
                href="https://github.com/tgaddam2",
                is_external=True,
            ),
        ),
        width="98%",
        top="0px",
        position="sticky",
        backdrop_filter="blur(4px)",
        z_index="99",
    )