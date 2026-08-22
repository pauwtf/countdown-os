# ============================================================
# COUNTDOWN OS — LAYOUT OUTPUT
# Version: 1.2 Elegance
# ============================================================

import json
from pathlib import Path

from layout_engine import build_layout

from kwgt_coordinate_adapter import (
    adapt_directional_position,
    adapt_dual_x_position,
)


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "output"

LAYOUT_FILE = OUTPUT_DIR / "layout.json"


# ============================================================
# KWGT POSITION ADAPTER
# ============================================================

def add_kwgt_positions(node):
    """
    Añade la representación de coordenadas KWGT
    a los nodos que contienen posiciones.

    Countdown OS:

        position.x
        position.y

    KWGT:

        x_right
        x_left
        y_down
        y_up

    Plane:

        x_left
        x_right
        y

    IMPORTANTE:

    - Nunca modifica `position`.
    - Nunca procesa `kwgt_position`.
    - Nunca crea coordenadas para nodos que no las tienen.
    """

    # ========================================================
    # DICT
    # ========================================================

    if isinstance(node, dict):

        # ----------------------------------------------------
        # STANDARD POSITION
        # ----------------------------------------------------

        position = node.get("position")

        if isinstance(position, dict):

            x = position.get("x")
            y = position.get("y")

            if x is not None and y is not None:

                node["kwgt_position"] = (
                    adapt_directional_position(
                        x,
                        y
                    )
                )

        # ----------------------------------------------------
        # PLANE — DUAL X POSITION
        # ----------------------------------------------------

        if (
            "x_left" in node
            and "x_right" in node
            and "y" in node
        ):

            node["kwgt_position"] = (
                adapt_dual_x_position(
                    node["x_left"],
                    node["x_right"],
                    node["y"]
                )
            )

        # ----------------------------------------------------
        # RECURSION
        # ----------------------------------------------------

        for key, value in list(node.items()):

            # Never recurse into generated adapter output.
            if key == "kwgt_position":
                continue

            if isinstance(value, (dict, list)):

                add_kwgt_positions(value)

        return node

    # ========================================================
    # LIST
    # ========================================================

    if isinstance(node, list):

        for item in node:

            if isinstance(item, (dict, list)):

                add_kwgt_positions(item)

    return node


# ============================================================
# EVENT → LAYOUT
# ============================================================

def generate_layout(event):
    """
    Genera el layout abstracto a partir del evento.
    """

    return build_layout(event)


# ============================================================
# LAYOUT → KWGT
# ============================================================

def prepare_kwgt_layout(layout):
    """
    Añade coordenadas KWGT al layout.

    El modelo abstracto permanece intacto.

    Ejemplo:

        position:
            x: 195
            y: -20

    se convierte adicionalmente en:

        kwgt_position:
            x_right: 195
            x_left: 0
            y_down: 0
            y_up: 20
    """

    if not isinstance(layout, dict):

        raise TypeError(
            "Layout must be a dictionary."
        )

    add_kwgt_positions(layout)

    return layout


# ============================================================
# VALIDATE LAYOUT
# ============================================================

def validate_layout_output(layout):
    """
    Validaciones mínimas antes de escribir layout.json.
    """

    if not isinstance(layout, dict):

        raise TypeError(
            "Layout output must be a dictionary."
        )

    if "canvas" not in layout:

        raise ValueError(
            "Layout is missing canvas."
        )

    if "components" not in layout:

        raise ValueError(
            "Layout is missing components."
        )

    canvas = layout["canvas"]

    if not isinstance(canvas, dict):

        raise TypeError(
            "Canvas must be a dictionary."
        )

    required_canvas = (
        "width",
        "height",
        "anchor"
    )

    for key in required_canvas:

        if key not in canvas:

            raise ValueError(
                f"Canvas is missing '{key}'."
            )

    components = layout["components"]

    if not isinstance(components, dict):

        raise TypeError(
            "Components must be a dictionary."
        )

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

    for component in required_components:

        if component not in components:

            raise ValueError(
                f"Missing component: {component}"
            )

    return True


# ============================================================
# WRITE LAYOUT
# ============================================================

def write_layout(layout):
    """
    Escribe el Layout Contract v1.2
    en output/layout.json.
    """

    # --------------------------------------------------------
    # VALIDATE INPUT
    # --------------------------------------------------------

    validate_layout_output(layout)

    # --------------------------------------------------------
    # PREPARE KWGT DATA
    # --------------------------------------------------------

    output_layout = prepare_kwgt_layout(
        layout
    )

    # --------------------------------------------------------
    # VALIDATE PREPARED OUTPUT
    # --------------------------------------------------------

    validate_layout_output(
        output_layout
    )

    # --------------------------------------------------------
    # OUTPUT DIRECTORY
    # --------------------------------------------------------

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # OUTPUT CONTRACT
    # --------------------------------------------------------

    output = {
        "version": "1.2",
        "system": "Countdown OS Layout System",
        "canvas": output_layout["canvas"],
        "components": output_layout["components"]
    }

    # --------------------------------------------------------
    # WRITE JSON
    # --------------------------------------------------------

    with LAYOUT_FILE.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            ensure_ascii=False,
            indent=2
        )

    return LAYOUT_FILE


# ============================================================
# EVENT → JSON
# ============================================================

def generate_layout_file(event):
    """
    Genera el layout completo y lo guarda.
    """

    layout = generate_layout(event)

    return write_layout(layout)


# ============================================================
# MANUAL TEST
# ============================================================

if __name__ == "__main__":

    event = {
        "titleDisplay": "UNTIL ALEX",
        "daysDisplay": "48",
        "progressDisplay": "66%",
        "notesDisplay": "Comprar cacao",
        "destinationDisplay": "",
        "arrivalDisplay": "",
        "progress": 0.6571428571428571
    }

    path = generate_layout_file(
        event
    )

    print()
    print("=" * 50)
    print("       COUNTDOWN OS — LAYOUT OUTPUT")
    print("=" * 50)

    print()
    print(f"Output: {path}")

    print()
    print(f"Exists: {path.exists()}")

    print()
    print("🟢 layout.json generated")
    print()