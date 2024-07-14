# src/backend/tests/test_app.py
import unittest
from src.backend.app import app

class TestApp(unittest.TestCase):
    def test_disaster_prediction(self):
        tester = app.test_client(self)
        response = tester.post("/predict", json={"input_data": "test"})
        self.assertEqual(response.status_code, 200)

    def test_prevention_measures(self):
        tester = app.test_client(self)
        response = tester.post("/prevent", json={"input_data": "test"})
        self.assertEqual(response.status_code, 200)

    def test_mitigation_measures(self):
        tester = app.test_client(self)
        response = tester.post("/mitigate", json={"input_data": "test"})
        self.assertEqual(response.status_code, 200)

    def test_data_visualization(self):
        tester = app.test_client(self)
        response = tester.get("/visualize")
        self.assertEqual(response.status_code, 200)

    def test_realtime_monitoring(self):
        tester = app.test_client(self)
        response = tester.get("/monitor")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
