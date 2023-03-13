# import pynecone as pc
# import sys

# sys.path.append("Pynecone/")

# from comps.topNavbar import TopNavbar
# from comps.botNavbar import BotNavbar
# from comps.constants import *

# route = "projects"

# projectText = """[Projects Here]"""

# def page():
#     return pc.box(
#         pc.vstack(
#             TopNavbar(),
            
#             pc.box(
#                 pc.heading(
#                     "Projects",
#                     # pc.spacer(),
#                     # style=heading,
#                     # font_size="5em",
#                 ),
#                 pc.spacer(),
#                 style=heading,
#                 font_size="5em",
#             ),
#             pc.box(
#                 pc.text(
#                     pc.wrap(projectText),
#                     color="#B0B0B0"
#                 )
#             )
#         ),
#         style=background,
#     )
    
import pynecone as pc
import sys

sys.path.append("Pynecone/")

from comps.topNavbar import TopNavbar
from comps.botNavbar import BotNavbar
from comps.constants import *

route = "projects"
title = "Projects"

projectText = """[Projects Here]"""

def page():
    return pc.box(
        pc.vstack(
            TopNavbar(),
            pc.spacer(),
            pc.box(
                pc.heading(
                    "Projects",
                    padding="35px",
                    style=heading,
                ),
            ),
            pc.spacer(),
            pc.box(
                pc.text(
                    pc.wrap(projectText),
                    color="#B0B0B0",
                ),
                border_radius="15px",
                border_color="#BABABA",
                border_width="2px",
                padding=5,
                width="95%"
            ),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            BotNavbar(),
            height="95%",
        ),
        style=background,
    )