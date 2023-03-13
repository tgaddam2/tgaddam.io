from pcconfig import config
import pynecone as pc

import sys
sys.path.append("tgaddamSite/")

from comps import state
from styles import *
from pages import welcome, projects, about, education

# Add state and page to the app.
app = pc.App(state=state.State,
             style=baseStyle)

pages = [welcome, projects, about, education]

for page in pages:
    app.add_page(
        page.page,
        route=page.route,
        title=page.title,
        image="Severum.ico")
app.compile()