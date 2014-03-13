from flask import Blueprint, jsonify, Response


numbers_blueprint = Blueprint('numbers_blueprint', __name__)


NUMBER_TRANSLATOR = {
    1: "one",
    2: "two",
    3: "three"
}


def translate_number(number):
    """
    Provided a integer number, return its name in English.
    """
    return NUMBER_TRANSLATOR[number]


@numbers_blueprint.route("/numbers/<int:number>")
def route_number(number):
    """
    Provided a integer number, return its name in English.
    """
    response = translate_number(number)

    if response:
        return response
    else:
        msg = u"unknown number, sorry"
        response = jsonify({u"error": msg})
        response.status_code = 500
        return response