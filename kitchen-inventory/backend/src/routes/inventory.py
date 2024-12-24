from flask import Blueprint, request, jsonify
from models.inventory import InventoryItem
from app import db

inventory = Blueprint('inventory', __name__)

@inventory.route('/inventory', methods=['GET'])
def get_inventory():
    items = InventoryItem.query.all()
    return jsonify([{"id": item.id, "name": item.name, "current_portions": item.current_portions, "required_portions": item.required_portions} for item in items])

@inventory.route('/inventory/update', methods=['POST'])
def update_inventory():
    data = request.json
    item = InventoryItem.query.get(data['id'])
    if item:
        item.current_portions = data['current_portions']
        db.session.commit()
        return jsonify({"message": "Inventory updated successfully"}), 200
    return jsonify({"message": "Item not found"}), 404
