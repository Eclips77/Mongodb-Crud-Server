import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "restdb")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "soliders")

