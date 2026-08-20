# ============================================================
# COUNTDOWN OS — PROGRESS TEST
# Version: 1.2 Elegance
# ============================================================

from layout_engine import resolve_plane_position


TEST_VALUES = [
    0,
    0.25,
    0.5,
    0.75,
    1,
    -1,
    2,
    None
]


EXPECTED_X = {
    0: 0,
    0.25: 130,
    0.5: 260,
    0.75: 390,
    1: 520,
    -1: 0,
    2: 520,
    None: 0
}


def main():

    print()
    print("=" * 46)
    print("       COUNTDOWN OS — PROGRESS TEST")
    print("=" * 46)

    print()
    print("PROGRESS → PLANE POSITION")
    print("-" * 46)


    for progress in TEST_VALUES:

        position = resolve_plane_position(
            progress
        )

        x_left = position["x_left"]
        x_right = position["x_right"]
        y = position["y"]

        expected = EXPECTED_X[progress]

        print(
            f"Progress: {str(progress):<5} "
            f"| X Left: {x_left:<5} "
            f"| X Right: {x_right} "
            f"| Y: {y}"
        )

        assert x_left == expected

        assert x_right == 275

        assert y == 93


    print()
    print("=" * 46)
    print("             🟢 TEST PASSED")
    print("=" * 46)
    print()


if __name__ == "__main__":
    main()