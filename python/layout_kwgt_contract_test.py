# ============================================================
# COUNTDOWN OS — KWGT LAYOUT CONTRACT TEST
# Version: 1.2 Elegance
# ============================================================

import json

from layout_output import LAYOUT_FILE


# ============================================================
# EXPECTED KWGT CONTRACT
# ============================================================

EXPECTED_COMPONENTS = [
    "Background",
    "Cover",
    "Header",
    "Gradient",
    "Counter",
    "Content",
    "Footer",
    "test",
]


# ============================================================
# HELPERS
# ============================================================

def assert_directional_position(position, name):
    """
    Valida que un componente con posición estándar
    tenga exactamente los cuatro campos direccionales KWGT.
    """

    required = [
        "x_right",
        "x_left",
        "y_up",
        "y_down",
    ]

    for field in required:
        assert field in position, (
            f"{name} missing KWGT field: {field}"
        )

        assert isinstance(position[field], (int, float)), (
            f"{name}.{field} must be numeric"
        )


def assert_dual_x_position(position, name):
    """
    Valida posiciones KWGT con X izquierda + X derecha.
    """

    required = [
        "x_left",
        "x_right",
        "y",
    ]

    for field in required:
        assert field in position, (
            f"{name} missing Plane field: {field}"
        )

        assert isinstance(position[field], (int, float)), (
            f"{name}.{field} must be numeric"
        )


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 50)
    print("       COUNTDOWN OS — KWGT LAYOUT CONTRACT TEST")
    print("=" * 50)


    # ========================================================
    # FILE
    # ========================================================

    print()
    print("OUTPUT FILE")
    print("-" * 50)

    assert LAYOUT_FILE.exists(), (
        f"Missing layout file: {LAYOUT_FILE}"
    )

    print("✓ layout.json exists")


    # ========================================================
    # JSON
    # ========================================================

    with LAYOUT_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        layout = json.load(file)

    print("✓ layout.json is valid JSON")


    # ========================================================
    # ROOT CONTRACT
    # ========================================================

    print()
    print("ROOT CONTRACT")
    print("-" * 50)

    assert layout["version"] == "1.2"
    assert layout["system"] == "Countdown OS Layout System"

    assert "canvas" in layout
    assert "components" in layout

    print("✓ version")
    print("✓ system")
    print("✓ canvas")
    print("✓ components")


    # ========================================================
    # CANVAS
    # ========================================================

    print()
    print("CANVAS")
    print("-" * 50)

    canvas = layout["canvas"]

    assert canvas["width"] == 400
    assert canvas["height"] == 200
    assert canvas["anchor"] == "center"

    print("✓ canvas contract valid")


    # ========================================================
    # COMPONENTS
    # ========================================================

    print()
    print("COMPONENT CONTRACT")
    print("-" * 50)

    components = layout["components"]

    for component in EXPECTED_COMPONENTS:

        assert component in components, (
            f"Missing component: {component}"
        )

        print(f"✓ {component}")


    # ========================================================
    # STANDARD KWGT POSITIONS
    # ========================================================

    print()
    print("STANDARD KWGT POSITIONS")
    print("-" * 50)

    standard_components = [
        "Background",
        "Cover",
        "Counter",
        "Content",
        "Footer",
    ]

    for component_name in standard_components:

        component = components[component_name]

        assert "kwgt_position" in component, (
            f"{component_name} missing kwgt_position"
        )

        assert_directional_position(
            component["kwgt_position"],
            component_name
        )

        print(
            f"✓ {component_name} → directional position"
        )


    # ========================================================
    # COUNTER
    # ========================================================

    print()
    print("COUNTER")
    print("-" * 50)

    counter = components["Counter"]

    counter_kwgt = counter["kwgt_position"]

    assert counter_kwgt["x_right"] == 195
    assert counter_kwgt["x_left"] == 0

    # Countdown OS -20 Y means 20 units DOWN in KWGT.
    assert counter_kwgt["y_down"] == 20
    assert counter_kwgt["y_up"] == 0

    print("✓ Counter X Right = 195")
    print("✓ Counter X Left = 0")
    print("✓ Counter Y Down = 20")
    print("✓ Counter Y Up = 0")


    # ========================================================
    # HEARTS
    # ========================================================

    print()
    print("HEARTS")
    print("-" * 50)

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

    print("✓ Hearts X Left = 245")
    print("✓ Hearts X Right = 0")
    print("✓ Hearts Y Up = 100")
    print("✓ Hearts Y Down = 0")


    # ========================================================
    # ORIGIN
    # ========================================================

    print()
    print("ORIGIN")
    print("-" * 50)

    origin = (
        components["Content"]
        ["journey"]
        ["Origin"]
    )

    origin_kwgt = origin["kwgt_position"]

    assert origin_kwgt["x_right"] == 275
    assert origin_kwgt["x_left"] == 0

    assert origin_kwgt["y_up"] == 100
    assert origin_kwgt["y_down"] == 0

    print("✓ Origin X Right = 275")
    print("✓ Origin Y Up = 100")


    # ========================================================
    # PLANE
    # ========================================================

    print()
    print("PLANE")
    print("-" * 50)

    plane = (
        components["Content"]
        ["journey"]
        ["Plane"]
    )

    plane_kwgt = plane["kwgt_position"]

    assert_dual_x_position(
        plane_kwgt,
        "Plane"
    )

    assert plane_kwgt["x_left"] == plane["x_left"]
    assert plane_kwgt["x_right"] == plane["x_right"]
    assert plane_kwgt["y"] == plane["y"]

    print(
        f"✓ Plane X Left  = {plane_kwgt['x_left']}"
    )

    print(
        f"✓ Plane X Right = {plane_kwgt['x_right']}"
    )

    print(
        f"✓ Plane Y       = {plane_kwgt['y']}"
    )


    # ========================================================
    # NO INVALID KWGT OUTPUT
    # ========================================================

    print()
    print("OUTPUT SAFETY")
    print("-" * 50)

    def validate_no_negative_directional_values(
        node,
        path="root"
    ):

        if isinstance(node, dict):

            for key, value in node.items():

                current_path = f"{path}.{key}"

                if key in {
                    "x_right",
                    "x_left",
                    "y_up",
                    "y_down",
                }:

                    assert value >= 0, (
                        f"Negative KWGT directional value "
                        f"at {current_path}: {value}"
                    )

                if isinstance(value, (dict, list)):

                    validate_no_negative_directional_values(
                        value,
                        current_path
                    )

        elif isinstance(node, list):

            for index, item in enumerate(node):

                validate_no_negative_directional_values(
                    item,
                    f"{path}[{index}]"
                )


    validate_no_negative_directional_values(
        layout
    )

    print(
        "✓ No negative directional KWGT values"
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