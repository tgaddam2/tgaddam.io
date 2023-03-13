from pcconfig import config
import sys

sys.path.append("tgaddamSite/")

from comps import state
from pages import welcome, projects, about
import pynecone as pc

# Add state and page to the app.
app = pc.App(state=state.State)

pages = [welcome, projects, about]

for page in pages:
    app.add_page(
        page.page,
        route=page.route,
        title=page.title,
        image="Severum.ico")
app.compile()