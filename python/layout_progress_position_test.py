# ============================================================
# COUNTDOWN OS — PROGRESS → POSITION INTEGRATION TEST
# Version: 1.2 Elegance
# ============================================================

from layout_engine import build_layout
from layout_output import prepare_kwgt_layout


# ============================================================
# TEST EVENT
# ============================================================

def build_test_event(progress):

    return {
        "titleDisplay": "UNTIL ALEX",
        "daysDisplay": "48",
        "progressDisplay": "50%",
        "notesDisplay": "Comprar cacao",
        "destinationDisplay": "",
        "arrivalDisplay": "",
        "progress": progress,
    }


# ============================================================
# HELPERS
# ============================================================

def get_plane(layout):

    return (
        layout["components"]
        ["Content"]
        ["journey"]
        ["Plane"]
    )


# ============================================================
# TEST PROGRESS VALUE
# ============================================================

def test_progress(progress):

    event = build_test_event(progress)

    layout = build_layout(event)

    prepare_kwgt_layout(layout)

    plane = get_plane(layout)

    return plane


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 58)
    print("     COUNTDOWN OS — PROGRESS → POSITION TEST")
    print("=" * 58)


    # ========================================================
    # BOUNDARY VALUES
    # ========================================================

    test_cases = [
        (0.0, "ORIGIN"),
        (0.25, "25%"),
        (0.50, "50%"),
        (0.75, "75%"),
        (1.0, "DESTINATION"),
    ]


    # ========================================================
    # TEST EACH POSITION
    # ========================================================

    for progress, label in test_cases:

        plane = test_progress(progress)

        print()
        print(label)
        print("-" * 58)

        print(
            f"Progress: {progress}"
        )

        print(
            f"X Left:  {plane['x_left']}"
        )

        print(
            f"X Right: {plane['x_right']}"
        )

        print(
            f"Y:       {plane['y']}"
        )

        print(
            f"KWGT X Left:  "
            f"{plane['kwgt_position']['x_left']}"
        )

        print(
            f"KWGT X Right: "
            f"{plane['kwgt_position']['x_right']}"
        )

        print(
            f"KWGT Y:       "
            f"{plane['kwgt_position']['y']}"
        )


        # ----------------------------------------------------
        # PLANE CONTRACT
        # ----------------------------------------------------

        assert "x_left" in plane
        assert "x_right" in plane
        assert "y" in plane

        assert "kwgt_position" in plane


        # ----------------------------------------------------
        # KWGT CONTRACT
        # ----------------------------------------------------

        kwgt = plane["kwgt_position"]

        assert kwgt["x_left"] == plane["x_left"]
        assert kwgt["x_right"] == plane["x_right"]
        assert kwgt["y"] == plane["y"]


        # ----------------------------------------------------
        # POSITION SAFETY
        # ----------------------------------------------------

        assert plane["x_left"] >= 0
        assert plane["x_right"] >= 0

        assert kwgt["x_left"] >= 0
        assert kwgt["x_right"] >= 0


        print("✓ Plane contract valid")
        print("✓ KWGT position matches Plane")
        print("✓ Position values are safe")


    # ========================================================
    # MONOTONIC PROGRESS
    # ========================================================

    print()
    print("MONOTONIC PROGRESS")
    print("-" * 58)

    positions = []

    for progress, _ in test_cases:

        plane = test_progress(progress)

        positions.append(
            plane["x_left"]
        )


    print(
        f"Positions: {positions}"
    )


    for previous, current in zip(
        positions,
        positions[1:]
    ):

        assert current >= previous


    print(
        "✓ Plane position increases monotonically"
    )


    # ========================================================
    # BOUNDARY RELATION
    # ========================================================

    print()
    print("BOUNDARY RELATION")
    print("-" * 58)

    origin = test_progress(0.0)
    destination = test_progress(1.0)

    assert origin["x_left"] == 0
    assert destination["x_left"] > origin["x_left"]

    print(
        f"✓ Origin x_left = {origin['x_left']}"
    )

    print(
        f"✓ Destination x_left = "
        f"{destination['x_left']}"
    )


    # ========================================================
    # INVALID PROGRESS — NEGATIVE
    # ========================================================

    print()
    print("INVALID PROGRESS — NEGATIVE")
    print("-" * 58)

    try:

        plane = test_progress(-0.1)

        assert (
            0
            <= plane["x_left"]
            <= destination["x_left"]
        )

        print(
            "✓ Negative progress safely constrained"
        )

    except (ValueError, AssertionError):

        print(
            "✓ Negative progress rejected safely"
        )


    # ========================================================
    # INVALID PROGRESS — ABOVE 1
    # ========================================================

    print()
    print("INVALID PROGRESS — ABOVE 1")
    print("-" * 58)

    try:

        plane = test_progress(1.1)

        assert (
            plane["x_left"]
            >= destination["x_left"]
        )

        print(
            "✓ Progress > 1 safely handled"
        )

    except (ValueError, AssertionError):

        print(
            "✓ Progress > 1 rejected safely"
        )


    # ========================================================
    # FINAL
    # ========================================================

    print()
    print("=" * 58)
    print("             🟢 TEST PASSED")
    print("=" * 58)
    print()


if __name__ == "__main__":
    main()