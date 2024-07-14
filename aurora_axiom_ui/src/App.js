import React, { useState, useEffect } from 'eact';
import axios from 'axios';

function App() {
  const [disasters, setDisasters] = useState([]);
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:3000/api/disasters')
     .then(response => {
        setDisasters(response.data);
      })
     .catch(error => {
        console.error(error);
      });
  }, []);

  const handlePredict = (latitude, longitude, timestamp) => {
    axios.post('http://localhost:3000/api/predict', { latitude, longitude, timestamp })
     .then(response => {
        setPrediction(response.data.prediction);
      })
     .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>AuroraAxiom</h1>
      <ul>
        {disasters.map(disaster => (
          <li key={disaster.id}>{disaster.name}</li>
        ))}
      </ul>
      <form>
        <label>Latitude:</label>
        <input type="number" value={latitude} onChange={e => setLatitude(e.target.value)} />
        <br />
        <label>Longitude:</label>
        <input type="number" value={longitude} onChange={e => setLongitude(e.target.value)} />
        <br />
        <label>Timestamp:</label>
        <input type="datetime-local" value={timestamp} onChange={e => setTimestamp(e.target.value)} />
        <br />
        <button onClick={() => handlePredict(latitude, longitude, timestamp)}>Make Prediction</button>
      </form>
      {prediction && <p>Prediction: {prediction}</p>}
    </div>
  );
}

export default App;
