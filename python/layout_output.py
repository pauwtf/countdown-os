 # ============================================================
# COUNTDOWN OS — LAYOUT OUTPUT
# Version: 1.2 Elegance
# ============================================================

import json
from pathlib import Path


# ============================================================
# OUTPUT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "output"

LAYOUT_FILE = OUTPUT_DIR / "layout.json"


# ============================================================
# SERIALIZE LAYOUT
# ============================================================

def write_layout(layout):
    """
    Escribe el resultado del Layout Engine
    en output/layout.json.
    """

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with LAYOUT_FILE.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            layout,
            file,
            ensure_ascii=False,
            indent=2
        )


# ============================================================
# MAIN
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

    write_layout(layout)

    print()
    print("=" * 46)
    print("       COUNTDOWN OS — LAYOUT OUTPUT")
    print("=" * 46)

    print()
    print(f"Output: {LAYOUT_FILE}")

    print()
    print("🟢 layout.json generated successfully")

    print()