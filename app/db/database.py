from faunadb.client import FaunaClient
from app.config import FAUNA_SECRET_KEY

client = FaunaClient(secret=FAUNA_SECRET_KEY)

collections = [
    # "users"
]