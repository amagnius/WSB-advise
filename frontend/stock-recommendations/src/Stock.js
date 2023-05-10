// src/Stock.js

import React from 'react';
import './Stock.css';

const Stock = ({ ticker, action }) => {
  return (
    <div className="stock">
      <h3>{ticker}</h3>
      <p>Symbol: {ticker}</p>
      <p>Action: {action}</p>
    </div>
  );
}

export default Stock;
