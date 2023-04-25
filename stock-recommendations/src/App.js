// src/App.js

import React, { useState, useEffect } from 'react';
import './App.css';
import Stock from './Stock';

const App = () => {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    fetchStockRecommendations();
  }, []);

  const fetchStockRecommendations = async () => {
    try {
      // Replace with your Java backend's REST API URL
      const apiUrl = 'https://your-java-backend-url/api/recommendations';
      const response = await fetch(apiUrl);
      const data = await response.json();
      setRecommendations(data);
    } catch (error) {
      console.error('Error fetching stock recommendations:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Today's Stock Recommendations</h1>
      </header>
      <main className="stocks-container">
        {recommendations.map(stock => (
          <Stock
            key={stock.symbol}
            name={stock.name}
            symbol={stock.symbol}
            action={stock.action}
          />
        ))}
      </main>
    </div>
  );
}

export default App;
