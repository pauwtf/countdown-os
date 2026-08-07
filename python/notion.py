from notion_client import Client
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Credenciales
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

# Cliente de Notion
notion = Client(auth=NOTION_TOKEN)


def get_events():
    """Obtiene todos los eventos de la base de datos."""

    response = notion.databases.query(
        database_id=DATABASE_ID
    )

    return response["results"]
