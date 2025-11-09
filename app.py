from flask import Flask
from flask_restful import Api, Resource, reqparse
from data.userManager import UserManager
from logging_file.log_config import *


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("age", type=int)

class Main(Resource):
    def get(self, user_id):
        logging.info("GET/user_id")

        user = UserManager.get_user(user_id)

        if not user:
            logging.warning("User not found")
            return {"message": "User not found"}, 404

        return user

    def delete(self, user_id):
        logging.info("DELETE/user_id")

        user = UserManager.delete_user(user_id)

        if not user:
            logging.warning("User not found")
            return {"message": "User not found"}, 404

        return user



    def put(self, user_id):
        logging.info("PUT/user_id")

        args = parser.parse_args()
        user = UserManager.update_user(user_id, args)
        if not user:
            logging.warning("User not found")
            return {"message": "User not found"}, 404

        return user

api.add_resource(Main, "/api/app/users/<int:user_id>")

class UserList(Resource):
    def post(self):
        logging.info("POST")
        args = parser.parse_args()
        user = UserManager.add_user(args)

        return user

    def get(self):
        logging.info("GET")
        return UserManager.get_all_user()

api.add_resource(UserList, "/api/app/users")

if __name__ == "__main__":
    app.run(debug=True, port=8090, host="localhost")