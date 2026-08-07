from notion_client import Client
import os


def get_notion_client():
    token = os.environ["NOTION_TOKEN"]
    return Client(auth=token)


def get_events():
    notion = get_notion_client()
    database_id = os.environ["DATABASE_ID"]

    response = notion.databases.query(
        database_id=database_id
    )

    return response["results"]
