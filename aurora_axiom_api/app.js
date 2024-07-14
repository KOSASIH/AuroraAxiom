const express = require('express');
const app = express();
const cors = require('cors');
const bodyParser = require('body-parser');

app.use(cors());
app.use(bodyParser.json());

const disasterData = require('./data/disaster_data.json');

app.get('/api/disasters', (req, res) => {
  res.json(disasterData);
});

app.post('/api/predict', (req, res) => {
  const { latitude, longitude, timestamp } = req.body;
  // Call the AI/ML model to make a prediction
  const prediction = makePrediction(latitude, longitude, timestamp);
  res.json({ prediction });
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
