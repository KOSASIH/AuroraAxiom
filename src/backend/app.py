# src/backend/app.py
from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from src.backend.models import DisasterPredictionModel, PreventionMeasuresModel, MitigationMeasuresModel
from src.backend.utils import DataProcessor, VisualizationGenerator

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
        model = PreventionMeasuresModel()
        prevention_measures = model.predict(data)
        return jsonify({"prevention_measures": prevention_measures})

class MitigationMeasures(Resource):
    def post(self):
        data = request.get_json()
        model = MitigationMeasuresModel()
        mitigation_measures = model.predict(data)
        return jsonify({"mitigation_measures": mitigation_measures})

class DataVisualization(Resource):
    def get(self):
        data_processor = DataProcessor()
        data = data_processor.process_data()
        visualization_generator = VisualizationGenerator()
        visualization = visualization_generator.generate_visualization(data)
        return send_file(visualization, mimetype="image/png")

class RealtimeMonitoring(Resource):
    def get(self):
        data_processor = DataProcessor()
        data = data_processor.process_realtime_data()
        return jsonify({"realtime_data": data})

api.add_resource(DisasterPrediction, "/predict")
api.add_resource(PreventionMeasures, "/prevent")
api.add_resource(MitigationMeasures, "/mitigate")
api.add_resource(DataVisualization, "/visualize")
api.add_resource(RealtimeMonitoring, "/monitor")

if __name__ == "__main__":
    app.run(debug=True)
