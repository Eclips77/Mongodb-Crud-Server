import os

MONGODB_HOST = os.getenv("MONGODB_HOST", "localhost")
MONGODB_PORT = int(os.getenv("MONGODB_PORT", 27017))
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "documents_db")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "documents")
