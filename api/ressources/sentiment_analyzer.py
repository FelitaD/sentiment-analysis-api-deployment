from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.models.sentiment_analyzer import SentimentModel
from api.models.user import UserModel


class SentimentAnalyzer(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('sentence', type=str, required=True, help='Enter the sentence you want to analyze.')

        self.data = self.parser.parse_args()
        self.sentiment = SentimentModel(self.data['sentence'])

        self.response = {'sentence': self.data['sentence'],
                         'processed_sentenced': self.sentiment.processed_sentence}


class SentimentAnalyzerV1(SentimentAnalyzer):

    @jwt_required()
    def post(self):
        user = UserModel.find_by_username(get_jwt_identity())
        if user.v1:
            self.response['polarity'] = self.sentiment.polarity
            return self.response, 200

        return {'message': 'Check permission for this version.'}, 401


class SentimentAnalyzerV2(SentimentAnalyzer):

    @jwt_required()
    def post(self):
        user = UserModel.find_by_username(get_jwt_identity())
        if user.v2:
            self.response['vader_compound'] = self.sentiment.compound
            return self.response, 200

        return {'message': 'Check permission for this version.'}, 401
