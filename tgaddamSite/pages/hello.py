import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from styles import *

def page():
    return pc.box(
        pc.vstack(
            TopNavbar(),
            pc.text("Hello, world!"),
        ),
        style=background,
    )