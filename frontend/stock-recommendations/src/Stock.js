// src/Stock.js

import React from 'react';
import './Stock.css';

const Stock = ({ name, symbol, action }) => {
  return (
    <div className="stock">
      <h3>{name}</h3>
      <p>Symbol: {symbol}</p>
      <p>Action: {action}</p>
    </div>
  );
}

export default Stock;
