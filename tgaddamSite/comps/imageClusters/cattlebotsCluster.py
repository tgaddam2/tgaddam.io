import pynecone as pc
import sys

sys.path.append("Pynecone/")

def cattleCluster():
    return pc.box(
        pc.responsive_grid(
            pc.image(
                src="ftc/cattlebots1.png",
                box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                _hover={"filter": "brightness(105%)", "z_index": "97"},
                border_radius="4em",
                width="75%",
                position="relative",
                top="16%",
                left="40%",
            ),
            pc.image(
                src="ftc/cattlebots2.png",
                box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                _hover={"filter": "brightness(105%)", "z_index": "97"},
                border_radius="4em",
                width="95%",
                position="relative",
                top="1%",
            ),
            pc.image(
                src="ftc/cattlebots3.png",
                box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                _hover={"filter": "brightness(105%)", "z_index": "97"},
                border_radius="4em",
                width="75%",
                position="relative",
                top="14%",
                right="45%",
            ),
            pc.image(
                src="ftc/cattlebots4.png",
                box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                _hover={"filter": "brightness(105%)", "z_index": "97"},
                border_radius="4em",
                width="75%",
                position="relative",
                bottom="61%",
                left="70%",
            ),
            pc.image(
                src="ftc/cattlebots5.png",
                box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                _hover={"filter": "brightness(105%)", "z_index": "97"},
                border_radius="4em",
                width="95%",
                position="relative",
                bottom="33%",
            ),
            columns=[3],
            spacing="4",
            padding_left="10%",
            padding_right="10%",
            padding_top="2%",
        ),
        height="60vh",
        width="75%"
    )