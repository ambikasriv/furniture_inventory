from flask import Blueprint, request, jsonify
from .models import Furniture, db

main = Blueprint('main', __name__)

@main.route('/furniture', methods=['POST'])
def add_furniture():
    data = request.get_json()
    new_furniture = Furniture(
        name=data['name'],
        description=data['description'],
        quantity=data['quantity'],
        location=data['location']
    )
    db.session.add(new_furniture)
    db.session.commit()
    return jsonify(new_furniture.to_dict()), 201

@main.route('/furniture', methods=['GET'])
def get_furniture():
    furniture_items = Furniture.query.all()
    return jsonify([item.to_dict() for item in furniture_items])

@main.route('/furniture/<int:id>', methods=['PUT'])
def update_furniture(id):
    data = request.get_json()
    furniture = Furniture.query.get_or_404(id)
    furniture.name = data.get('name', furniture.name)
    furniture.description = data.get('description', furniture.description)
    furniture.quantity = data.get('quantity', furniture.quantity)
    furniture.location = data.get('location', furniture.location)
    db.session.commit()
    return jsonify(furniture.to_dict())

@main.route('/furniture/<int:id>', methods=['DELETE'])
def delete_furniture(id):
    furniture = Furniture.query.get_or_404(id)
    db.session.delete(furniture)
    db.session.commit()
    return '', 204