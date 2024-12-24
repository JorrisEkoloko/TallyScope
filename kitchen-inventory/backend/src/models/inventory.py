from app import db

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    current_portions = db.Column(db.Integer, default=0)
    required_portions = db.Column(db.Integer, nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey('stations.id'))
