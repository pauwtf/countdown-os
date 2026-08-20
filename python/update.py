import json
from pathlib import Path

from notion import get_events
from event_parser import parse_events
from countdown import get_active_event, calculate_countdown
from presentation import prepare_event
from layout_output import generate_layout_file


def main():

    # ========================================================
    # GET EVENTS FROM NOTION
    # ========================================================

    events = get_events()
    parsed_events = parse_events(events)

    # ========================================================
    # FIND ACTIVE EVENT
    # ========================================================

    active_event = get_active_event(parsed_events)

    if active_event is None:
        print("⚠️ No hay ningún evento activo.")
        return

    # ========================================================
    # CALCULATE COUNTDOWN
    # ========================================================

    countdown = calculate_countdown(
        active_event
    )

    # ========================================================
    # PREPARE PRESENTATION DATA
    # ========================================================

    output = prepare_event(
        active_event,
        countdown
    )

    # ========================================================
    # OUTPUT DIRECTORY
    # ========================================================

    output_dir = (
        Path(__file__).parent.parent
        / "output"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    # ========================================================
    # WRITE COUNTDOWN JSON
    # ========================================================

    countdown_path = (
        output_dir
        / "countdown.json"
    )

    with countdown_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            ensure_ascii=False,
            indent=2
        )

    # ========================================================
    # GENERATE LAYOUT JSON
    # ========================================================

    layout_path = generate_layout_file(
        output
    )

    # ========================================================
    # LOG
    # ========================================================

    print()
    print("=" * 50)
    print("       COUNTDOWN OS — UPDATE")
    print("=" * 50)

    print()

    print(
        f"✅ countdown.json generado: "
        f"{countdown_path}"
    )

    print(
        f"✅ layout.json generado: "
        f"{layout_path}"
    )

    print()

    print("COUNTDOWN DATA")
    print("-" * 50)

    print(
        json.dumps(
            output,
            ensure_ascii=False,
            indent=2
        )
    )

    print()

    print("LAYOUT")
    print("-" * 50)

    print(
        json.dumps(
            json.loads(
                layout_path.read_text(
                    encoding="utf-8"
                )
            ),
            ensure_ascii=False,
            indent=2
        )
    )

    print()
    print("🟢 UPDATE COMPLETED")
    print()


if __name__ == "__main__":
    main()