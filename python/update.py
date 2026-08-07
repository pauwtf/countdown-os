from notion import get_events


def main():
    events = get_events()

    print(f"Eventos encontrados: {len(events)}")

    for index, event in enumerate(events, start=1):
        print(f"\n===== EVENTO {index} =====")
        print(event["properties"])


if __name__ == "__main__":
    main()