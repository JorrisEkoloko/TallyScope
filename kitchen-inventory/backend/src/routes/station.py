from flask import Blueprint, request, jsonify
from models.station import Station
from app import db

station = Blueprint('station', __name__)

@station.route('/stations', methods=['GET'])
def get_stations():
    stations = Station.query.all()
    return jsonify([{"id": s.id, "name": s.name} for s in stations])

@station.route('/station/<int:station_id>/inventory', methods=['GET'])
def get_station_inventory(station_id):
    # Implement logic to get inventory for a specific station
    pass
