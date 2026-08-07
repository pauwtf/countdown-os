from notion import get_events


def main():
    events = get_events()

    print(f"Eventos encontrados: {len(events)}")

    for event in events:
        print(event)


if __name__ == "__main__":
    main()
