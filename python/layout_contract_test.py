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


    # --------------------------------------------------------
    # COUNTER → KWGT POSITION
    # --------------------------------------------------------

    print()
    print("KWGT POSITION VALIDATION")
    print("-" * 50)

    counter_kwgt = counter["kwgt_position"]

    print(
        f"• Counter → X Right    "
        f"{counter_kwgt['x_right']}"
    )

    print(
        f"• Counter → X Left     "
        f"{counter_kwgt['x_left']}"
    )

    print(
        f"• Counter → Y Down     "
        f"{counter_kwgt['y_down']}"
    )

    print(
        f"• Counter → Y Up       "
        f"{counter_kwgt['y_up']}"
    )

    assert counter_kwgt["x_right"] == 195
    assert counter_kwgt["x_left"] == 0

    assert counter_kwgt["y_down"] == 0
    assert counter_kwgt["y_up"] == 20


    # --------------------------------------------------------
    # JOURNEY
    # --------------------------------------------------------

    journey = (
        components["Content"]
        ["journey"]
    )

    print(
        f"• Journey              "
        f"X: {journey['position']['x']} "
        f"Y: {journey['position']['y']}"
    )

    assert journey["position"]["x"] == 0
    assert journey["position"]["y"] == 0


    # --------------------------------------------------------
    # LINE
    # --------------------------------------------------------

    line = journey["Line"]

    print(
        f"• Journey → Line       "
        f"X: {line['position']['x']} "
        f"Y: {line['position']['y']}"
    )

    assert line["position"]["x"] == 20
    assert line["position"]["y"] == 100


    # --------------------------------------------------------
    # ORIGIN
    # --------------------------------------------------------

    origin = journey["Origin"]

    print(
        f"• Journey → Origin     "
        f"X: {origin['position']['x']} "
        f"Y: {origin['position']['y']}"
    )

    assert origin["position"]["x"] == 275
    assert origin["position"]["y"] == 100


    # --------------------------------------------------------
    # HEARTS
    # --------------------------------------------------------

    hearts = journey["Hearts"]

    print(
        f"• Journey → Hearts     "
        f"X: {hearts['position']['x']} "
        f"Y: {hearts['position']['y']}"
    )

    assert hearts["position"]["x"] == -245
    assert hearts["position"]["y"] == 100


    # --------------------------------------------------------
    # HEARTS → KWGT POSITION
    # --------------------------------------------------------

    hearts_kwgt = hearts["kwgt_position"]

    print()
    print("HEARTS → KWGT")
    print("-" * 50)

    print(
        f"X Right: {hearts_kwgt['x_right']}"
    )

    print(
        f"X Left:  {hearts_kwgt['x_left']}"
    )

    print(
        f"Y Down:  {hearts_kwgt['y_down']}"
    )

    print(
        f"Y Up:    {hearts_kwgt['y_up']}"
    )

    assert hearts_kwgt["x_right"] == 0
    assert hearts_kwgt["x_left"] == 245

    assert hearts_kwgt["y_down"] == 100
    assert hearts_kwgt["y_up"] == 0


    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    footer = components["Footer"]

    print()
    print(
        f"• Footer               "
        f"X: {footer['position']['x']} "
        f"Y: {footer['position']['y']}"
    )

    assert footer["position"]["x"] == 200
    assert footer["position"]["y"] == -125


    # --------------------------------------------------------
    # COVER
    # --------------------------------------------------------

    cover = components["Cover"]

    print(
        f"• Cover                "
        f"X: {cover['position']['x']} "
        f"Y: {cover['position']['y']}"
    )

    assert cover["position"]["x"] == -300
    assert cover["position"]["y"] == 0


    # ========================================================
    # PLANE
    # ========================================================

    plane = journey["Plane"]

    print()
    print("PLANE")
    print("-" * 50)

    print(f"Progress: {EVENT['progress']}")
    print(f"X Left:  {plane['x_left']}")
    print(f"X Right: {plane['x_right']}")
    print(f"Y:       {plane['y']}")


    # --------------------------------------------------------
    # PLANE → KWGT POSITION
    # --------------------------------------------------------

    plane_kwgt = plane["kwgt_position"]

    print()
    print("PLANE → KWGT")
    print("-" * 50)

    print(
        f"X Left:  {plane_kwgt['x_left']}"
    )

    print(
        f"X Right: {plane_kwgt['x_right']}"
    )

    print(
        f"Y:       {plane_kwgt['y']}"
    )

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


    # ========================================================
    # SUCCESS
    # ========================================================

    print()
    print("=" * 50)
    print("             🟢 TEST PASSED")
    print("=" * 50)
    print()


if __name__ == "__main__":
    main()