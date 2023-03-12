from pcconfig import config
import sys

sys.path.append("tgaddamSite/")

from comps import state
from pages import index, projects, about
import pynecone as pc

# Add state and page to the app.
app = pc.App(state=state.State)

pages = [index, projects, about]

for page in pages:
    app.add_page(
        page.page,
        route=page.route,)
app.compile()