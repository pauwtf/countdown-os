# ============================================================
# COUNTDOWN OS — LAYOUT CONTRACT TEST
# Version: 1.2 Elegance
# ============================================================

from layout_engine import build_layout
from layout_contract import (
    REQUIRED_HIERARCHY,
    validate_hierarchy
)


EVENT = {
    "titleDisplay": "UNTIL ALEX",
    "daysDisplay": "48",
    "progressDisplay": "66%",
    "notesDisplay": "Comprar cacao",
    "destinationDisplay": "",
    "arrivalDisplay": "",
    "progress": 0.6571428571428571
}


def main():

    print()
    print("=" * 50)
    print("       COUNTDOWN OS — LAYOUT CONTRACT TEST")
    print("=" * 50)

    layout = build_layout(EVENT)

    canvas = layout["canvas"]
    components = layout["components"]


    # ========================================================
    # CANVAS
    # ========================================================

    print()
    print("CANVAS")
    print("-" * 50)

    print(f"Width:  {canvas['width']}")
    print(f"Height: {canvas['height']}")
    print(f"Anchor: {canvas['anchor']}")

    assert canvas["width"] == 400
    assert canvas["height"] == 200
    assert canvas["anchor"] == "center"


    # ========================================================
    # COMPONENT HIERARCHY
    # ========================================================

    print()
    print("COMPONENT HIERARCHY")
    print("-" * 50)

    validate_hierarchy(
        components,
        REQUIRED_HIERARCHY
    )

    print("✓ Background")
    print("  └── Background_shape")
    print("      └── BackgroundShape")

    print("✓ Cover")
    print("  └── coverImage")
    print("      └── coverText")

    print("✓ Header")
    print("  ├── Title")
    print("  │   └── TitleText")
    print("  └── Days")
    print("      └── DaysText")

    print("✓ Gradient")
    print("  ├── Vertical")
    print("  │   └── GradientVerticalShape")
    print("  └── Horizontal")
    print("      └── GradientHorizontalShape")

    print("✓ Counter")
    print("  └── DaysRemaining")
    print("      └── DaysRemainingText")

    print("✓ Content")
    print("  └── journey")
    print("      ├── Line")
    print("      │   └── JourneyLineShape")
    print("      ├── Origin")
    print("      │   └── OriginShape")
    print("      ├── Plane")
    print("      │   └── PlaneText")
    print("      └── Hearts")
    print("          ├── Destination")
    print("          │   └── DestinationText")
    print("          └── Arrival")
    print("              └── ArrivalText")

    print("✓ Footer")
    print("  └── FooterText")

    print("✓ test")
    print("  └── TestText")


    # ========================================================
    # POSITION VALIDATION
    # ========================================================

    print()
    print("POSITION VALIDATION")
    print("-" * 50)


    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    header = components["Header"]

    title = header["Title"]
    days = header["Days"]

    print(
        f"• Header → Title       "
        f"X: {title['position']['x']} "
        f"Y: {title['position']['y']}"
    )

    print(
        f"• Header → Days        "
        f"X: {days['position']['x']} "
        f"Y: {days['position']['y']}"
    )

    assert title["position"]["x"] == 175
    assert title["position"]["y"] == -125

    assert days["position"]["x"] == 50
    assert days["position"]["y"] == 21


    # --------------------------------------------------------
    # COUNTER
    # --------------------------------------------------------

    counter = components["Counter"]

    print(
        f"• Counter              "
        f"X: {counter['position']['x']} "
        f"Y: {counter['position']['y']}"
    )

    assert counter["position"]["x"] == 195
    assert counter["position"]["y"] == -20


    # ========================================================
    # KWGT POSITION VALIDATION
    # ========================================================

    print()
    print("KWGT POSITION VALIDATION")
    print("-" * 50)


    # --------------------------------------------------------
    # COUNTER → KWGT
    # --------------------------------------------------------

    counter_kwgt = counter["kwgt_position"]

   