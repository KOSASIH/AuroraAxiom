# src/backend/app.py
from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from src.backend.models import DisasterPredictionModel

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///aurora_axiom.db"
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class DisasterPrediction(Resource):
    def post(self):
        data = request.get_json()
        model = DisasterPredictionModel()
        prediction = model.predict(data)
        return jsonify({"prediction": prediction})

class PreventionMeasures(Resource):
    def post(self):
        data = request.get_json()
        # implement prevention measures logic
        return jsonify({"prevention_measures": "implemented"})

class MitigationMeasures(Resource):
    def post(self):
        data = request.get_json()
        # implement mitigation measures logic
        return jsonify({"mitigation_measures": "implemented"})

class DataVisualization(Resource):
    def get(self):
        # generate visualization data
        data = {"labels": ["label1", "label2"], "values": [10, 20]}
        return jsonify(data)

api.add_resource(DisasterPrediction, "/predict")
api.add_resource(PreventionMeasures, "/prevent")
api.add_resource(MitigationMeasures, "/mitigate")
api.add_resource(DataVisualization, "/visualize")

if __name__ == "__main__":
    app.run(debug=True)
