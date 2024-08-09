from flask import Blueprint, request, jsonify

from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.views.http_types.http_request import HttpRequest

pet_route_bp = Blueprint("pets_routes", __name__)

@pet_route_bp.route("/pets", methods=["GET"])
def list_pets():
    http_request = HttpRequest()
    
    view = pet_lister_composer()
    
    http_response = view.handle(http_request)
    
    return jsonify(http_response.body), http_response.status_code


@pet_route_bp.route("/pets/<pet_name>", methods=["DELETE"])
def delete_pet(pet_name):
    http_request = HttpRequest(param={"pet_name": pet_name})
    
    view = pet_deleter_composer()
    
    http_response = view.handle(http_request)
    
    return jsonify(http_response.body), http_response.status_code