import pynecone as pc
from .state import State

def BotNavbar():
    return pc.hstack(
        pc.center(
            pc.link( # navigate to gihub
                pc.image(
                    src="discordcl.ico",
                    width="30px",
                    height="auto",),
                href="https://discordapp.com/users/460131360603111424",
                is_external=True,
            ),
        ),
    )