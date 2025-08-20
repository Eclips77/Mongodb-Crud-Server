import os

MONGODB_HOST = os.getenv("MONGODB_HOST", "mongodb://localhost")
MONGODB_PORT = int(os.getenv("MONGODB_PORT", 27017))
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "restdb")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "restaurants")
