import React from 'react';
import './Stock.css';

const Stock = ({ ticker, action }) => {
  return (
    <div className={`stock ${action}`}>
      <h3>{ticker}</h3>
    </div>
  );
}

export default Stock;
