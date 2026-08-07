from notion_client import Client
import os


def get_notion_client():
    token = os.environ["NOTION_TOKEN"]
    return Client(auth=token)


def test_data_sources():
    notion = get_notion_client()
    database_id = os.environ["DATABASE_ID"]

    response = notion.databases.retrieve(
        database_id=database_id
    )

    print("✅ DATABASE ENCONTRADA")
    print("DATABASE ID:", database_id)

    print("\nDATA SOURCES:")

    for data_source in response.get("data_sources", []):
        print(data_source)


if __name__ == "__main__":
    test_data_sources()