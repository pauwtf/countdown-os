# ============================================================
# COUNTDOWN OS — LAYOUT ENGINE TEST
# Version: 1.2 Elegance
# ============================================================

from layout_engine import build_layout


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
# BUILD
# ============================================================

layout = build_layout(event)

components = layout["components"]


# ============================================================
# HELPERS
# ============================================================

def position(component):
    return component["position"]


def print_position(label, component):
    pos = position(component)

    print(
        f"{label:<20}"
        f"X: {pos['x']:<10}"
        f"Y: {pos['y']}"
    )


# ============================================================
# TEST HEADER
# ============================================================

print("")
print("==============================================")
print("       COUNTDOWN OS — LAYOUT ENGINE TEST")
print("==============================================")

print("")
print("CANVAS")
print("----------------------------------------------")

print(
    f"Width:  {layout['canvas']['width']}"
)

print(
    f"Height: {layout['canvas']['height']}"
)

print(
    f"Anchor: {layout['canvas']['anchor']}"
)


# ============================================================
# HEADER
# ============================================================

print("")
print("HEADER")
print("----------------------------------------------")

print_position(
    "Title",
    components["header"]["title"]
)

print_position(
    "Days",
    components["header"]["days"]
)

print(
    f"Title text: "
    f"{components['header']['title']['text']}"
)

print(
    f"Days text: "
    f"{components['header']['days']['text']}"
)


# ============================================================
# COUNTER
# ============================================================

print("")
print("COUNTER")
print("----------------------------------------------")

print_position(
    "Counter",
    components["counter"]
)

print_position(
    "Days Remaining",
    components["counter"]["days"]
)

print(
    f"Value: "
    f"{components['counter']['days']['text']}"
)


# ============================================================
# JOURNEY
# ============================================================

journey = components["journey"]

print("")
print("JOURNEY")
print("----------------------------------------------")

print_position(
    "Journey",
    journey
)

print_position(
    "Line",
    journey["line"]
)

print(
    f"Line size: "
    f"{journey['line']['width']} × "
    f"{journey['line']['height']}"
)

print_position(
    "Origin",
    journey["origin"]
)

print(
    f"Origin size: "
    f"{journey['origin']['size']} × "
    f"{journey['origin']['size']}"
)


# ============================================================
# PLANE
# ============================================================

plane = journey["plane"]

print("")
print("PLANE")
print("----------------------------------------------")

print(
    f"Progress: "
    f"{event['progress']}"
)

print(
    f"X Left:   "
    f"{plane['x_left']}"
)

print(
    f"X Right:  "
    f"{plane['x_right']}"
)

print(
    f"Y:        "
    f"{plane['y']}"
)


# ============================================================
# HEARTS
# ============================================================

hearts = journey["hearts"]

print("")
print("HEARTS")
print("----------------------------------------------")

print_position(
    "Hearts",
    hearts
)

print_position(
    "Destination",
    hearts["destination"]
)

print_position(
    "Arrival",
    hearts["arrival"]
)


# ============================================================
# FOOTER
# ============================================================

print("")
print("FOOTER")
print("----------------------------------------------")

print_position(
    "Footer",
    components["footer"]
)

print(
    f"Text: "
    f"{components['footer']['text']}"
)


# ============================================================
# COVER
# ============================================================

print("")
print("COVER")
print("----------------------------------------------")

print_position(
    "Cover",
    components["cover"]
)


# ============================================================
# FINAL VALIDATION
# ============================================================

assert layout["canvas"]["width"] == 400
assert layout["canvas"]["height"] == 200

assert components["header"]["title"]["position"] == {
    "x": 175,
    "y": -125
}

assert components["counter"]["position"] == {
    "x": 195,
    "y": -20
}

assert journey["line"]["position"] == {
    "x": 20,
    "y": 100
}

assert journey["line"]["width"] == 258
assert journey["line"]["height"] == 1

assert journey["origin"]["position"] == {
    "x": 275,
    "y": 100
}

assert journey["origin"]["size"] == 5

assert journey["hearts"]["position"] == {
    "x": -245,
    "y": 100
}

assert components["footer"]["position"] == {
    "x": 200,
    "y": -125
}


# ============================================================
# SUCCESS
# ============================================================

print("")
print("==============================================")
print("             🟢 TEST PASSED")
print("==============================================")
print("")