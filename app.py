import flask
from flask_restful import Api


from create_app import create_app
from ressources.sentiment_analyzer import SentimentAnalyzerV1, SentimentAnalyzerV2
from ressources.user import UserLogin, UserPermissions, UserWelcome
from ressources.status import Status
from db.create_user_db import create_user_db

app = create_app()
api = Api(app)
api.add_resource(Status, '/status')
api.add_resource(UserWelcome, '/welcome/<string:name>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserPermissions, '/permissions')
api.add_resource(SentimentAnalyzerV1, '/v1/sentiment')
api.add_resource(SentimentAnalyzerV2, '/v2/sentiment')


@app.before_first_request
def register_users():
    create_user_db()


if __name__ == '__main__':
    create_user_db()
    app.run(host='localhost', debug=True)
