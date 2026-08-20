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


def assert_equal(
    actual,
    expected,
    label
):

    if actual != expected:

        raise AssertionError(
            f"{label}: "
            f"expected {expected}, "
            f"got {actual}"
        )


def main():

    print()
    print("=" * 46)
    print("       COUNTDOWN OS — LAYOUT CONTRACT TEST")
    print("=" * 46)


    # ========================================================
    # BUILD
    # ========================================================

    layout = build_layout(EVENT)


    # ========================================================
    # CANVAS
    # ========================================================

    canvas = layout["canvas"]

    print()
    print("CANVAS")
    print("-" * 46)

    print(
        f"Width:  {canvas['width']}"
    )

    print(
        f"Height: {canvas['height']}"
    )

    print(
        f"Anchor: {canvas['anchor']}"
    )

    assert_equal(
        canvas["width"],
        400,
        "Canvas width"
    )

    assert_equal(
        canvas["height"],
        200,
        "Canvas height"
    )

    assert_equal(
        canvas["anchor"],
        "center",
        "Canvas anchor"
    )


    # ========================================================
    # HIERARCHY
    # ========================================================

    print()
    print("COMPONENT HIERARCHY")
    print("-" * 46)

    validate_hierarchy(
        layout["components"],
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


    components = layout["components"]


    # Background

    background = components["Background"]

    print(
        f"• Background             "
        f"X: {background['position']['x']} "
        f"Y: {background['position']['y']}"
    )


    # Header

    title = (
        components["Header"]
        ["Title"]
    )

    days = (
        components["Header"]
        ["Days"]
    )

    print(
        f"• Header → Title         "
        f"X: {title['position']['x']} "
        f"Y: {title['position']['y']}"
    )

    print(
        f"• Header → Days          "
        f"X: {days['position']['x']} "
        f"Y: {days['position']['y']}"
    )


    # Counter

    counter = components["Counter"]

    print(
        f"• Counter                "
        f"X: {counter['position']['x']} "
        f"Y: {counter['position']['y']}"
    )


    # Journey

    journey = (
        components["Content"]
        ["journey"]
    )

    print(
        f"• Journey                "
        f"X: {journey['position']['x']} "
        f"Y: {journey['position']['y']}"
    )


    line = journey["Line"]

    print(
        f"• Journey → Line         "
        f"X: {line['position']['x']} "
        f"Y: {line['position']['y']}"
    )


    origin = journey["Origin"]

    print(
        f"• Journey → Origin       "
        f"X: {origin['position']['x']} "
        f"Y: {origin['position']['y']}"
    )


    hearts = journey["Hearts"]

    print(
        f"• Journey → Hearts       "
        f"X: {hearts['position']['x']} "
        f"Y: {hearts['position']['y']}"
    )


    # Footer

    footer = components["Footer"]

    print(
        f"• Footer                 "
        f"X: {footer['position']['x']} "
        f"Y: {footer['position']['y']}"
    )


    # Cover

    cover = components["Cover"]

    print(
        f"• Cover                  "
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

    print(
        f"Progress: "
        f"{EVENT['progress']}"
    )

    print(
        f"X Left:  "
        f"{plane['x_left']}"
    )

    print(
        f"X Right: "
        f"{plane['x_right']}"
    )

    print(
        f"Y:       "
        f"{plane['y']}"
    )


    # ========================================================
    # CRITICAL ASSERTIONS
    # ========================================================

    assert_equal(
        title["position"]["x"],
        175.0,
        "Title X"
    )

    assert_equal(
        title["position"]["y"],
        -125.0,
        "Title Y"
    )

    assert_equal(
        days["position"]["x"],
        50.0,
        "Days X"
    )

    assert_equal(
        days["position"]["y"],
        21.0,
        "Days Y"
    )

    assert_equal(
        counter["position"]["x"],
        195.0,
        "Counter X"
    )

    assert_equal(
        counter["position"]["y"],
        -20.0,
        "Counter Y"
    )

    assert_equal(
        line["position"]["x"],
        20.0,
        "Line X"
    )

    assert_equal(
        line["position"]["y"],
        100.0,
        "Line Y"
    )

    assert_equal(
        origin["position"]["x"],
        275.0,
        "Origin X"
    )

    assert_equal(
        origin["position"]["y"],
        100.0,
        "Origin Y"
    )

    assert_equal(
        hearts["position"]["x"],
        -245.0,
        "Hearts X"
    )

    assert_equal(
        hearts["position"]["y"],
        100.0,
        "Hearts Y"
    )


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