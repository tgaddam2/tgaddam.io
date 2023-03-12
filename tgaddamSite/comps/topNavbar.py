import pynecone as pc
from .state import State

def TopNavbar():
    return pc.hstack(        
        pc.link( # navigate home
            pc.hstack(
                pc.image(
                    src="favicon.ico",
                    width="30px",
                    height="auto",
                ),
                pc.button(
                    "tgaddam",
                    color_scheme="white", 
                    size="lg",
                    width="5em",
                    _hover={"box-shadow":"#D434A4 5px 5px, #000000 6px 6px, #E41581 10px 10px",},
                ),
            ),
            href="/",
            button="True",
        ),
        pc.spacer(),
        pc.hstack(
            pc.link( # navigate to projects page
                pc.button(
                    "Projects",
                    color_scheme="white",
                    size="lg",
                    width="4em",
                    _hover={"box-shadow":"#D434A4 5px 5px, #000000 6px 6px, #E41581 10px 10px",},),
                href="projects",
                button=True,
            ),
            pc.link( # navigate to about page
                pc.button(
                    "About",
                    color_scheme="white",
                    size="lg",
                    width="5em",
                    _hover={"box-shadow":"#D434A4 5px 5px, #000000 6px 6px, #E41581 10px 10px",},),
                href="about",
                button=True,
            ),
            pc.link( # navigate to gihub
                pc.image(
                    src="github-white.ico",
                    width="30px",
                    height="auto",),
                href="https://github.com/tgaddam2",
                is_external=True,
            ),
        ),
        width="98%",
    )