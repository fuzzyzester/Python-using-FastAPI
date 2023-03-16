# seed data to the database from a json file: seed.json
import json
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas

# Define a function to load data from the seed file and insert it into the database
def seed_db():
    with open("seed.json") as f:
        data = json.load(f)
        db = SessionLocal()
        for item_data in data:
            item = models.Item(**item_data)
            db.add(item)
        db.commit()
        db.close()

# Call the seed_db function to insert the data into the database
seed_db()
