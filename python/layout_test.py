# ============================================================
# COUNTDOWN OS — LAYOUT ENGINE TEST
# Version: 1.2 Elegance
# ============================================================

from layout_engine import build_layout


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
    print("       COUNTDOWN OS — LAYOUT ENGINE TEST")
    print("=" * 46)

    # ========================================================
    # BUILD
    # ========================================================

    layout = build_layout(EVENT)

    canvas = layout["canvas"]
    components = layout["components"]


    # ========================================================
    # CANVAS
    # ========================================================

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


    # ========================================================
    # HEADER
    # ========================================================

    print()
    print("HEADER")
    print("-" * 46)

    header = components["Header"]

    title = header["Title"]
    days = header["Days"]

    print(
        f"Title               "
        f"X: {title['position']['x']}       "
        f"Y: {title['position']['y']}"
    )

    print(
        f"Days                "
        f"X: {days['position']['x']}        "
        f"Y: {days['position']['y']}"
    )

    print(
        f"Title text: "
        f"{title['TitleText']['value']}"
    )

    print(
        f"Days text: "
        f"{days['DaysText']['value']}"
    )


    # ========================================================
    # COUNTER
    # ========================================================

    print()
    print("COUNTER")
    print("-" * 46)

    counter = components["Counter"]

    days_remaining = counter["DaysRemaining"]

    print(
        f"Counter             "
        f"X: {counter['position']['x']}       "
        f"Y: {counter['position']['y']}"
    )

    print(
        f"Days Remaining      "
        f"X: {days_remaining['position']['x']}       "
        f"Y: {days_remaining['position']['y']}"
    )

    print(
        f"Value: "
        f"{days_remaining['DaysRemainingText']['value']}"
    )


    # ========================================================
    # JOURNEY
    # ========================================================

    print()
    print("JOURNEY")
    print("-" * 46)

    content = components["Content"]
    journey = content["journey"]

    print(
        f"Journey             "
        f"X: {journey['position']['x']}         "
        f"Y: {journey['position']['y']}"
    )


    # --------------------------------------------------------
    # LINE
    # --------------------------------------------------------

    line = journey["Line"]

    line_shape = line["JourneyLineShape"]

    print(
        f"Line                "
        f"X: {line['position']['x']}      "
        f"Y: {line['position']['y']}"
    )

    print(
        f"Line size: "
        f"{line_shape['width']} × "
        f"{line_shape['height']}"
    )


    # --------------------------------------------------------
    # ORIGIN
    # --------------------------------------------------------

    origin = journey["Origin"]

    origin_shape = origin["OriginShape"]

    print(
        f"Origin              "
        f"X: {origin['position']['x']}      "
        f"Y: {origin['position']['y']}"
    )

    print(
        f"Origin size: "
        f"{origin_shape['size']} × "
        f"{origin_shape['size']}"
    )


    # --------------------------------------------------------
    # PLANE
    # --------------------------------------------------------

    plane = journey["Plane"]

    print()
    print("PLANE")
    print("-" * 46)

    print(
        f"Progress: "
        f"{EVENT['progress']}"
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

    print(
        f"Text: "
        f"{plane['PlaneText']['value']}"
    )


    # ========================================================
    # HEARTS
    # ========================================================

    hearts = journey["Hearts"]

    print()
    print("HEARTS")
    print("-" * 46)

    print(
        f"Hearts              "
        f"X: {hearts['position']['x']}      "
        f"Y: {hearts['position']['y']}"
    )

    destination = hearts["Destination"]

    print(
        f"Destination         "
        f"X: {destination['position']['x']}      "
        f"Y: {destination['position']['y']}"
    )

    arrival = hearts["Arrival"]

    print(
        f"Arrival             "
        f"X: {arrival['position']['x']}      "
        f"Y: {arrival['position']['y']}"
    )


    # ========================================================
    # FOOTER
    # ========================================================

    print()
    print("FOOTER")
    print("-" * 46)

    footer = components["Footer"]

    print(
        f"Footer              "
        f"X: {footer['position']['x']}      "
        f"Y: {footer['position']['y']}"
    )

    print(
        f"Text: "
        f"{footer['FooterText']['value']}"
    )


    # ========================================================
    # COVER
    # ========================================================

    print()
    print("COVER")
    print("-" * 46)

    cover = components["Cover"]

    print(
        f"Cover               "
        f"X: {cover['position']['x']}      "
        f"Y: {cover['position']['y']}"
    )

    print(
        f"Cover text: "
        f"{cover['coverImage']['coverText']['value']}"
    )


    # ========================================================
    # GRADIENT
    # ========================================================

    print()
    print("GRADIENT")
    print("-" * 46)

    gradient = components["Gradient"]

    vertical = gradient["Vertical"]
    horizontal = gradient["Horizontal"]

    print(
        f"Vertical            "
        f"X: {vertical['position']['x']}      "
        f"Y: {vertical['position']['y']}"
    )

    print(
        f"Vertical size: "
        f"{vertical['GradientVerticalShape']['width']} × "
        f"{vertical['GradientVerticalShape']['height']}"
    )

    print(
        f"Horizontal          "
        f"X: {horizontal['position']['x']}      "
        f"Y: {horizontal['position']['y']}"
    )

    print(
        f"Horizontal size: "
        f"{horizontal['GradientHorizontalShape']['width']} × "
        f"{horizontal['GradientHorizontalShape']['height']}"
    )


    # ========================================================
    # TEST
    # ========================================================

    test = components["test"]

    print()
    print("TEST")
    print("-" * 46)

    print(
        f"Test text: "
        f"{test['TestText']['value']}"
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