import pynecone as pc

startPad = "10px"

baseStyle = {
    "::selection": {
        "backgroundImage":"linear-gradient(to top, #1d3c42, #1e2d37, #1e1e26, #161216, #000000)",
        "width":"100vw",
        "height":"100vh"
    },
    pc.Text: {
        "font_family": "Inter",
        "font_size": 16,
    },
}

background = {
        # "background":"linear-gradient(315deg, #000000 50%, #FFFFFF 50%)",
        # "background":"linear-gradient(315deg, #020202 2.4%, #0B0B0B 4.9%, #121212 7.3%, #181818 9.8%, #1D1D1D 12.2%, #222222 14.6%, #272727 17.1%, #2D2D2D 19.5%, #323232 22.0%, #383838 24.4%, #3E3E3E 26.8%, #434343 29.3%, #494949 31.7%, #4F4F4F 34.1%, #555555 36.6%, #5B5B5B 39.0%, #626262 41.5%, #686868 43.9%, #6E6E6E 46.3%, #747474 48.8%, #7B7B7B 51.2%, #818181 53.7%, #888888 56.1%, #8E8E8E 58.5%, #959595 61.0%, #9C9C9C 63.4%, #A3A3A3 65.9%, #A9A9A9 68.3%, #B0B0B0 70.7%, #B7B7B7 73.2%, #BEBEBE 75.6%, #C5C5C5 78.0%, #CCCCCC 80.5%, #D3D3D3 82.9%, #DBDBDB 85.4%, #E2E2E2 87.8%, #E9E9E9 90.2%, #F0F0F0 92.7%, #F8F8F8 95.1%, #FFFFFF 97.6%)",
        # "background":"linear-gradient(135deg, #FFFFFF 0%, #000000 100%)",
        # "background": "radial-gradient(circle, #325056, #2d3b45, #272730, #1a171a, #000000)",
        "backgroundImage":"linear-gradient(to top, #1d3c42, #1e2d37, #1e1e26, #161216, #000000)",
        "width":"100vw",
        "height":"100vh"}

h1Color = {
        # "background_image":"linear-gradient(88.32deg, #526584 35%, #5D225C 65%, #D434A4 90%, #E41581 95%)",
        # "background_image":"radial-gradient(circle, #d434a4, #bc3298, #a42f8b, #8e2c7d, #78286f, #6d3071, #633671, #593b6f, #574b7a, #575982, #5b6688, #63738c)",
        # "background_image":"radial-gradient(circle, #b0388c, #9f3484, #8f307b, #7f2c72, #702869, #68306c, #60366e, #593b6f, #574b7a, #575982, #5b6688, #63738c)",
        # "background_image":"radial-gradient(circle, #b0388c, #93529d, #7763a1, #656d9a, #63738c)",
        "backgroundImage":"linear-gradient(to right, #cd2a9c, #a73ca7, #7d47a9, #514ca4, #1b4c97)",
        "background_clip":"text",
}

subHColor = {
        "color":"#B0B0B0",
}

hoverSize = 2
navbar = {      
        "size":"lg",
        "_hover":{"boxShadow":f"#D434A4 {hoverSize}px {hoverSize}px, #000000 {hoverSize + 1}px {hoverSize + 1}px, #E41581 {hoverSize * 2 + 1}px {hoverSize * 2 + 1}px",},
}