// src/App.js

import React, { useState, useEffect } from 'react';
import './App.css';
import StockList from './StockList';

const App = () => {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    fetchStockRecommendations();
  }, []);

  const fetchStockRecommendations = async () => {
    try {
      const apiUrl = 'https://wsb-advise.herokuapp.com/api/stock_recommendations';
      const response = await fetch(apiUrl);
      const data = await response.json();
      setRecommendations(data);
    } catch (error) {
      console.error('Error fetching stock recommendations:', error);
    }
  };

  const buyRecommendations = recommendations.filter(
    stock => stock.action.toLowerCase() === 'buy'
  );

  const sellRecommendations = recommendations.filter(
    stock => stock.action.toLowerCase() === 'sell'
  );

  return (
    <div className="App">
      <header className="App-header">
        <h1>r/WallStreetBets Roulette: Today's WSB Gamble</h1>
      </header>
      <main className="stock-lists">
        <StockList title="Buy" stocks={buyRecommendations} />
        <StockList title="Sell" stocks={sellRecommendations} />
      </main>
    </div>
  );
};

export default App;
