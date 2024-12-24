from flask import Blueprint, request, jsonify
from models.recipe import Recipe
from app import db

recipe = Blueprint('recipe', __name__)

@recipe.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([{"id": r.id, "name": r.name, "portions_yield": r.portions_yield} for r in recipes])

@recipe.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        return jsonify({"id": recipe.id, "name": recipe.name, "instructions": recipe.instructions, "portions_yield": recipe.portions_yield})
    return jsonify({"message": "Recipe not found"}), 404
