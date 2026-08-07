import json
from pathlib import Path

from notion import get_events
from event_parser import parse_events
from countdown import get_active_event, calculate_countdown


def main():
    events = get_events()
    parsed_events = parse_events(events)

    active_event = get_active_event(parsed_events)

    if active_event is None:
        print("No hay ningún evento activo.")
        return

    countdown = calculate_countdown(active_event)

    output = {
        "title": countdown["title"],
        "start_date": countdown["start_date"],
        "target_date": countdown["target_date"],
        "days_remaining": countdown["days_remaining"],
        "progress": countdown["progress"],
        "category": active_event["category"]
    }

    output_path = Path(__file__).parent.parent / "output" / "countdown.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(output, file, ensure_ascii=False, indent=2)

    print("✅ countdown.json generado")
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()