from notion import get_events
from event_parser import parse_events


def main():
    events = get_events()

    parsed_events = parse_events(events)

    print(f"Eventos encontrados: {len(parsed_events)}")

    for index, event in enumerate(parsed_events, start=1):
        print(f"\n===== EVENTO {index} =====")
        print(event)


if __name__ == "__main__":
    main()