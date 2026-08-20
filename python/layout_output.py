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
    a todos los elementos que utilizan position.x/y.

    Countdown OS conserva:

        position:
            x
            y

    KWGT recibe:

        kwgt_position:
            x_right
            x_left
            y_down
            y_up
    """

    if isinstance(node, dict):

        # ----------------------------------------------------
        # STANDARD POSITION
        # ----------------------------------------------------

        if "position" in node:

            position = node["position"]

            if (
                isinstance(position, dict)
                and "x" in position
                and "y" in position
            ):

                node["kwgt_position"] = (
                    adapt_directional_position(
                        position["x"],
                        position["y"]
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
        # RECURSE THROUGH CHILDREN
        # ----------------------------------------------------

        for value in node.values():

            if isinstance(value, (dict, list)):

                add_kwgt_positions(value)

    elif isinstance(node, list):

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
    Añade al layout la representación de coordenadas
    específica para KWGT.

    No modifica la posición abstracta original.
    """

    add_kwgt_positions(layout)

    return layout


# ============================================================
# WRITE LAYOUT
# ============================================================

def write_layout(layout):
    """
    Escribe el Layout Contract v1.2
    en output/layout.json.

    El JSON conserva las coordenadas abstractas
    y añade sus equivalentes KWGT.
    """

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # PREPARE KWGT DATA
    # --------------------------------------------------------

    output_layout = prepare_kwgt_layout(
        layout
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

    path = generate_layout_file(event)

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