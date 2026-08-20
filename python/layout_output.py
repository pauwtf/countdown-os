# ============================================================
# COUNTDOWN OS — LAYOUT OUTPUT
# Version: 1.2 Elegance
# ============================================================

import json
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "output"

LAYOUT_FILE = OUTPUT_DIR / "layout.json"


# ============================================================
# WRITE
# ============================================================

def write_layout(layout):
    """
    Guarda el layout generado por Layout Engine
    como output/layout.json.
    """

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        LAYOUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            layout,
            file,
            ensure_ascii=False,
            indent=2
        )

    return LAYOUT_FILE


# ============================================================
# TEST / MANUAL EXECUTION
# ============================================================

if __name__ == "__main__":

    from layout_engine import build_layout

    event = {
        "titleDisplay": "UNTIL ALEX",
        "daysDisplay": "48",
        "progressDisplay": "66%",
        "notesDisplay": "Comprar cacao",
        "destinationDisplay": "",
        "arrivalDisplay": "",
        "progress": 0.6571428571428571
    }

    layout = build_layout(event)

    path = write_layout(layout)

    print()
    print("=" * 50)
    print("       COUNTDOWN OS — LAYOUT OUTPUT")
    print("=" * 50)

    print()
    print("PROJECT ROOT:")
    print(PROJECT_ROOT)

    print()
    print("OUTPUT DIRECTORY:")
    print(OUTPUT_DIR)

    print()
    print("LAYOUT FILE:")
    print(path)

    print()
    print("FILE EXISTS:")
    print(path.exists())

    print()
    print("🟢 layout.json generated")
    print()