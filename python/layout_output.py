# ============================================================
# COUNTDOWN OS — LAYOUT OUTPUT
# Version: 1.2 Elegance
# ============================================================

import json
from pathlib import Path

from layout_engine import build_layout


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "output"

LAYOUT_FILE = OUTPUT_DIR / "layout.json"


# ============================================================
# EVENT → LAYOUT
# ============================================================

def generate_layout(event):
    """
    Genera el layout a partir del evento preparado.
    """

    return build_layout(event)


# ============================================================
# WRITE LAYOUT
# ============================================================

def write_layout(layout):
    """
    Escribe el Layout Contract v1.2
    en output/layout.json.
    """

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    output = {
        "version": "1.2",
        "system": "Countdown OS Layout System",
        "canvas": layout["canvas"],
        "components": layout["components"]
    }

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