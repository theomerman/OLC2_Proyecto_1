from flask import Blueprint, request, jsonify

routes = Blueprint('routes', __name__)

#receive code from client
@routes.route('/sendCode', methods=['POST'])
def sendCode():
    data = request.get_json()
    x = data.get('code')
    print(x)
    return f'We parse: {x}', 200