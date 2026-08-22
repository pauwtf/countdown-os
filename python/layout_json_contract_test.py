# ============================================================
# COUNTDOWN OS — LAYOUT JSON CONTRACT TEST
# Version: 1.2 Elegance
# ============================================================

import json
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

LAYOUT_FILE = (
    PROJECT_ROOT
    / "output"
    / "layout.json"
)


# ============================================================
# HELPERS
# ============================================================

def load_layout():
    """
    Carga el layout.json generado por Countdown OS.
    """

    assert LAYOUT_FILE.exists(), (
        f"Missing layout file: {LAYOUT_FILE}"
    )

    with LAYOUT_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def assert_kwgt_position(
    position,
    *,
    directional=True,
):
    """
    Valida una posición KWGT.

    Posición direccional:
        x_right
        x_left
        y_up
        y_down

    Posición dual-X:
        x_left
        x_right
        y
    """

    assert isinstance(position, dict)

    if directional:

        required = {
            "x_right",
            "x_left",
            "y_up",
            "y_down",
        }

        assert required.issubset(position.keys()), (
            f"Invalid directional KWGT position: {position}"
        )

        for key in required:

            assert isinstance(
                position[key],
                (int, float)
            ), (
                f"{key} must be numeric"
            )

            assert position[key] >= 0, (
                f"{key} cannot be negative: "
                f"{position[key]}"
            )

    else:

        required = {
            "x_left",
            "x_right",
            "y",
        }

        assert required.issubset(position.keys()), (
            f"Invalid dual-X KWGT position: {position}"
        )

        for key in required:

            assert isinstance(
                position[key],
                (int, float)
            ), (
                f"{key} must be numeric"
            )

        assert position["x_left"] >= 0
        assert position["x_right"] >= 0


# ============================================================
# MAIN TEST
# ============================================================

def main():

    print()
    print("=" * 54)
    print("       COUNTDOWN OS — LAYOUT JSON CONTRACT TEST")
    print("=" * 54)


    # ========================================================
    # LOAD
    # ========================================================

    print()
    print("FILE")
    print("-" * 54)

    layout = load_layout()

    print(f"✓ layout.json exists")
    print(f"✓ layout.json loaded")


    # ========================================================
    # ROOT CONTRACT
    # ========================================================

    print()
    print("ROOT CONTRACT")
    print("-" * 54)

    assert isinstance(layout, dict)

    assert layout["version"] == "1.2"

    assert (
        layout["system"]
        == "Countdown OS Layout System"
    )

    assert "canvas" in layout
    assert "components" in layout

    print("✓ root object valid")
    print("✓ version = 1.2")
    print("✓ system identifier valid")
    print("✓ canvas exists")
    print("✓ components exists")


    # ========================================================
    # CANVAS
    # ========================================================

    print()
    print("CANVAS CONTRACT")
    print("-" * 54)

    canvas = layout["canvas"]

    assert canvas["width"] == 400
    assert canvas["height"] == 200
    assert canvas["anchor"] == "center"

    print("✓ width = 400")
    print("✓ height = 200")
    print("✓ anchor = center")


    # ========================================================
    # COMPONENTS
    # ========================================================

    print()
    print("COMPONENT CONTRACT")
    print("-" * 54)

    components = layout["components"]

    required_components = [
        "Background",
        "Cover",
        "Header",
        "Gradient",
        "Counter",
        "Content",
        "Footer",
        "test",
    ]

    for name in required_components:

        assert name in components, (
            f"Missing component: {name}"
        )

        assert isinstance(
            components[name],
            dict
        )

        print(f"✓ {name}")


    # ========================================================
    # STANDARD KWGT POSITIONS
    # ========================================================

    print()
    print("STANDARD KWGT POSITIONS")
    print("-" * 54)

    standard_components = [
        "Background",
        "Cover",
        "Header",
        "Gradient",
        "Counter",
        "Content",
        "Footer",
    ]

    for name in standard_components:

        component = components[name]

        if "kwgt_position" in component:

            assert_kwgt_position(
                component["kwgt_position"]
            )

            print(
                f"✓ {name}.kwgt_position"
            )


    # ========================================================
    # COUNTER
    # ========================================================

    print()
    print("COUNTER")
    print("-" * 54)

    counter = components["Counter"]

    assert counter["position"]["x"] == 195
    assert counter["position"]["y"] == -20

    counter_kwgt = counter["kwgt_position"]

    assert counter_kwgt["x_right"] == 195
    assert counter_kwgt["x_left"] == 0

    # Countdown OS -Y = KWGT y_down
    assert counter_kwgt["y_down"] == 20
    assert counter_kwgt["y_up"] == 0

    print("✓ Countdown position valid")
    print("✓ X Right = 195")
    print("✓ X Left = 0")
    print("✓ Y Down = 20")
    print("✓ Y Up = 0")


    # ========================================================
    # HEARTS
    # ========================================================

    print()
    print("HEARTS")
    print("-" * 54)

    hearts = (
        components["Content"]
        ["journey"]
        ["Hearts"]
    )

    hearts_kwgt = hearts["kwgt_position"]

    assert hearts_kwgt["x_right"] == 0
    assert hearts_kwgt["x_left"] == 245

    assert hearts_kwgt["y_down"] == 0
    assert hearts_kwgt["y_up"] == 100

    print("✓ X Right = 0")
    print("✓ X Left = 245")
    print("✓ Y Down = 0")
    print("✓ Y Up = 100")


    # ========================================================
    # PLANE
    # ========================================================

    print()
    print("PLANE")
    print("-" * 54)

    plane = (
        components["Content"]
        ["journey"]
        ["Plane"]
    )

    assert "x_left" in plane
    assert "x_right" in plane
    assert "y" in plane

    plane_kwgt = plane["kwgt_position"]

    assert_kwgt_position(
        plane_kwgt,
        directional=False,
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

    print("✓ Plane uses dual-X contract")
    print("✓ X Left valid")
    print("✓ X Right valid")
    print("✓ Y valid")
    print("✓ Plane adapter output matches source")


    # ========================================================
    # JOURNEY
    # ========================================================

    print()
    print("JOURNEY")
    print("-" * 54)

    journey = (
        components["Content"]
        ["journey"]
    )

    assert "Line" in journey
    assert "Origin" in journey
    assert "Plane" in journey
    assert "Hearts" in journey

    print("✓ Line")
    print("✓ Origin")
    print("✓ Plane")
    print("✓ Hearts")


    # ========================================================
    # NO NEGATIVE DIRECTIONAL VALUES
    # ========================================================

    print()
    print("KWGT DIRECTION SAFETY")
    print("-" * 54)

    def walk(node, path="root"):

        if isinstance(node, dict):

            if "kwgt_position" in node:

                position = node["kwgt_position"]

                if (
                    "x_right" in position
                    and "x_left" in position
                    and "y_up" in position
                    and "y_down" in position
                ):

                    for key in (
                        "x_right",
                        "x_left",
                        "y_up",
                        "y_down",
                    ):

                        assert position[key] >= 0, (
                            f"Negative KWGT directional "
                            f"value at {path}.{key}"
                        )

            for key, value in node.items():

                walk(
                    value,
                    f"{path}.{key}"
                )

        elif isinstance(node, list):

            for index, item in enumerate(node):

                walk(
                    item,
                    f"{path}[{index}]"
                )

    walk(layout)

    print(
        "✓ No negative directional KWGT values"
    )


    # ========================================================
    # SUCCESS
    # ========================================================

    print()
    print("=" * 54)
    print("             🟢 TEST PASSED")
    print("=" * 54)
    print()


if __name__ == "__main__":
    main()