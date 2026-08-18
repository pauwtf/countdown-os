import os

from notion_client import Client


def get_notion_client():
    """
    Crea y devuelve un cliente autenticado de Notion.

    El token se obtiene desde la variable de entorno
    NOTION_TOKEN.
    """

    token = os.environ["NOTION_TOKEN"]

    return Client(auth=token)


def get_events():
    """
    Obtiene los eventos directamente desde el data source
    de Notion.

    Devuelve la respuesta cruda de la API para que
    event_parser.py se encargue de normalizarla.
    """

    notion = get_notion_client()

    data_source_id = os.environ["DATA_SOURCE_ID"]

    response = notion.data_sources.query(
        data_source_id=data_source_id
    )

    return response["results"]