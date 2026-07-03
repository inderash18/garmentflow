from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

class Database:
    client: AsyncIOMotorClient = None
    db = None

db_instance = Database()

async def connect_db():
    logger.info(f"Connecting to MongoDB at {settings.mongo_url}")
    db_instance.client = AsyncIOMotorClient(settings.mongo_url)
    db_instance.db = db_instance.client[settings.mongo_db_name]
    # Ensure unique indexes
    await db_instance.db.users.create_index("email", unique=True)
    await db_instance.db.departments.create_index("name", unique=True)
    logger.info("MongoDB connection and indexes initialized.")

async def disconnect_db():
    if db_instance.client:
        db_instance.client.close()
        logger.info("MongoDB disconnected.")

def get_db():
    return db_instance.db
