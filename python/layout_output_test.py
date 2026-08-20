# ============================================================
# COUNTDOWN OS — LAYOUT OUTPUT TEST
# Version: 1.2 Elegance
# ============================================================

import json

from layout_engine import build_layout
from layout_output import write_layout, LAYOUT_FILE


EVENT = {
    "titleDisplay": "UNTIL ALEX",
    "daysDisplay": "48",
    "progressDisplay": "66%",
    "notesDisplay": "Comprar cacao",
    "destinationDisplay": "",
    "arrivalDisplay": "",
    "progress": 0.6571428571428571
}


def assert_key(data, key, label):

    assert key in data, (
        f"Missing {label}: {key}"
    )

    print(f"✓ {label}: {key}")


def main():

    print()
    print("=" * 52)
    print("       COUNTDOWN OS — LAYOUT OUTPUT TEST")
    print("=" * 52)


    # ========================================================
    # BUILD LAYOUT
    # ========================================================

    print()
    print("BUILD")
    print("-" * 52)

    layout = build_layout(EVENT)

    print("✓ Layout Engine generated layout")


    # ========================================================
    # WRITE JSON
    # ========================================================

    print()
    print("OUTPUT")
    print("-" * 52)

    write_layout(layout)

    print(f"Output: {LAYOUT_FILE}")


    # ========================================================
    # FILE
    # ========================================================

    assert LAYOUT_FILE.exists(), (
        "layout.json was not created."
    )

    print("✓ layout.json exists")


    # ========================================================
    # READ JSON
    # ========================================================

    with LAYOUT_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        saved_layout = json.load(file)

    print("✓ layout.json is valid JSON")


    # ========================================================
    # ROOT CONTRACT
    # ========================================================

    print()
    print("ROOT CONTRACT")
    print("-" * 52)

    assert saved_layout["version"] == "1.2"

    print(
        f"✓ version: "
        f"{saved_layout['version']}"
    )


    assert (
        saved_layout["system"]
        == "Countdown OS Layout System"
    )

    print(
        f"✓ system: "
        f"{saved_layout['system']}"
    )


    assert_key(
        saved_layout,
        "canvas",
        "root property"
    )

    assert_key(
        saved_layout,
        "components",
        "root property"
    )


    # ========================================================
    # CANVAS
    # ========================================================

    print()
    print("CANVAS")
    print("-" * 52)

    canvas = saved_layout["canvas"]

    assert canvas["width"] == 400
    assert canvas["height"] == 200
    assert canvas["anchor"] == "center"

    print(f"✓ Width:  {canvas['width']}")
    print(f"✓ Height: {canvas['height']}")
    print(f"✓ Anchor: {canvas['anchor']}")


    # ========================================================
    # COMPONENT CONTRACT
    # ========================================================

    print()
    print("COMPONENT CONTRACT")
    print("-" * 52)

    components = saved_layout["components"]

    required_components = [
        "Background",
        "Cover",
        "Header",
        "Gradient",
        "Counter",
        "Content",
        "Footer",
        "test"
    ]

    for component in required_components:

        assert_key(
            components,
            component,
            "component"
        )


    # ========================================================
    # BACKGROUND
    # ========================================================

    print()
    print("BACKGROUND")
    print("-" * 52)

    background = components["Background"]

    assert_key(
        background,
        "position",
        "Background property"
    )

    assert_key(
        background,
        "kwgt_position",
        "Background KWGT position"
    )

    assert_key(
        background["Background_shape"],
        "BackgroundShape",
        "Background shape"
    )

    shape = (
        background
        ["Background_shape"]
        ["BackgroundShape"]
    )

    assert shape["type"] == "rectangle"
    assert shape["width"] == 400
    assert shape["height"] == 200

    print("✓ BackgroundShape contract valid")


    # ========================================================
    # HEADER
    # ========================================================

    print()
    print("HEADER")
    print("-" * 52)

    header = components["Header"]

    title = header["Title"]
    days = header["Days"]

    assert_key(
        title,
        "position",
        "Title position"
    )

    assert_key(
        title,
        "kwgt_position",
        "Title KWGT position"
    )

    assert_key(
        title,
        "TitleText",
        "Title text"
    )

    assert title["TitleText"]["value"] == "UNTIL ALEX"

    assert title["TitleText"]["font_size"] == 18

    print("✓ Title contract valid")


    assert_key(
        days,
        "position",
        "Days position"
    )

    assert_key(
        days,
        "kwgt_position",
        "Days KWGT position"
    )

    assert days["DaysText"]["value"] == "days"

    assert days["DaysText"]["font_size"] == 15

    print("✓ Days contract valid")


    # ========================================================
    # COUNTER
    # ========================================================

    print()
    print("COUNTER")
    print("-" * 52)

    counter = components["Counter"]

    assert_key(
        counter,
        "position",
        "Counter position"
    )

    assert_key(
        counter,
        "kwgt_position",
        "Counter KWGT position"
    )

    days_remaining = counter["DaysRemaining"]

    assert_key(
        days_remaining,
        "position",
        "DaysRemaining position"
    )

    assert_key(
        days_remaining,
        "kwgt_position",
        "DaysRemaining KWGT position"
    )

    text = days_remaining["DaysRemainingText"]

    assert text["value"] == "48"
    assert text["font_size"] == 100

    print("✓ Counter contract valid")


    # ========================================================
    # JOURNEY
    # ========================================================

    print()
    print("JOURNEY")
    print("-" * 52)

    journey = (
        components
        ["Content"]
        ["journey"]
    )

    assert_key(
        journey,
        "position",
        "Journey position"
    )

    assert_key(
        journey,
        "kwgt_position",
        "Journey KWGT position"
    )

    print("✓ Journey contract valid")


    # ========================================================
    # LINE
    # ========================================================

    line = journey["Line"]

    assert_key(
        line,
        "position",
        "Line position"
    )

    assert_key(
        line,
        "kwgt_position",
        "Line KWGT position"
    )

    line_shape = line["JourneyLineShape"]

    assert line_shape["type"] == "rectangle"
    assert line_shape["width"] == 258
    assert line_shape["height"] == 1

    print("✓ JourneyLineShape contract valid")


    # ========================================================
    # ORIGIN
    # ========================================================

    origin = journey["Origin"]

    assert_key(
        origin,
        "position",
        "Origin position"
    )

    assert_key(
        origin,
        "kwgt_position",
        "Origin KWGT position"
    )

    origin_shape = origin["OriginShape"]

    assert origin_shape["type"] == "circle"
    assert origin_shape["size"] == 5

    print("✓ OriginShape contract valid")


    # ========================================================
    # PLANE
    # ========================================================

    print()
    print("PLANE")
    print("-" * 52)

    plane = journey["Plane"]

    assert_key(
        plane,
        "x_left",
        "Plane X left"
    )

    assert_key(
        plane,
        "x_right",
        "Plane X right"
    )

    assert_key(
        plane,
        "y",
        "Plane Y"
    )

    assert_key(
        plane,
        "kwgt_position",
        "Plane KWGT position"
    )

    assert plane["x_right"] == 275
    assert plane["y"] == 93

    expected_x_left = 520 * EVENT["progress"]

    assert abs(
        plane["x_left"] - expected_x_left
    ) < 0.000001

    plane_kwgt = plane["kwgt_position"]

    assert (
        plane_kwgt["x_left"]
        == plane["x_left"]
    )

    assert (
        plane_kwgt["x_right"]
        == plane["x_right"]
    )

    assert (
        plane_kwgt["y"]
        == plane["y"]
    )

    assert (
        plane["PlaneText"]["value"]
        == "✈"
    )

    assert (
        plane["PlaneText"]["font_size"]
        == 30
    )

    print(
        f"✓ Progress: {EVENT['progress']}"
    )

    print(
        f"✓ X Left: {plane['x_left']}"
    )

    print(
        f"✓ X Right: {plane['x_right']}"
    )

    print(
        f"✓ Y: {plane['y']}"
    )

    print("✓ Plane contract valid")


    # ========================================================
    # HEARTS
    # ========================================================

    print()
    print("HEARTS")
    print("-" * 52)

    hearts = journey["Hearts"]

    assert_key(
        hearts,
        "position",
        "Hearts position"
    )

    assert_key(
        hearts,
        "kwgt_position",
        "Hearts KWGT position"
    )


    destination = hearts["Destination"]

    assert_key(
        destination,
        "position",
        "Destination position"
    )

    assert destination["DestinationText"]["font_size"] == 14

    print("✓ Destination contract valid")


    arrival = hearts["Arrival"]

    assert_key(
        arrival,
        "position",
        "Arrival position"
    )

    assert arrival["ArrivalText"]["font_size"] == 14

    print("✓ Arrival contract valid")


    # ========================================================
    # FOOTER
    # ========================================================

    print()
    print("FOOTER")
    print("-" * 52)

    footer = components["Footer"]

    assert_key(
        footer,
        "position",
        "Footer position"
    )

    assert_key(
        footer,
        "kwgt_position",
        "Footer KWGT position"
    )

    assert footer["FooterText"]["font_size"] == 10
    assert footer["FooterText"]["value"] == "Comprar cacao"

    print("✓ Footer contract valid")


    # ========================================================
    # COVER
    # ========================================================

    print()
    print("COVER")
    print("-" * 52)

    cover = components["Cover"]

    assert_key(
        cover,
        "position",
        "Cover position"
    )

    assert_key(
        cover,
        "kwgt_position",
        "Cover KWGT position"
    )

    cover_text = (
        cover
        ["coverImage"]
        ["coverText"]
    )

    assert cover_text["font_size"] == 240
    assert cover_text["value"] == "♡"

    print("✓ Cover contract valid")


    # ========================================================
    # GRADIENT
    # ========================================================

    print()
    print("GRADIENT")
    print("-" * 52)

    gradient = components["Gradient"]

    vertical = gradient["Vertical"]
    horizontal = gradient["Horizontal"]

    assert_key(
        vertical,
        "kwgt_position",
        "Vertical gradient KWGT position"
    )

    assert_key(
        horizontal,
        "kwgt_position",
        "Horizontal gradient KWGT position"
    )

    print("✓ Vertical