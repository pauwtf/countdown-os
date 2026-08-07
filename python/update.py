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

    print("===== COUNTDOWN =====")
    print(countdown)


if __name__ == "__main__":
    main()