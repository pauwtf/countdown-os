# ============================================================
# COUNTDOWN OS — LAYOUT CONTRACT TEST
# Version: 1.2 Elegance
# ============================================================

from layout_engine import build_layout
from layout_contract import (
    build_layout_contract
)


# ============================================================
# TEST DATA
# ============================================================

event = {
    "titleDisplay": "UNTIL ALEX",
    "daysDisplay": "48",
    "progressDisplay": "66%",
    "notesDisplay": "Comprar cacao",
    "progress": 0.6571428571428571
}


# ============================================================
# BUILD LAYOUT
# ============================================================

layout = build_layout(event)


# ============================================================
# BUILD CONTRACT
# ============================================================

contract = build_layout_contract(
    layout
)


layout_data = contract["layout"]

canvas = layout_data["canvas"]

components = layout_data["components"]


# ============================================================
# TEST HEADER
# ============================================================

print("")
print("==============================================")
print("       COUNTDOWN OS — LAYOUT CONTRACT TEST")
print("==============================================")


# ============================================================
# CANVAS
# ============================================================

print("")
print("CANVAS")
print("----------------------------------------------")

print(
    f"Width:  {canvas['width']}"
)

print(
    f"Height: {canvas['height']}"
)

print(
    f"Anchor: {canvas['anchor']}"
)


# ============================================================
# COMPONENT HIERARCHY
# ============================================================

print("")
print("COMPONENT HIERARCHY")
print("----------------------------------------------")

for component_name, component in components.items():

    print(
        f"✓ {component_name}"
    )

    for child_name in component:

        if isinstance(
            component[child_name],
            dict
        ):

            if child_name in (
                "position",
                "text",
                "font_size",
                "width",
                "height",
                "size",
                "x_left",
                "x_right",
                "y"
            ):
                continue

            print(
                f"  └── {child_name}"
            )


# ============================================================
# POSITION TEST
# ============================================================

print("")
print("POSITION VALIDATION")
print("----------------------------------------------")


def check_position(
    name,
    component
):

    if "position" not in component:
        print(
            f"• {name:<25} "
            f"NO POSITION"
        )
        return

    position = component["position"]

    print(
        f"• {name:<25}"
        f"X: {position['x']:<10}"
        f"Y: {position['y']}"
    )


check_position(
    "Header",
    components["header"]
)

check_position(
    "Header → Title",
    components["header"]["title"]
)

check_position(
    "Header → Days",
    components["header"]["days"]
)

check_position(
    "Counter",
    components["counter"]
)

check_position(
    "Counter → Days",
    components["counter"]["days"]
)

check_position(
    "Journey",
    components["journey"]
)

check_position(
    "Journey → Line",
    components["journey"]["line"]
)

check_position(
    "Journey → Origin",
    components["journey"]["origin"]
)

check_position(
    "Journey → Hearts",
    components["journey"]["hearts"]
)

check_position(
    "Footer",
    components["footer"]
)

check_position(
    "Cover",
    components["cover"]
)


# ============================================================
# PLANE TEST
# ============================================================

print("")
print("PLANE")
print("----------------------------------------------")

plane = components["journey"]["plane"]

print(
    f"X Left:  {plane['x_left']}"
)

print(
    f"X Right: {plane['x_right']}"
)

print(
    f"Y:       {plane['y']}"
)


# ============================================================
# REQUIRED STRUCTURE TEST
# ============================================================

assert "layout" in contract

assert "canvas" in contract["layout"]

assert "components" in contract["layout"]


assert "cover" in components

assert "header" in components

assert "counter" in components

assert "journey" in components

assert "footer" in components


assert "title" in components["header"]

assert "days" in components["header"]

assert "days" in components["counter"]

assert "line" in components["journey"]

assert "origin" in components["journey"]

assert "plane" in components["journey"]

assert "hearts" in components["journey"]


# ============================================================
# CANVAS TEST
# ============================================================

assert canvas["width"] == 400

assert canvas["height"] == 200

assert canvas["anchor"] == "center"


# ============================================================
# POSITION TEST
# ============================================================

assert components["header"]["title"]["position"] == {
    "x": 175.0,
    "y": -125.0
}


assert components["header"]["days"]["position"] == {
    "x": 50.0,
    "y": 21.0
}


assert components["counter"]["position"] == {
    "x": 195.0,
    "y": -20.0
}


assert components["journey"]["line"]["position"] == {
    "x": 20.0,
    "y": 100.0
}


assert components["journey"]["origin"]["position"] == {
    "x": 275.0,
    "y": 100.0
}


assert components["journey"]["hearts"]["position"] == {
    "x": -245.0,
    "y": 100.0
}


assert components["footer"]["position"] == {
    "x": 200.0,
    "y": -125.0
}


assert components["cover"]["position"] == {
    "x": -300.0,
    "y": 0.0
}


# ============================================================
# PLANE TEST
# ============================================================

assert plane["x_left"] == 341.7142857142857

assert plane["x_right"] == 275

assert plane["y"] == 93


# ============================================================
# SUCCESS
# ============================================================

print("")
print("==============================================")
print("             🟢 TEST PASSED")
print("==============================================")
print("")