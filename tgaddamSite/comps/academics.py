import pynecone as pc
import sys

sys.path.append("Pynecone/")

from styles import *

def academicsInfo():
    return pc.box(
        pc.box(
            pc.vstack(                
                pc.box(
                    pc.heading(
                        "Orlando Science High School",
                        font_size="150%",
                        padding="10px",                   
                        style=subHColor,
                    ),
                ),
                pc.box(
                    pc.heading(
                        "John Hopkins - Summer 2021",
                        font_size="150%",
                        padding="10px",                   
                        style=subHColor,
                    ),
                ),
                pc.unordered_list(
                    pc.list_item("Explore Engineering Innovation"),
                    padding_left=f"{2.5}%",
                    color="#B0B0B0",
                ),
                pc.box(
                    pc.heading(
                        "Stanford - Summer 2022",
                        font_size="150%",
                        padding="10px",                   
                        style=subHColor,
                    ),
                ),
                pc.unordered_list(
                    pc.list_item("ENGR 40M - An Introduction to Making: What is EE"),
                    pc.list_item("PHYSICS 16 - The Origin and Development of the Cosmos"),
                    padding_left=f"{2.5}%",
                    color="#B0B0B0",
                ),      
            ),
        ),
    )