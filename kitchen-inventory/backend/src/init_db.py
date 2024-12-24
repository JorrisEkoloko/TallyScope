from app import db
from models.user import User
from models.station import Station
from models.inventory import InventoryItem
from models.recipe import Recipe

def init_db():
    print("Creating database tables...")
    db.create_all()
    print("Database tables created successfully!")


if __name__ == "__main__":
    init_db()
