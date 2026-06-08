import os
from datetime import datetime, timezone
from pymongo import MongoClient


MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "cybersec_agent")


def get_database():
    client = MongoClient(MONGO_URL)
    return client[MONGO_DB_NAME]


def save_conversation(user_id, question, response, theme="unknown"):
    db = get_database()

    document = {
        "user_id": user_id,
        "question": question,
        "response": response,
        "theme": theme,
        "created_at": datetime.now(timezone.utc)
    }

    db.conversations.insert_one(document)


def get_user_history(user_id, limit=10):
    db = get_database()

    conversations = (
        db.conversations
        .find({"user_id": user_id})
        .sort("created_at", -1)
        .limit(limit)
    )

    return list(conversations)