from notion_client import Client
import os


def get_notion_client():
    token = os.environ["NOTION_TOKEN"]
    return Client(auth=token)


def get_events():
    notion = get_notion_client()
    data_source_id = os.environ["DATA_SOURCE_ID"]

    response = notion.data_sources.query(
        data_source_id=data_source_id
    )

    return response["results"]