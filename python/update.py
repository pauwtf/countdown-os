import json
from pathlib import Path

from notion import get_events
from event_parser import parse_events
from countdown import get_active_event, calculate_countdown
from presentation import prepare_event


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
        print("No hay ningún evento activo.")
        return

    # ========================================================
    # CALCULATE COUNTDOWN
    # ========================================================

    countdown = calculate_countdown(active_event)

    # ========================================================
    # PREPARE PRESENTATION DATA
    # ========================================================

    output = prepare_event(
        active_event,
        countdown
    )

    # ========================================================
    # OUTPUT PATH
    # ========================================================

    output_path = (
        Path(__file__).parent.parent
        / "output"
        / "countdown.json"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # ========================================================
    # WRITE JSON
    # ========================================================

    with open(
        output_path,
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
    # LOG
    # ========================================================

    print("✅ countdown.json generado")
    print(
        json.dumps(
            output,
            ensure_ascii=False,
            indent=2
        )
    )


if __name__ == "__main__":
    main()