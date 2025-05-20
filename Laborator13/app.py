from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
SECRET_KEY = "secret_key"
jwt = JWTManager(app)
@app.route('/',methods=['GET'])
def home():
    return "Welcome to the homepage!"


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/auth", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# Funcție de validare a token-ului
def validate_token(token):
    try:
        # Decodificarea token-ului JWT
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


@app.route('/auth/jwtStore', methods=['GET'])
def verify_jwt():

    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({"message": "Authorization header missing"}), 400

    token = auth_header.split(" ")[1]

    decoded_token = validate_token(token)

    if not decoded_token:
        return jsonify({"message": "Invalid or expired token"}), 404


    user_role = get_user_role_from_db(decoded_token['user_id'])

    if not user_role:
        return jsonify({"message": "User not found"}), 404


    return jsonify({"role": user_role}), 200

def get_user_role_from_db(user_id):
    if user_id == 123:
        return "admin"
    return None


if __name__ == "__main__":
    app.run()