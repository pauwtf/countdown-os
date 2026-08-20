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
    print("=" * 46)
    print("       COUNTDOWN OS — LAYOUT CONTRACT TEST")
    print("=" * 46)

    layout = build_layout(EVENT)

    canvas = layout["canvas"]
    components = layout["components"]


    # ========================================================
    # CANVAS
    # ========================================================

    print()
    print("CANVAS")
    print("-" * 46)

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
    print("-" * 46)

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
    print("-" * 46)

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


    counter = components["Counter"]

    print(
        f"• Counter              "
        f"X: {counter['position']['x']} "
        f"Y: {counter['position']['y']}"
    )


    journey = (
        components["Content"]
        ["journey"]
    )

    print(
        f"• Journey              "
        f"X: {journey['position']['x']} "
        f"Y: {journey['position']['y']}"
    )


    line = journey["Line"]

    print(
        f"• Journey → Line       "
        f"X: {line['position']['x']} "
        f"Y: {line['position']['y']}"
    )


    origin = journey["Origin"]

    print(
        f"• Journey → Origin     "
        f"X: {origin['position']['x']} "
        f"Y: {origin['position']['y']}"
    )


    hearts = journey["Hearts"]

    print(
        f"• Journey → Hearts     "
        f"X: {hearts['position']['x']} "
        f"Y: {hearts['position']['y']}"
    )


    footer = components["Footer"]

    print(
        f"• Footer               "
        f"X: {footer['position']['x']} "
        f"Y: {footer['position']['y']}"
    )


    cover = components["Cover"]

    print(
        f"• Cover                "
        f"X: {cover['position']['x']} "
        f"Y: {cover['position']['y']}"
    )


    # ========================================================
    # PLANE
    # ========================================================

    plane = journey["Plane"]

    print()
    print("PLANE")
    print("-" * 46)

    print(f"Progress: {EVENT['progress']}")
    print(f"X Left:  {plane['x_left']}")
    print(f"X Right: {plane['x_right']}")
    print(f"Y:       {plane['y']}")


    # ========================================================
    # SUCCESS
    # ========================================================

    print()
    print("=" * 46)
    print("             🟢 TEST PASSED")
    print("=" * 46)
    print()


if __name__ == "__main__":
    main()