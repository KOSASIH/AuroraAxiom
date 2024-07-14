import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('https://api.example.com/data')
      .then(response => {
        setData(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact component={() => <div>Welcome to the high-tech frontend!</div>} />
        <Route path="/data" component={() => <div>Data: {data}</div>} />
      </Switch>
    </BrowserRouter>
  );
}

export default App;
