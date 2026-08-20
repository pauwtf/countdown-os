# ============================================================
# COUNTDOWN OS — LAYOUT OUTPUT TEST
# Version: 1.2 Elegance
# ============================================================

import json
from pathlib import Path

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


def main():

    print()
    print("=" * 46)
    print("       COUNTDOWN OS — LAYOUT OUTPUT TEST")
    print("=" * 46)

    # --------------------------------------------------------
    # BUILD LAYOUT
    # --------------------------------------------------------

    layout = build_layout(EVENT)

    # --------------------------------------------------------
    # WRITE JSON
    # --------------------------------------------------------

    write_layout(layout)

    print()
    print(f"Output: {LAYOUT_FILE}")

    # --------------------------------------------------------
    # VERIFY FILE
    # --------------------------------------------------------

    assert LAYOUT_FILE.exists(), (
        "layout.json was not created."
    )

    print("✓ layout.json exists")


    # --------------------------------------------------------
    # READ JSON
    # --------------------------------------------------------

    with LAYOUT_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        saved_layout = json.load(file)


    print("✓ layout.json is valid JSON")


    # --------------------------------------------------------
    # BASIC CONTRACT
    # --------------------------------------------------------

    assert "canvas" in saved_layout
    assert "components" in saved_layout

    print("✓ canvas exists")
    print("✓ components exists")


    # --------------------------------------------------------
    # CANVAS
    # --------------------------------------------------------

    canvas = saved_layout["canvas"]

    assert canvas["width"] == 400
    assert canvas["height"] == 200
    assert canvas["anchor"] == "center"

    print("✓ canvas contract valid")


    # --------------------------------------------------------
    # COMPONENTS
    # --------------------------------------------------------

    components = saved_layout["components"]

    required = [
        "Background",
        "Cover",
        "Header",
        "Gradient",
        "Counter",
        "Content",
        "Footer",
        "test"
    ]

    for component in required:

        assert component in components, (
            f"Missing component: {component}"
        )

        print(
            f"✓ {component}"
        )


    # --------------------------------------------------------
    # PLANE
    # --------------------------------------------------------

    plane = (
        components
        ["Content"]
        ["journey"]
        ["Plane"]
    )

    assert "x_left" in plane
    assert "x_right" in plane
    assert "y" in plane

    print("✓ Plane position exported")


    # --------------------------------------------------------
    # SUCCESS
    # --------------------------------------------------------

    print()
    print("=" * 46)
    print("             🟢 TEST PASSED")
    print("=" * 46)
    print()


if __name__ == "__main__":
    main()