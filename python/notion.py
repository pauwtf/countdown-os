from notion_client import Client
import os


def get_notion_client():
    token = os.environ["NOTION_TOKEN"]
    return Client(auth=token)


def test_database():
    notion = get_notion_client()
    database_id = os.environ["DATABASE_ID"]

    response = notion.databases.retrieve(
        database_id=database_id
    )

    print("✅ DATABASE ENCONTRADA")
    print(response)


if __name__ == "__main__":
    test_database()