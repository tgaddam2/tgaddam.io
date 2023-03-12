import pynecone as pc

from .topNavbar import TopNavbar
from .constants import *

def page():
    return pc.box(
        pc.vstack(
            TopNavbar(),
            pc.text("Hello, world!"),
        ),
        style=background,
    )